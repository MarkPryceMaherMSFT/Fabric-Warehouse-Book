"""
RUNNABLE: paste this entire file into one Fabric notebook PySpark cell.
Prerequisites: attach schema-enabled BookLakehouse as the DEFAULT lakehouse,
in the notebook's workspace; create an empty book schema in Lakehouse explorer.
Effects: creates four managed Delta tables in book, with original synthetic data.
Safety: checks all four names before writing and uses errorifexists, never
overwrite or append. Four table writes are NOT one multi-table transaction.
If interrupted, inspect the partial results; do not bypass the existence guard.
Run once, with no concurrent seed or other writer.

Original book code, 8 October 2026. No third-party code copied.
Syntax and mapping references verified on that date:
https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-schemas
https://learn.microsoft.com/en-us/fabric/data-engineering/notebookutils/notebookutils-runtime
https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types

Delta STRING columns map to endpoint varchar widths determined by the service,
not to the Warehouse seed's exact varchar lengths. Values and numeric/date types
are deliberately equivalent; SQL metadata need not be byte-for-byte identical.
"""

from datetime import date, datetime, timezone
from decimal import Decimal

import notebookutils
from pyspark.sql import functions as F
from pyspark.sql.types import (
    DateType,
    DecimalType,
    IntegerType,
    LongType,
    ShortType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)


context = notebookutils.runtime.context
if context.get("defaultLakehouseName") != "BookLakehouse":
    raise RuntimeError("Attach BookLakehouse as the notebook's default lakehouse.")
if context.get("defaultLakehouseWorkspaceId") != context.get("currentWorkspaceId"):
    raise RuntimeError("Use BookLakehouse in this notebook's own workspace.")

# This also fails before any write if book was not created or is inaccessible.
existing_tables = spark.sql("SHOW TABLES IN book").collect()
target_names = {"DimCustomer", "DimProduct", "DimDate", "FactSales"}
existing_names = {row["tableName"].casefold() for row in existing_tables}
collisions = sorted(name for name in target_names if name.casefold() in existing_names)
if collisions:
    raise RuntimeError(f"Refusing to replace existing book tables: {collisions}")

customer_schema = StructType([
    StructField("CustomerKey", IntegerType(), False),
    StructField("CustomerName", StringType(), False),
    StructField("CountryCode", StringType(), False),
])
product_schema = StructType([
    StructField("ProductKey", IntegerType(), False),
    StructField("ProductName", StringType(), False),
    StructField("Category", StringType(), False),
])
date_schema = StructType([
    StructField("DateKey", IntegerType(), False),
    StructField("CalendarDate", DateType(), False),
    StructField("CalendarYear", ShortType(), False),
    StructField("CalendarMonth", ShortType(), False),
])
fact_schema = StructType([
    StructField("SalesKey", LongType(), False),
    StructField("DateKey", IntegerType(), False),
    StructField("CustomerKey", IntegerType(), False),
    StructField("ProductKey", IntegerType(), False),
    StructField("Quantity", IntegerType(), False),
    StructField("UnitPrice", DecimalType(12, 2), False),
    StructField("LastModifiedUtc", TimestampType(), False),
])

customers = [
    (1, "Aster Retail", "GB"),
    (2, "Birch Stores", "DE"),
    (3, "Cedar Market", "GB"),
]
products = [
    (10, "Desk lamp", "Home"),
    (20, "Travel bag", "Travel"),
    (30, "Notebook", "Stationery"),
    (40, "Headphones", "Electronics"),
]
dates = [
    (20260101, date(2026, 1, 1), 2026, 1),
    (20260102, date(2026, 1, 2), 2026, 1),
    (20260103, date(2026, 1, 3), 2026, 1),
]
modified_utc = datetime(2026, 1, 4, 0, 0, 0, tzinfo=timezone.utc)
facts = [
    (1001, 20260101, 1, 10, 2, Decimal("25.00"), modified_utc),
    (1002, 20260101, 2, 20, 1, Decimal("80.00"), modified_utc),
    (1003, 20260102, 1, 30, 3, Decimal("10.00"), modified_utc),
    (1004, 20260102, 3, 10, 1, Decimal("25.00"), modified_utc),
    (1005, 20260103, 2, 40, 2, Decimal("50.00"), modified_utc),
    (1006, 20260103, 3, 20, 1, Decimal("80.00"), modified_utc),
]

if len(facts) != 6 or sum(row[4] for row in facts) != 10:
    raise ValueError("Unexpected in-memory fact count or quantity.")
if sum(row[4] * row[5] for row in facts) != Decimal("365.00"):
    raise ValueError("Unexpected in-memory revenue.")

datasets = [
    ("DimCustomer", customers, customer_schema),
    ("DimProduct", products, product_schema),
    ("DimDate", dates, date_schema),
    ("FactSales", facts, fact_schema),
]

previous_time_zone = spark.conf.get("spark.sql.session.timeZone")
previous_case_sensitivity = spark.conf.get("spark.sql.caseSensitive")
created_tables = []
try:
    spark.conf.set("spark.sql.session.timeZone", "UTC")
    spark.conf.set("spark.sql.caseSensitive", "true")
    # Build all explicitly typed DataFrames before committing any table.
    frames = [
        (name, spark.createDataFrame(rows, schema=schema))
        for name, rows, schema in datasets
    ]
    for name, frame in frames:
        qualified_name = f"book.{name}"
        frame.write.format("delta").mode("errorifexists").saveAsTable(qualified_name)
        created_tables.append(qualified_name)

    for name, rows, _ in datasets:
        if spark.table(f"book.{name}").count() != len(rows):
            raise RuntimeError(f"Stored row count differs for book.{name}.")

    stored_facts = spark.table("book.FactSales")
    totals = stored_facts.agg(
        F.count("*").alias("FactRows"),
        F.sum("Quantity").alias("Quantity"),
        F.sum(F.col("Quantity") * F.col("UnitPrice")).alias("Revenue"),
    ).first()
    if (totals["FactRows"], totals["Quantity"], totals["Revenue"]) != (
        6, 10, Decimal("365.00")
    ):
        raise RuntimeError(f"Stored fact reconciliation failed: {totals}")

    country_totals = (
        stored_facts.join(spark.table("book.DimCustomer"), "CustomerKey")
        .groupBy("CountryCode")
        .agg(F.sum(F.col("Quantity") * F.col("UnitPrice")).alias("Revenue"))
    )
    actual_countries = {
        row["CountryCode"]: row["Revenue"] for row in country_totals.collect()
    }
    if actual_countries != {"GB": Decimal("185.00"), "DE": Decimal("180.00")}:
        raise RuntimeError(f"Country reconciliation failed: {actual_countries}")

    print("Spark checks passed: 6 facts; quantity 10; revenue 365.00.")
    country_totals.orderBy("CountryCode").show()
    print("Now verify the independent SQL endpoint view after metadata sync.")
except Exception:
    print(f"Tables created before failure: {created_tables}")
    print("No tables were overwritten or automatically removed. Inspect before retrying.")
    raise
finally:
    spark.conf.set("spark.sql.session.timeZone", previous_time_zone)
    spark.conf.set("spark.sql.caseSensitive", previous_case_sensitivity)
