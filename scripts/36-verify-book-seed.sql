-- Runnable read-only verification of the unchanged synthetic book seed.
-- Execute in BookWarehouse or the independently seeded BookLakehouse SQL endpoint.
-- Original book example, 2026-10-08. No third-party implementation copied.
-- Assumes chapter 4 or 5 seed, not a dataset with subsequent legitimate changes.
-- Diagnostic reads consume capacity. No tenant execution was performed here.

IF EXISTS (SELECT CustomerKey FROM book.DimCustomer
           GROUP BY CustomerKey HAVING COUNT_BIG(*) <> 1)
    THROW 50001, 'Duplicate synthetic customer keys.', 1;
IF EXISTS (SELECT ProductKey FROM book.DimProduct
           GROUP BY ProductKey HAVING COUNT_BIG(*) <> 1)
    THROW 50002, 'Duplicate synthetic product keys.', 1;
IF EXISTS (SELECT DateKey FROM book.DimDate
           GROUP BY DateKey HAVING COUNT_BIG(*) <> 1)
    THROW 50003, 'Duplicate synthetic date keys.', 1;
IF EXISTS (SELECT SalesKey FROM book.FactSales
           GROUP BY SalesKey HAVING COUNT_BIG(*) <> 1)
    THROW 50004, 'Duplicate synthetic sales keys.', 1;

IF EXISTS (
    SELECT 1
    FROM book.FactSales AS s
    LEFT JOIN book.DimCustomer AS c ON c.CustomerKey = s.CustomerKey
    LEFT JOIN book.DimProduct AS p ON p.ProductKey = s.ProductKey
    LEFT JOIN book.DimDate AS d ON d.DateKey = s.DateKey
    WHERE c.CustomerKey IS NULL OR p.ProductKey IS NULL OR d.DateKey IS NULL
)
    THROW 50005, 'Synthetic facts have missing dimension references.', 1;

DECLARE @Facts bigint, @Quantity bigint, @Revenue decimal(38,2);
SELECT @Facts = COUNT_BIG(*),
       @Quantity = SUM(CAST(Quantity AS bigint)),
       @Revenue = SUM(CAST(Quantity * UnitPrice AS decimal(18,2)))
FROM book.FactSales;

IF @Facts <> 6 OR @Quantity IS NULL OR @Quantity <> 10
   OR @Revenue IS NULL OR @Revenue <> 365.00
    THROW 50006, 'Book seed totals differ from six facts, ten units, revenue 365.', 1;

SELECT @Facts AS FactRows, @Quantity AS Quantity, @Revenue AS Revenue;
