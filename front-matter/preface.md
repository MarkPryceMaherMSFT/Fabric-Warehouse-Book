# Preface

[Book contents](../index.md) | [Previous: Foreword](foreword.md) | [Next: Acknowledgements](acknowledgements.md)

## Begin with an answer you can explain

A successful analytical solution is more than a query that returns quickly. Its answers must mean what their readers think they mean. Its data must be fresh enough for the decision, its access must be deliberate, and its behaviour must remain understandable when the workload grows or something fails.

Microsoft Fabric puts many of the tools for that work in one platform. Familiar SQL makes the first steps approachable, but familiarity can conceal important differences. A Warehouse is not a SQL Server instance with a different label. A Lakehouse SQL analytics endpoint is not another way to write the same tables. Shared OneLake storage does not remove ownership, security or freshness boundaries.

This book connects those distinctions into a continuous explanation: from the first small model to the engine that serves it, and from individual queries to the responsibilities of operating and migrating a complete service.

## Who this book is for

SQL developers can start with familiar language and discover the consequences of distributed execution and open storage. Data engineers can learn where Lakehouse processing ends and SQL serving begins. Database administrators and architects can connect their existing knowledge to a SaaS platform without assuming that SQL Server instance administration or Synapse dedicated-pool tuning transfers unchanged.

Basic familiarity with tables and SELECT statements is helpful, but the opening chapters do not assume previous Fabric experience. The engine chapters are intentionally more demanding. Read them after building the introductory examples: a query plan, a Delta log or a capacity chart is easier to understand when it explains something you have already observed.

## From first principles to production decisions

The seven parts form one learning journey. Part I introduces Fabric and OneLake before asking you to create an item. Part II builds analytical solutions with T-SQL, models, transformations, security and client access. Part IV starts with the Warehouse architecture and gives each of its six building blocks a dedicated chapter, alongside Polaris, metadata synchronization and a complete query walkthrough.

Part V applies that understanding to statistics and performance. Part VI broadens the view to monitoring, troubleshooting, consumption, capacity, workload management, acceleration, recovery and automation. Part VII brings those ideas together in migration planning, reconciliation and a production-oriented capstone.

GPU acceleration appears twice on purpose: first as an accessible introduction, then as an operational and economic decision. OneLake security has its own chapter because the route by which data is read matters as much as the SQL object a reader can see.

## One small example, many useful questions

A fictional retail model runs through the book. Three customers, four products and six sales rows make the early results small enough to check by hand. The Warehouse and Lakehouse hold independent implementations of that same model, so their responsibilities can be compared without suggesting that they replicate automatically.

The small example is a teaching device, not a demonstration of production scale. Later chapters explicitly require representative data, concurrency and observations before drawing performance or capacity conclusions. The aim is to learn which question to ask and which evidence can answer it.

The 24 original explanatory figures serve the same purpose. They make relationships visible without claiming to reveal an undocumented service topology. Twenty-six separately credited Microsoft documentation diagrams and screenshots connect that explanation to public product guidance, including the official Fabric platform diagram in Chapter 1. The [figure index](../appendices/F-diagram-index.md) distinguishes original editable drawings from unmodified source copies, and the [chapter review](../appendices/I-chapter-review.md) records coverage through Chapter 42.

## Read the evidence as carefully as the code

Fabric changes quickly. Documentation, announcements, research papers and public samples each contribute something useful, but they do not establish the same kind of claim. A research result is not a service guarantee, an announcement is not proof of availability in every tenant, and a repository is not a product-support contract.

The manuscript keeps these distinctions visible through dated feature notes, references and source registers. It favours a clear boundary over a convenient but unsupported answer. Use the current documentation for implementation decisions and the book to understand why those decisions belong together.

Start with the [reader guide](how-to-use-this-book.md), or open [Part I](../parts/01-getting-started/README.md) and follow the chapters in order.

---

[Previous: Foreword](foreword.md) | [Book contents](../index.md) | [Next: Acknowledgements](acknowledgements.md)
