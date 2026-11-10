# Part III - The SQL analytics endpoint

[Book contents](../../index.md) | [Cover](../../README.md)

**Chapters 14-16**

The SQL analytics endpoint shares Warehouse SQL technology while retaining a source-owned data contract. Learn what is shared, what is read-only, how synchronization works, and where SQL versus OneLake security is enforced.

## Before you begin

Complete the independent Warehouse/Lakehouse setup and the shared SQL/security foundations. No mode or permission change is required merely to read this part.

## Chapter index

| Chapter | Subject |
| --- | --- |
| [14. The SQL analytics endpoint: shared engine, different contract](14-sql-analytics-endpoint.md) | Shared SQL technology, item/write differences, source authority and reader contracts. |
| [15. Metadata Sync: Legacy and New Architectures](15-metadata-sync-v1-v2.md) | Sync generations, Delta/type compatibility, identity-aware discovery and refresh. |
| [16. OneLake security: follow the identity to the data](16-onelake-security.md) | Endpoint modes and their side effects, groups and column-level access. |

## By the end of this part

Explain the endpoint's write/type/freshness boundaries, choose the correct metadata operation, and test OneLake access control/RLS/CLS without confusing it with SQL-engine permissions.

---

[Previous: Part II](../02-building-analytical-solutions/README.md) | [Start Chapter 14](14-sql-analytics-endpoint.md) | [Next: Part IV](../04-how-the-engine-works/README.md)
