/*
Template, read-only. Execute on an approved SQL Server-family source database.
Substitute only the two filter values below; no target deployment occurs.
Source register G15. Adapted discovery pattern:
Mark Pryce-Maher, migrate_views.py, 2025-08-11.
Canonical: https://gist.github.com/MarkPryceMaherMSFT/a834d3043c38ea498029e147d061624b
Pinned revision:
https://gist.github.com/MarkPryceMaherMSFT/a834d3043c38ea498029e147d061624b/aa59d2d2453a61dbe5b57383cd79bb521f0a5be6
Changes: SQL-only review; schema-qualified filtering; dependency inventory;
no regex rewriting, credentials, automatic execution, or definition-file writes.
Author-authorized use for this book; source gist has no explicit license.
Output can contain sensitive source code. Use an approved review destination.
*/
DECLARE @SchemaName sysname = N'book';
DECLARE @ViewName sysname = N'RevenueByCountry';

SELECT s.name AS SchemaName,
       v.name AS ViewName,
       v.object_id AS ObjectId,
       m.definition AS SourceDefinition,
       CASE WHEN m.definition IS NULL
            THEN 'Definition unavailable: investigate before proceeding'
            ELSE 'Review required'
       END AS ReviewState
FROM sys.views AS v
JOIN sys.schemas AS s ON s.schema_id = v.schema_id
LEFT JOIN sys.sql_modules AS m ON m.object_id = v.object_id
WHERE s.name = @SchemaName AND v.name = @ViewName
ORDER BY s.name, v.name;

SELECT s.name AS SchemaName,
       v.name AS ViewName,
       d.referenced_server_name AS ReferencedServer,
       d.referenced_database_name AS ReferencedDatabase,
       d.referenced_schema_name AS ReferencedSchema,
       d.referenced_entity_name AS ReferencedEntity,
       d.is_ambiguous AS IsAmbiguous
FROM sys.views AS v
JOIN sys.schemas AS s ON s.schema_id = v.schema_id
JOIN sys.sql_expression_dependencies AS d ON d.referencing_id = v.object_id
WHERE s.name = @SchemaName AND v.name = @ViewName
ORDER BY d.referenced_database_name,
         d.referenced_schema_name,
         d.referenced_entity_name;
