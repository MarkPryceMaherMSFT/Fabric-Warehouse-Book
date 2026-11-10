# Part V - Statistics and performance

[Book contents](../../index.md) | [Cover](../../README.md)

**Chapters 26-28**

Connect engine knowledge to measured tuning decisions. Start with cardinality and statistics, read plans as evidence, and separate file layout from the different kinds of cache.

## Before you begin

Read Part IV and retain a known-correct query and dataset. The six-row teaching seed proves semantics, not speed; performance conclusions require a representative workload.

## Chapter index

| Chapter | Subject |
| --- | --- |
| [26. Statistics: Estimates, Maintenance, and Safe Inspection](26-statistics.md) | Cardinality estimates, managed refresh, and targeted maintenance. |
| [27. Query Plans and Evidence-Led Tuning](27-query-plans-and-tuning.md) | Evidence-led comparisons and bounded, human-reviewed AI suggestions. |
| [28. Physical Layout, Caching, and Maintenance](28-layout-caching-and-maintenance.md) | File organization, pruning, compaction, and cache behaviour. |

## By the end of this part

Form a tuning hypothesis, compare like-for-like observations, and choose a statistics, SQL or storage intervention without treating every slow query as a capacity problem.

---

[Previous: Part IV](../04-how-the-engine-works/README.md) | [Start Chapter 26](26-statistics.md) | [Next: Part VI](../06-operating-the-platform/README.md)
