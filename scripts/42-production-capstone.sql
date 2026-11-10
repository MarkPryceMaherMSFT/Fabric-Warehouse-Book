/*
Runnable T-SQL, original book lab, 2026-10-08.
Execute as one batch in BookWarehouse after scripts\04-create-book-warehouse.sql.
Requires the unchanged common seed and permission to create book.Lab32 objects.
Effects: creates eight isolated, persistent Lab32 tables; never changes core tables.
Run once with no competing lab writer. Any existing lab object causes failure.
An explicit Warehouse transaction holds a consistent source snapshot and makes
the eight creates/loads atomic. This is NOT cross-platform change capture.
Expected outcomes are computed from the seed, not claimed tenant measurements.
References:
https://learn.microsoft.com/en-us/fabric/data-warehouse/transactions
https://learn.microsoft.com/en-us/sql/t-sql/statements/create-table-as-select-azure-sql-data-warehouse?view=fabric
*/
SET NOCOUNT ON;

IF DB_NAME() <> 'BookWarehouse'
    THROW 53200, 'Select the isolated BookWarehouse database before running.', 1;

IF @@TRANCOUNT <> 0
    THROW 53214, 'Run this lab without an existing user transaction.', 1;

IF EXISTS
(
    SELECT 1
    FROM sys.tables AS t
    JOIN sys.schemas AS s ON s.schema_id = t.schema_id
    WHERE s.name = 'book'
      AND t.name IN
      (
          'Lab32StageCustomer', 'Lab32StageProduct', 'Lab32StageDate',
          'Lab32StageSales', 'Lab32MigratedCustomer', 'Lab32MigratedProduct',
          'Lab32MigratedDate', 'Lab32MigratedSales'
      )
)
    THROW 53201, 'Lab32 objects already exist. Inspect them; no automatic reset.', 1;

