/*
Runnable, read-only. Execute in the source SQL database or BookWarehouse.
Metadata visibility follows the caller's permissions. No DDL or data writes.
Source register G14. Adapted from Mark Pryce-Maher,
tables-columns-datatypes.sql, 2026-03-10.
Canonical: https://gist.github.com/MarkPryceMaherMSFT/32f9e21deb2f784bbb47b2d50f71d412
Pinned revision:
https://gist.github.com/MarkPryceMaherMSFT/32f9e21deb2f784bbb47b2d50f71d412/47df0d6920436ac9a85ece3d3fea4fc6d4fe0aaa
Changes: restrict to book; expose object/column IDs and collation;
name max_length explicitly as bytes. No automatic type conversion.
Author-authorized use for this book; source gist has no explicit license.
*/
SELECT s.name AS SchemaName,
       t.name AS TableName,
       t.object_id AS ObjectId,
       c.column_id AS ColumnOrdinal,
       c.name AS ColumnName,
       ty.name AS DataType,
       c.max_length AS MaxLengthBytes,
       c.precision AS NumericPrecision,
       c.scale AS NumericOrTimeScale,
       c.is_nullable AS IsNullable,
       c.collation_name AS CollationName
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
JOIN sys.columns AS c ON c.object_id = t.object_id
JOIN sys.types AS ty ON ty.user_type_id = c.user_type_id
WHERE s.name = 'book'
ORDER BY s.name, t.name, c.column_id;
