/*
Runnable ONLY after deliberate opt-in below. Original book lab, 2026-10-08.
Execution location: isolated BookWarehouse.
DESTRUCTIVE: removes exactly the eight capstone lab tables and their data.
Does not alter the four core book tables, the schema, or other chapter labs.
Review and retain needed evidence first. Default is refusal, not deletion.
*/
DECLARE @ConfirmIsolatedLabCleanup bit = 0;

IF DB_NAME() <> 'BookWarehouse' OR @ConfirmIsolatedLabCleanup <> 1
    THROW 53290, 'Cleanup refused. Confirm isolated BookWarehouse and opt in explicitly.', 1;

IF @@TRANCOUNT <> 0
    THROW 53291, 'Run cleanup without an existing user transaction.', 1;

BEGIN TRY
    BEGIN TRANSACTION;
    DROP TABLE IF EXISTS book.Lab32MigratedSales;
    DROP TABLE IF EXISTS book.Lab32MigratedCustomer;
    DROP TABLE IF EXISTS book.Lab32MigratedProduct;
    DROP TABLE IF EXISTS book.Lab32MigratedDate;
    DROP TABLE IF EXISTS book.Lab32StageSales;
    DROP TABLE IF EXISTS book.Lab32StageCustomer;
    DROP TABLE IF EXISTS book.Lab32StageProduct;
    DROP TABLE IF EXISTS book.Lab32StageDate;
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
    THROW;
END CATCH;