BEGIN TRY
    BEGIN TRANSACTION;

    CREATE TABLE book.Lab32StageCustomer AS
    SELECT CustomerKey, CustomerName, CountryCode FROM book.DimCustomer;

    CREATE TABLE book.Lab32StageProduct AS
    SELECT ProductKey, ProductName, Category FROM book.DimProduct;

    CREATE TABLE book.Lab32StageDate AS
    SELECT DateKey, CalendarDate, CalendarYear, CalendarMonth FROM book.DimDate;

    CREATE TABLE book.Lab32StageSales AS
    SELECT SalesKey, DateKey, CustomerKey, ProductKey, Quantity,
           UnitPrice, LastModifiedUtc
    FROM book.FactSales;

    IF (SELECT COUNT_BIG(*) FROM book.Lab32StageCustomer) <> 3
       OR EXISTS
       (
           SELECT CustomerKey FROM book.Lab32StageCustomer
           GROUP BY CustomerKey HAVING COUNT_BIG(*) <> 1
       )
       OR EXISTS
       (
           SELECT 1 FROM book.Lab32StageCustomer
           WHERE NOT
           (
               (CustomerKey = 1 AND CustomerName = 'Aster Retail' AND CountryCode = 'GB')
               OR (CustomerKey = 2 AND CustomerName = 'Birch Stores' AND CountryCode = 'DE')
               OR (CustomerKey = 3 AND CustomerName = 'Cedar Market' AND CountryCode = 'GB')
           )
       )
        THROW 53202, 'Customer seed differs from the book fixture.', 1;

    IF (SELECT COUNT_BIG(*) FROM book.Lab32StageProduct) <> 4
       OR EXISTS
       (
           SELECT ProductKey FROM book.Lab32StageProduct
           GROUP BY ProductKey HAVING COUNT_BIG(*) <> 1
       )
       OR EXISTS
       (
           SELECT 1 FROM book.Lab32StageProduct
           WHERE NOT
           (
               (ProductKey = 10 AND ProductName = 'Desk lamp' AND Category = 'Home')
               OR (ProductKey = 20 AND ProductName = 'Travel bag' AND Category = 'Travel')
               OR (ProductKey = 30 AND ProductName = 'Notebook' AND Category = 'Stationery')
               OR (ProductKey = 40 AND ProductName = 'Headphones' AND Category = 'Electronics')
           )
       )
        THROW 53203, 'Product seed differs from the book fixture.', 1;

    IF (SELECT COUNT_BIG(*) FROM book.Lab32StageDate) <> 3
       OR EXISTS
       (
           SELECT DateKey FROM book.Lab32StageDate
           GROUP BY DateKey HAVING COUNT_BIG(*) <> 1
       )
       OR EXISTS
       (
           SELECT 1 FROM book.Lab32StageDate
           WHERE CalendarYear <> 2026 OR CalendarMonth <> 1
              OR NOT
              (
                  (DateKey = 20260101 AND CalendarDate = CAST('2026-01-01' AS date))
                  OR (DateKey = 20260102 AND CalendarDate = CAST('2026-01-02' AS date))
                  OR (DateKey = 20260103 AND CalendarDate = CAST('2026-01-03' AS date))
              )
       )
        THROW 53204, 'Date seed differs from the book fixture.', 1;

    IF (SELECT COUNT_BIG(*) FROM book.Lab32StageSales) <> 6
       OR EXISTS
       (
           SELECT SalesKey FROM book.Lab32StageSales
           GROUP BY SalesKey HAVING COUNT_BIG(*) <> 1
       )
        THROW 53205, 'Expected six facts with unique sales keys.', 1;

    DECLARE @MismatchCount bigint;
    WITH Expected AS
    (
        SELECT SalesKey, DateKey, CustomerKey, ProductKey, Quantity, UnitPrice
        FROM
        (
            VALUES
            (1001, 20260101, 1, 10, 2, CAST(25.00 AS decimal(12,2))),
            (1002, 20260101, 2, 20, 1, CAST(80.00 AS decimal(12,2))),
            (1003, 20260102, 1, 30, 3, CAST(10.00 AS decimal(12,2))),
            (1004, 20260102, 3, 10, 1, CAST(25.00 AS decimal(12,2))),
            (1005, 20260103, 2, 40, 2, CAST(50.00 AS decimal(12,2))),
            (1006, 20260103, 3, 20, 1, CAST(80.00 AS decimal(12,2)))
        ) AS v(SalesKey, DateKey, CustomerKey, ProductKey, Quantity, UnitPrice)
    )
    SELECT @MismatchCount = COUNT_BIG(*)
    FROM Expected AS e
    FULL OUTER JOIN book.Lab32StageSales AS s ON s.SalesKey = e.SalesKey
    WHERE e.SalesKey IS NULL OR s.SalesKey IS NULL
       OR s.DateKey <> e.DateKey OR s.CustomerKey <> e.CustomerKey
       OR s.ProductKey <> e.ProductKey OR s.Quantity <> e.Quantity
       OR s.UnitPrice <> e.UnitPrice
       OR s.LastModifiedUtc <> CAST('2026-01-04T00:00:00' AS datetime2(6));

    IF @MismatchCount <> 0
        THROW 53206, 'Fact values differ from the canonical six-row fixture.', 1;

    IF EXISTS
    (
        SELECT 1
        FROM book.Lab32StageSales AS f
        LEFT JOIN book.Lab32StageCustomer AS c ON c.CustomerKey = f.CustomerKey
        LEFT JOIN book.Lab32StageProduct AS p ON p.ProductKey = f.ProductKey
        LEFT JOIN book.Lab32StageDate AS d ON d.DateKey = f.DateKey
        WHERE c.CustomerKey IS NULL OR p.ProductKey IS NULL OR d.DateKey IS NULL
    )
        THROW 53207, 'A staged fact has a missing dimension relationship.', 1;

    CREATE TABLE book.Lab32MigratedCustomer AS
    SELECT CustomerKey, CustomerName, CountryCode FROM book.Lab32StageCustomer;

    CREATE TABLE book.Lab32MigratedProduct AS
    SELECT ProductKey, ProductName, Category FROM book.Lab32StageProduct;

    CREATE TABLE book.Lab32MigratedDate AS
    SELECT DateKey, CalendarDate, CalendarYear, CalendarMonth FROM book.Lab32StageDate;

    CREATE TABLE book.Lab32MigratedSales AS
    SELECT SalesKey, DateKey, CustomerKey, ProductKey, Quantity,
           UnitPrice, LastModifiedUtc
    FROM book.Lab32StageSales;

    -- Compare all columns and multiplicity across source, staging, and target.
    WITH Versions AS
    (
        SELECT CustomerKey, CustomerName, CountryCode, 0 AS Origin
        FROM book.DimCustomer
        UNION ALL
        SELECT CustomerKey, CustomerName, CountryCode, 1 FROM book.Lab32StageCustomer
        UNION ALL
        SELECT CustomerKey, CustomerName, CountryCode, 2 FROM book.Lab32MigratedCustomer
    )
    SELECT @MismatchCount = COUNT_BIG(*)
    FROM
    (
        SELECT CustomerKey, CustomerName, CountryCode
        FROM Versions
        GROUP BY CustomerKey, CustomerName, CountryCode
        HAVING SUM(CASE WHEN Origin = 0 THEN CAST(1 AS bigint) ELSE 0 END)
            <> SUM(CASE WHEN Origin = 1 THEN CAST(1 AS bigint) ELSE 0 END)
            OR SUM(CASE WHEN Origin = 1 THEN CAST(1 AS bigint) ELSE 0 END)
            <> SUM(CASE WHEN Origin = 2 THEN CAST(1 AS bigint) ELSE 0 END)
    ) AS Differences;

    IF @MismatchCount <> 0
        THROW 53208, 'Customer source/staging/target comparison failed.', 1;

    WITH Versions AS
    (
        SELECT ProductKey, ProductName, Category, 0 AS Origin FROM book.DimProduct
        UNION ALL
        SELECT ProductKey, ProductName, Category, 1 FROM book.Lab32StageProduct
        UNION ALL
        SELECT ProductKey, ProductName, Category, 2 FROM book.Lab32MigratedProduct
    )
    SELECT @MismatchCount = COUNT_BIG(*)
    FROM
    (
        SELECT ProductKey, ProductName, Category
        FROM Versions
        GROUP BY ProductKey, ProductName, Category
        HAVING SUM(CASE WHEN Origin = 0 THEN CAST(1 AS bigint) ELSE 0 END)
            <> SUM(CASE WHEN Origin = 1 THEN CAST(1 AS bigint) ELSE 0 END)
            OR SUM(CASE WHEN Origin = 1 THEN CAST(1 AS bigint) ELSE 0 END)
            <> SUM(CASE WHEN Origin = 2 THEN CAST(1 AS bigint) ELSE 0 END)
    ) AS Differences;

    IF @MismatchCount <> 0
        THROW 53209, 'Product source/staging/target comparison failed.', 1;

    WITH Versions AS
    (
        SELECT DateKey, CalendarDate, CalendarYear, CalendarMonth, 0 AS Origin
        FROM book.DimDate
        UNION ALL
        SELECT DateKey, CalendarDate, CalendarYear, CalendarMonth, 1 FROM book.Lab32StageDate
        UNION ALL
        SELECT DateKey, CalendarDate, CalendarYear, CalendarMonth, 2 FROM book.Lab32MigratedDate
    )
    SELECT @MismatchCount = COUNT_BIG(*)
    FROM
    (
        SELECT DateKey, CalendarDate, CalendarYear, CalendarMonth
        FROM Versions
        GROUP BY DateKey, CalendarDate, CalendarYear, CalendarMonth
        HAVING SUM(CASE WHEN Origin = 0 THEN CAST(1 AS bigint) ELSE 0 END)
            <> SUM(CASE WHEN Origin = 1 THEN CAST(1 AS bigint) ELSE 0 END)
            OR SUM(CASE WHEN Origin = 1 THEN CAST(1 AS bigint) ELSE 0 END)
            <> SUM(CASE WHEN Origin = 2 THEN CAST(1 AS bigint) ELSE 0 END)
    ) AS Differences;

    IF @MismatchCount <> 0
        THROW 53210, 'Date source/staging/target comparison failed.', 1;

    WITH Versions AS
    (
        SELECT SalesKey, DateKey, CustomerKey, ProductKey, Quantity,
               UnitPrice, LastModifiedUtc, 0 AS Origin FROM book.FactSales
        UNION ALL
        SELECT SalesKey, DateKey, CustomerKey, ProductKey, Quantity,
               UnitPrice, LastModifiedUtc, 1 FROM book.Lab32StageSales
        UNION ALL
        SELECT SalesKey, DateKey, CustomerKey, ProductKey, Quantity,
               UnitPrice, LastModifiedUtc, 2 FROM book.Lab32MigratedSales
    )
    SELECT @MismatchCount = COUNT_BIG(*)
    FROM
    (
        SELECT SalesKey, DateKey, CustomerKey, ProductKey, Quantity,
               UnitPrice, LastModifiedUtc
        FROM Versions
        GROUP BY SalesKey, DateKey, CustomerKey, ProductKey, Quantity,
                 UnitPrice, LastModifiedUtc
        HAVING SUM(CASE WHEN Origin = 0 THEN CAST(1 AS bigint) ELSE 0 END)
            <> SUM(CASE WHEN Origin = 1 THEN CAST(1 AS bigint) ELSE 0 END)
            OR SUM(CASE WHEN Origin = 1 THEN CAST(1 AS bigint) ELSE 0 END)
            <> SUM(CASE WHEN Origin = 2 THEN CAST(1 AS bigint) ELSE 0 END)
    ) AS Differences;

    IF @MismatchCount <> 0
        THROW 53211, 'Fact source/staging/target comparison failed.', 1;

    IF (SELECT SUM(CAST(Quantity AS bigint)) FROM book.Lab32MigratedSales) <> 10
       OR (SELECT SUM(CAST(Quantity * UnitPrice AS decimal(18,2)))
           FROM book.Lab32MigratedSales) <> CAST(365.00 AS decimal(18,2))
        THROW 53212, 'Quantity or revenue acceptance gate failed.', 1;

    DECLARE @GB decimal(18,2), @DE decimal(18,2);
    SELECT @GB = SUM(CASE WHEN c.CountryCode = 'GB'
                         THEN CAST(f.Quantity * f.UnitPrice AS decimal(18,2)) ELSE 0 END),
           @DE = SUM(CASE WHEN c.CountryCode = 'DE'
                         THEN CAST(f.Quantity * f.UnitPrice AS decimal(18,2)) ELSE 0 END)
    FROM book.Lab32MigratedSales AS f
    JOIN book.Lab32MigratedCustomer AS c ON c.CustomerKey = f.CustomerKey;

    IF @GB <> 185.00 OR @DE <> 180.00
        THROW 53213, 'Country revenue acceptance gate failed.', 1;

    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
    THROW;
END CATCH;

SELECT 'Staging' AS Phase, COUNT_BIG(*) AS FactRows,
       SUM(CAST(Quantity AS bigint)) AS Quantity,
       SUM(CAST(Quantity * UnitPrice AS decimal(18,2))) AS Revenue
FROM book.Lab32StageSales
UNION ALL
SELECT 'Migrated', COUNT_BIG(*), SUM(CAST(Quantity AS bigint)),
       SUM(CAST(Quantity * UnitPrice AS decimal(18,2)))
FROM book.Lab32MigratedSales;

SELECT c.CountryCode,
       SUM(CAST(f.Quantity * f.UnitPrice AS decimal(18,2))) AS Revenue
FROM book.Lab32MigratedSales AS f
JOIN book.Lab32MigratedCustomer AS c ON c.CustomerKey = f.CustomerKey
GROUP BY c.CountryCode
ORDER BY c.CountryCode;

SELECT 'PASS: canonical fixture, relationships, and all-column multiplicity' AS Acceptance;
