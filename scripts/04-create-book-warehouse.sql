/*
RUNNABLE: Fabric Warehouse query editor, connected to BookWarehouse.
Effects: creates a NEW book schema, four tables, and the book's synthetic data.
Run the entire file as one batch, without an existing user transaction.
Safety: refuses an existing book schema; never drops, truncates, or overwrites.
If table creation/loading fails, its transaction rolls back. The newly created
empty schema can remain; investigate it rather than bypassing the safety check.
Do not run concurrently. This is a teaching seed, not a production loader.

Original book code, 8 October 2026. No third-party code copied.
Syntax references verified on that date:
https://learn.microsoft.com/en-us/fabric/data-warehouse/tables
https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types
https://learn.microsoft.com/en-us/fabric/data-warehouse/transactions
*/

IF DB_NAME() <> 'BookWarehouse'
    THROW 51000, 'Connect to the isolated BookWarehouse item before running this seed.', 1;

IF @@TRANCOUNT <> 0
    THROW 51001, 'Run the seed without an existing transaction.', 1;

IF SCHEMA_ID('book') IS NOT NULL
    THROW 51002, 'The book schema already exists. Nothing has been changed.', 1;

-- CREATE SCHEMA must be its own batch. Keep schema creation outside the
-- table/load transaction; do not imply that a failed load removes the schema.
EXEC ('CREATE SCHEMA book;');

BEGIN TRY
    BEGIN TRANSACTION;

    CREATE TABLE book.DimCustomer
    (
        CustomerKey int NOT NULL,
        CustomerName varchar(100) NOT NULL,
        CountryCode varchar(2) NOT NULL
    );

    CREATE TABLE book.DimProduct
    (
        ProductKey int NOT NULL,
        ProductName varchar(100) NOT NULL,
        Category varchar(50) NOT NULL
    );

    CREATE TABLE book.DimDate
    (
        DateKey int NOT NULL,
        CalendarDate date NOT NULL,
        CalendarYear smallint NOT NULL,
        CalendarMonth smallint NOT NULL
    );

    CREATE TABLE book.FactSales
    (
        SalesKey bigint NOT NULL,
        DateKey int NOT NULL,
        CustomerKey int NOT NULL,
        ProductKey int NOT NULL,
        Quantity int NOT NULL,
        UnitPrice decimal(12,2) NOT NULL,
        LastModifiedUtc datetime2(6) NOT NULL
    );

    INSERT INTO book.DimCustomer (CustomerKey, CustomerName, CountryCode)
    VALUES
        (1, 'Aster Retail', 'GB'),
        (2, 'Birch Stores', 'DE'),
        (3, 'Cedar Market', 'GB');

    INSERT INTO book.DimProduct (ProductKey, ProductName, Category)
    VALUES
        (10, 'Desk lamp', 'Home'),
        (20, 'Travel bag', 'Travel'),
        (30, 'Notebook', 'Stationery'),
        (40, 'Headphones', 'Electronics');

    INSERT INTO book.DimDate
        (DateKey, CalendarDate, CalendarYear, CalendarMonth)
    VALUES
        (20260101, '20260101', 2026, 1),
        (20260102, '20260102', 2026, 1),
        (20260103, '20260103', 2026, 1);

    INSERT INTO book.FactSales
        (SalesKey, DateKey, CustomerKey, ProductKey,
         Quantity, UnitPrice, LastModifiedUtc)
    VALUES
        (1001, 20260101, 1, 10, 2, 25.00, '2026-01-04T00:00:00'),
        (1002, 20260101, 2, 20, 1, 80.00, '2026-01-04T00:00:00'),
        (1003, 20260102, 1, 30, 3, 10.00, '2026-01-04T00:00:00'),
        (1004, 20260102, 3, 10, 1, 25.00, '2026-01-04T00:00:00'),
        (1005, 20260103, 2, 40, 2, 50.00, '2026-01-04T00:00:00'),
        (1006, 20260103, 3, 20, 1, 80.00, '2026-01-04T00:00:00');

    IF (SELECT COUNT_BIG(*) FROM book.DimCustomer) <> 3
       OR (SELECT COUNT_BIG(*) FROM book.DimProduct) <> 4
       OR (SELECT COUNT_BIG(*) FROM book.DimDate) <> 3
       OR (SELECT COUNT_BIG(*) FROM book.FactSales) <> 6
       OR (SELECT SUM(Quantity) FROM book.FactSales) <> 10
       OR (SELECT SUM(Quantity * UnitPrice) FROM book.FactSales) <> 365.00
        THROW 51003, 'The seed failed its row count or measure checks.', 1;

    IF (SELECT SUM(f.Quantity * f.UnitPrice)
        FROM book.FactSales AS f
        JOIN book.DimCustomer AS c ON c.CustomerKey = f.CustomerKey
        WHERE c.CountryCode = 'GB') <> 185.00
       OR (SELECT SUM(f.Quantity * f.UnitPrice)
           FROM book.FactSales AS f
           JOIN book.DimCustomer AS c ON c.CustomerKey = f.CustomerKey
           WHERE c.CountryCode = 'DE') <> 180.00
        THROW 51004, 'The seed failed its country reconciliation.', 1;

    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;
    THROW;
END CATCH;

SELECT COUNT_BIG(*) AS FactRows,
       SUM(Quantity) AS Quantity,
       CAST(SUM(Quantity * UnitPrice) AS decimal(18,2)) AS Revenue
FROM book.FactSales;

SELECT c.CountryCode,
       CAST(SUM(f.Quantity * f.UnitPrice) AS decimal(18,2)) AS Revenue
FROM book.FactSales AS f
JOIN book.DimCustomer AS c ON c.CustomerKey = f.CustomerKey
GROUP BY c.CountryCode
ORDER BY c.CountryCode;
