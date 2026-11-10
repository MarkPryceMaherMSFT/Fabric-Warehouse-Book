"""Render the book's original diagrams from one scene to PNG, SVG and Excalidraw.

Run from the book root: python tools\\render_diagrams.py
Requires Pillow plus Python's standard library; rendering makes no network calls.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "diagrams"
W, H = 1700, 1200
COLORS = {
    "blue": ("#0078D4", "#CFE4FA"),
    "teal": ("#008575", "#D5F1ED"),
    "green": ("#107C10", "#DFF6DD"),
    "gray": ("#605E5C", "#F3F2F1"),
}
FONT_DIR = Path(r"C:\Windows\Fonts")
FONT_REG = FONT_DIR / "segoeui.ttf"
FONT_BOLD = FONT_DIR / "segoeuib.ttf"
if not FONT_REG.exists():
    FONT_REG = FONT_DIR / "arial.ttf"
    FONT_BOLD = FONT_DIR / "arialbd.ttf"


def font(size, bold=False):
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REG), size)


class Scene:
    def __init__(self, number, slug, title, subtitle, chapters, caption, caveat,
                 evidence_reviewed_on="2026-10-09"):
        self.id = f"{number:02d}-{slug}"
        self.title, self.chapters = title, chapters
        self.caption, self.caveat = caption, caveat
        self.evidence_reviewed_on = evidence_reviewed_on
        self.elements = []
        self.text(60, 45, title, 46, bold=True, width=1580)
        self.text(60, 116, subtitle, 28, width=1580)
        self.line([(60, 174), (1640, 174)], "blue", width=3)

    def add(self, kind, **kwargs):
        eid = f"{self.id}-{len(self.elements):03d}"
        element = {"id": eid, "kind": kind, **kwargs}
        self.elements.append(element)
        return eid

    def text(self, x, y, text, size=30, width=1500, align="left", bold=False,
             parent=None):
        lines = text.split("\n")
        f = font(size, bold)
        measured = max(f.getlength(line) for line in lines)
        if measured > width + 0.5:
            raise ValueError(f"{self.id}: text too wide ({measured:.0f}>{width}): {text}")
        height = size * 1.32 * len(lines)
        if x < 0 or y < 0 or x + width > W + 1 or y + height > H:
            raise ValueError(f"{self.id}: text outside canvas: {text}")
        return self.add("text", x=x, y=y, w=width, h=height, text=text,
                        size=size, align=align, bold=bold, parent=parent)

    def box(self, x, y, w, h, text, color="blue", size=30, future=False,
            bold=False):
        eid = self.add("rect", x=x, y=y, w=w, h=h, color=color,
                       fill=True, dashed=future, radius=16, container=False)
        if not text:
            return eid
        th = len(text.split("\n")) * size * 1.32
        if th > h - 24:
            raise ValueError(f"{self.id}: text too tall in box: {text}")
        self.text(x + 16, y + (h - th) / 2, text, size, w - 32,
                  "center", bold, parent=eid)
        return eid

    def container(self, x, y, w, h, title, color="gray", future=False):
        eid = self.add("rect", x=x, y=y, w=w, h=h, color=color,
                       fill=False, dashed=future, radius=18, container=True)
        self.text(x + 22, y + 17, title, 31, width=w - 44, bold=True)
        return eid

    def arrow(self, points, color="blue", dashed=False, width=4):
        return self.add("arrow", points=points, color=color,
                        dashed=dashed, stroke_width=width)

    def line(self, points, color="gray", dashed=False, width=2):
        return self.add("line", points=points, color=color,
                        dashed=dashed, stroke_width=width)

    def note(self, x, y, text, width=1500, size=27, bold=False):
        return self.text(x, y, text, size, width=width, bold=bold)

    def finish(self, takeaway):
        self.box(60, 1050, 1580, 82, takeaway, "gray", 28)
        self.box(63, 1157, 23, 23, "", "blue", 1)
        self.note(96, 1150, "SQL / control", 225, 24)
        self.box(329, 1157, 23, 23, "", "teal", 1)
        self.note(362, 1150, "Storage / flow", 230, 24)
        self.box(598, 1157, 23, 23, "", "green", 1)
        self.note(631, 1150, "Output / checks", 245, 24)
        self.line([(885, 1169), (946, 1169)], "gray", True, 3)
        self.note(958, 1150, "Announced - coming soon", 405, 24)
        self.note(1435, 1150, f"Figure {self.id[:2]} / {len(BUILDERS)}", 205, 24)
        return self


def platform():
    s = Scene(1, "platform-journey", "From operational records to decisions",
              "A sales question crosses several responsibilities, not one magic database.", [1],
              "Conceptual analytics journey: ingest operational data, shape a governed model, "
              "and serve decisions while OneLake storage remains separate from compute.",
              "Conceptual responsibility map, not a measured deployment or fixed topology.")
    for x, name, body, color in [
        (70, "1  Land", "Operational records\nFiles and changes", "blue"),
        (480, "2  Shape", "Warehouse SQL\nor Lakehouse Spark", "teal"),
        (890, "3  Serve", "SQL + semantic model\nBusiness measures", "blue"),
        (1300, "4  Decide", "Reports and clients\nRevenue by country", "green"),
    ]:
        s.box(x, 245, 330, 80, name, color, 32, bold=True)
        s.box(x, 360, 330, 145, body, color, 28)
    for x in [405, 815, 1225]:
        s.arrow([(x, 433), (x + 68, 433)], "teal")
    s.container(70, 585, 1560, 195, "OneLake: shared storage foundation", "teal")
    s.box(110, 665, 480, 76, "Managed tables + open data", "teal", 30)
    s.box(650, 665, 400, 76, "Governed access paths", "teal", 30)
    s.box(1110, 665, 470, 76, "Not an execution engine", "gray", 30)
    s.arrow([(645, 505), (645, 577)], "teal")
    s.arrow([(1055, 585), (1055, 513)], "teal")
    s.box(70, 835, 735, 155, "MPP / Polaris\nSplit eligible work into tasks;\ncoordinate and combine results.", "blue", 29)
    s.box(865, 835, 765, 155, "Business contract\nUse the right grain and permissions;\nverify the answer before tuning.", "green", 29)
    return s.finish("One platform does not erase write ownership, security boundaries or freshness checks.")


def concepts():
    s = Scene(2, "fabric-concepts", "Fabric's organizing layers",
              "Tenant, capacity, workspace and item answer different administrative questions.", [2],
              "Conceptual containment and assignment map. A capacity supplies compute to an assigned "
              "workspace; OneLake is a storage foundation, not a second capacity.",
              "One illustrative assignment; not a physical infrastructure map.")
    s.container(75, 215, 1550, 810, "Tenant  |  organizational boundary", "blue")
    s.box(125, 315, 390, 170, "Capacity\nCompute resources\nand billing boundary", "blue", 30)
    s.container(675, 310, 890, 465, "Workspace  |  collaboration + access", "teal")
    s.arrow([(523, 392), (665, 392)], "blue")
    s.note(537, 425, "assigned\nto", 122, 27)
    s.box(715, 415, 355, 135, "Warehouse item\nSQL-owned writes", "blue", 30)
    s.box(1140, 415, 355, 135, "Lakehouse item\nSpark / data writers", "teal", 30)
    s.box(715, 600, 355, 115, "Notebook item\nCompute instructions", "blue", 29)
    s.box(1140, 600, 355, 115, "Semantic model\nBusiness measures", "green", 29)
    s.box(125, 605, 390, 170, "Item\nA managed artifact:\nnot always a table", "gray", 30)
    s.container(125, 835, 1370, 145, "OneLake  |  storage, not compute", "teal")
    s.note(155, 900, "Items organize data and metadata; engines execute work against permitted data.", 1290, 29)
    s.arrow([(892, 775), (892, 827)], "teal")
    s.arrow([(1317, 775), (1317, 827)], "teal")
    return s.finish("Ask separately: who owns this item, which workspace contains it, and what compute runs it?")


def onelake_paths():
    s = Scene(3, "onelake-paths", "OneLake paths connect readers to data",
              "A shortcut points to a source; compute and authorization still live on the reading route.", [2],
              "Conceptual direct and shortcut read paths. An external shortcut references existing "
              "data rather than creating an independent authoritative copy.",
              "Reader, shortcut type and source determine supported features and permissions.")
    s.container(70, 220, 720, 525, "Storage and references", "teal")
    s.box(110, 330, 300, 140, "OneLake\nManaged table", "teal", 31)
    s.box(110, 545, 300, 140, "External source\nExisting data", "teal", 30)
    s.box(475, 545, 265, 140, "Shortcut\nReference", "teal", 30)
    s.arrow([(475, 615), (420, 615)], "teal")
    s.note(470, 492, "resolves to source", 275, 26)
    s.container(955, 220, 675, 525, "Compute reads through a supported route", "blue")
    s.box(1000, 330, 580, 140, "SQL / Spark / other reader\nCompatibility + identity matter", "blue", 30)
    s.box(1000, 545, 580, 140, "Result\nRows computed when requested", "green", 30)
    s.arrow([(420, 400), (990, 400)], "teal")
    s.note(815, 341, "read data", 150, 26)
    s.arrow([(740, 614), (860, 614), (860, 451), (990, 451)], "teal")
    s.arrow([(1290, 470), (1290, 535)], "blue")
    s.box(70, 825, 745, 160, "Path is not permission\nSource access and consumer access\nmust both be designed.", "gray", 30)
    s.box(875, 825, 755, 160, "Reference is not ownership\nA shortcut does not grant permission\nto rewrite Warehouse-managed files.", "gray", 29)
    return s.finish("Separate three questions: where are the bytes, who may read them, and which engine computes?")


def ownership():
    s = Scene(4, "artifact-ownership", "Three artifacts, three write owners",
              "Warehouse writes differ from Lakehouse and mirrored SQL analytics endpoint reads.", [14],
              "Conceptual write-ownership lanes for Warehouse, Lakehouse and mirrored database. "
              "The mirrored upstream system remains authoritative for source writes.",
              "Mirroring is source-specific. SQL endpoint reads do not transfer ownership of data writes.")
    headers = [(75, 330, "Authoritative writer"), (450, 600, "Fabric item + data"), (1110, 520, "SQL surface")]
    for x, w, title in headers:
        s.note(x, 221, title, w, 30, True)
    rows = [
        (290, "Warehouse SQL\nInsert / update / delete", "Warehouse\nManaged OneLake tables", "Warehouse SQL\nReads + managed writes", "blue"),
        (535, "Spark + ingestion\nLakehouse owns writes", "Lakehouse\nDelta tables in OneLake", "SQL analytics endpoint\nReads Lakehouse tables", "teal"),
        (780, "Upstream database\nSource owns writes", "Mirrored database\nReplicated copy in OneLake", "SQL analytics endpoint\nReads mirrored copy", "green"),
    ]
    for y, a, b, c, color in rows:
        s.box(75, y, 330, 165, a, color, 27)
        s.box(490, y, 535, 165, b, color, 30)
        s.box(1110, y, 520, 165, c, color, 29)
        s.arrow([(410, y + 82), (480, y + 82)], color)
        s.arrow([(1030, y + 82), (1100, y + 82)], color)
    s.note(75, 984, "Independent lanes: no Warehouse-to-Lakehouse replication is implied.", 1550, 28)
    return s.finish("Shared storage formats do not make all artifacts interchangeable or all engines valid writers.")


def decision():
    s = Scene(5, "lakehouse-warehouse-decision", "Choose by the work and its owner",
              "Both paths can serve analytics. Start with the supported write workflow, not a format slogan.", [14],
              "Conceptual decision tree: SQL-managed relational writes favor Warehouse; Spark and "
              "file-centered engineering favor Lakehouse. Mixed solutions keep ownership explicit.",
              "A design aid, not an exhaustive feature matrix or a claim that one path excludes the other.")
    s.box(500, 220, 700, 100, "What should own the transformation writes?", "gray", 31, bold=True)
    s.arrow([(715, 320), (715, 370), (435, 370), (435, 420)], "blue")
    s.arrow([(985, 320), (985, 370), (1265, 370), (1265, 420)], "teal")
    s.container(75, 420, 720, 395, "SQL-led relational workflow", "blue")
    s.container(905, 420, 720, 395, "Spark / file-led engineering workflow", "teal")
    s.box(115, 510, 640, 110, "Warehouse\nT-SQL DML + transactions", "blue", 31)
    s.box(945, 510, 640, 110, "Lakehouse\nSpark + supported Delta writers", "teal", 31)
    s.box(115, 665, 640, 105, "Example: controlled sales mart loads", "green", 28)
    s.box(945, 665, 640, 105, "Example: notebook shaping raw files", "green", 28)
    s.arrow([(435, 815), (435, 860), (675, 860), (675, 900)], "blue")
    s.arrow([(1265, 815), (1265, 860), (1025, 860), (1025, 900)], "teal")
    s.box(300, 900, 1100, 105, "Both: SQL reads, BI consumers and governance\nMixed architecture: define the handoff and verify freshness.", "gray", 29)
    return s.finish("The Lakehouse SQL endpoint does not turn a Spark-owned table into a Warehouse-write table.")


def gpu():
    s = Scene(6, "cpu-gpu-execution", "GPU acceleration is a partial execution choice",
              "Public preview announced September 2026; verify workspace, region and eligibility.", [6, 34],
              "Conceptual CPU/GPU split: an eligible portion of execution may use GPU acceleration "
              "while other work stays on CPU and results are combined.",
              "Illustrative operator split only; not an observed plan, benchmark or universal speedup. "
              "Accelerated-workspace metering includes ineligible queries; toggling cancels requests.")
    s.box(75, 265, 330, 125, "SQL request\nBusiness question", "blue", 30)
    s.box(530, 265, 460, 125, "Plan + eligibility\nChoose supported work", "blue", 31)
    s.arrow([(413, 328), (520, 328)], "blue")
    s.container(75, 475, 720, 270, "CPU execution", "blue")
    s.box(115, 565, 640, 120, "General / noneligible work\nCoordination and remaining operators", "blue", 29)
    s.container(905, 475, 720, 270, "GPU execution  |  preview", "teal")
    s.box(945, 565, 640, 120, "Eligible accelerated work\nOnly the supported part of a query", "teal", 30)
    s.arrow([(650, 390), (650, 430), (435, 430), (435, 466)], "blue")
    s.arrow([(850, 390), (850, 430), (1265, 430), (1265, 466)], "teal")
    s.box(570, 845, 560, 110, "Combine and return results\nValidate correctness + total cost", "green", 30)
    s.arrow([(435, 745), (435, 900), (560, 900)], "blue")
    s.arrow([(1265, 745), (1265, 900), (1140, 900)], "teal")
    return s.finish("Do not infer GPU use from a toggle alone, or assume an ineligible query is outside the meter.")


def security():
    s = Scene(7, "security-routes", "Authorization depends on the access route",
              "OneLake security is authorization, not encryption; item Read alone does not grant data read.", [12, 16],
              "Conceptual security routes. Delegated endpoint mode uses SQL table authorization; "
              "user-identity mode uses OneLake roles for underlying table data. Direct storage "
              "access is a separate route and does not automatically inherit SQL policy.",
              "SQL analytics endpoint mode diagram, not a universal Warehouse security matrix. "
              "OneLake DDM is not available in user-identity mode; elevated roles require separate review.")
    s.container(65, 215, 500, 620, "SQL endpoint: delegated mode", "blue")
    s.container(600, 215, 500, 620, "SQL endpoint: user identity", "teal")
    s.container(1135, 215, 500, 620, "Direct storage route", "green")
    for x, color in [(105, "blue"), (640, "teal"), (1175, "green")]:
        s.box(x, 310, 420, 95, "User / application", color, 30)
    s.box(105, 465, 420, 145, "SQL permissions\nTable RLS / CLS / DDM", "blue", 29)
    s.box(640, 465, 420, 145, "OneLake roles\nTable RLS / CLS", "teal", 29)
    s.box(1175, 465, 420, 145, "OneLake / source access\nApplicable storage policies", "green", 27)
    s.box(105, 675, 420, 105, "Storage identity:\nitem owner / associated identity", "blue", 26)
    s.box(640, 675, 420, 105, "Storage identity:\ncalling user", "teal", 29)
    s.box(1175, 675, 420, 105, "Do not assume\nSQL policies follow this route", "green", 28)
    for x, color in [(315, "blue"), (850, "teal"), (1385, "green")]:
        s.arrow([(x, 410), (x, 455)], color)
        s.arrow([(x, 615), (x, 665)], color)
    s.box(65, 890, 1035, 118, "Both endpoint modes require initial item access.\nSQL permissions still govern views, procedures and functions.", "gray", 29)
    s.box(1135, 890, 500, 118, "CLS controls columns.\nEncryption protects stored bytes.", "gray", 28)
    return s.finish("Changing endpoint security mode is a workspace-impacting operation, not a harmless reader exercise.")


def workspace_identity():
    s = Scene(8, "workspace-identity-ingest", "COPY INTO uses two authorization contexts",
              "Workspace Identity authorizes the source read; it does not replace the caller's target SQL rights.", [9],
              "Conceptual COPY INTO authorization: the caller retains target INSERT responsibility, "
              "while the Fabric-managed workspace identity reads the authorized source.",
              "Workspace Identity COPY INTO is GA as of August 2026. Source-specific role, ACL, "
              "network and workspace-membership requirements still apply.")
    s.box(70, 245, 470, 145, "Caller\nSQL context + target INSERT\nRequired workspace membership", "blue", 29)
    s.box(695, 245, 590, 145, "COPY INTO target table\nCredential: Workspace Identity", "blue", 30)
    s.arrow([(550, 318), (685, 318)], "blue")
    s.note(565, 263, "submits", 120, 26)
    s.container(70, 490, 690, 400, "Source authorization", "teal")
    s.box(110, 580, 610, 115, "Workspace Identity\nFabric-managed Entra service principal", "teal", 29)
    s.box(110, 755, 610, 95, "Authorized source files", "teal", 31)
    s.arrow([(415, 695), (415, 745)], "teal")
    s.container(930, 490, 700, 400, "Target authorization", "blue")
    s.box(970, 580, 620, 115, "Warehouse table\nCaller must have INSERT permission", "blue", 29)
    s.box(970, 755, 620, 95, "Committed rows after successful load", "green", 29)
    s.arrow([(1280, 695), (1280, 745)], "green")
    s.arrow([(870, 390), (870, 440), (415, 440), (415, 480)], "teal")
    s.arrow([(1110, 390), (1110, 450), (1280, 450), (1280, 480)], "blue")
    s.arrow([(760, 805), (920, 805)], "teal")
    s.note(779, 746, "file data", 135, 26)
    s.note(70, 952, "One identity reads the source. A different authorization context permits the target write.", 1540, 30)
    return s.finish("Grant source access to the workspace identity and target rights to the caller; troubleshoot them separately.")


def query_lifecycle():
    s = Scene(9, "query-lifecycle", "QO chooses; DQP coordinates; QE executes",
              "A responsibility map from SQL text to distributed results, not a fixed private service topology.", [18, 25],
              "Conceptual query lifecycle distinguishing the query optimizer (QO), Distributed Query "
              "Processor (DQP) and local query execution engines (QE).",
              "Task counts, placement, retries and scheduler algorithms are illustrative, not product guarantees.")
    s.box(70, 250, 335, 155, "Bind SQL\nObjects, types,\nsecurity context", "blue", 30)
    s.box(505, 250, 465, 155, "QO: query optimizer\nEstimate + cost alternatives\nChoose physical strategy", "blue", 30)
    s.box(1070, 250, 560, 155, "DQP: distributed coordination\nTask dependencies + resources\nSchedule eligible work", "teal", 29)
    s.arrow([(415, 327), (495, 327)], "blue")
    s.arrow([(980, 327), (1060, 327)], "blue")
    s.container(70, 520, 1560, 295, "QE: local SQL execution engines", "blue")
    for x, txt in [(110, "Scan + filter"), (615, "Join + aggregate"), (1120, "Combine work")]:
        s.box(x, 620, 460, 125, f"Assigned operators\n{txt}", "blue", 31)
    s.arrow([(1350, 405), (1350, 510)], "teal")
    s.note(100, 455, "Tasks may run concurrently when dependencies and resources permit.", 1150, 27)
    s.box(70, 895, 700, 105, "OneLake data + managed caches\nStorage is not the scheduler", "teal", 30)
    s.box(990, 895, 640, 105, "Results returned to the client\nCompletion is coordinated", "green", 30)
    s.arrow([(420, 895), (420, 825)], "teal")
    s.arrow([(1310, 815), (1310, 885)], "green")
    return s.finish("A poor estimate, a scheduling wait and slow local execution are different hypotheses to investigate.")


def storage():
    s = Scene(10, "storage-publication", "Commit and publication are different boundaries",
              "Warehouse publishes outward to Delta readers; Lakehouse metadata sync exposes changes inward to SQL.", [23],
              "Conceptual visibility paths separating Warehouse transaction commit and asynchronous "
              "Delta publication from Lakehouse SQL endpoint metadata synchronization.",
              "Not a timing diagram or latency SLA. External readers must verify their required data condition.")
    s.container(70, 225, 1560, 400, "Warehouse write and external read path", "blue")
    for x, w, txt, color in [
        (110, 300, "SQL write\nManaged changes", "blue"),
        (490, 300, "SQL commit\nSQL-visible state", "blue"),
        (875, 325, "Background\nDelta publication", "teal"),
        (1280, 310, "External reader\nRead-only access", "green"),
    ]:
        s.box(x, 330, w, 145, txt, color, 29)
    for a, b in [(420, 480), (800, 865), (1210, 1270)]:
        s.arrow([(a, 402), (b, 402)], "teal")
    s.note(120, 535, "SQL commit does not wait for every external consumer to observe the published snapshot.", 1450, 29)
    s.container(70, 710, 1560, 290, "Lakehouse-to-SQL path: a different mechanism", "teal")
    s.box(110, 810, 400, 130, "Spark / Delta commit\nLakehouse-owned write", "teal", 30)
    s.box(650, 810, 400, 130, "Metadata sync\nDiscovery + freshness", "blue", 30)
    s.box(1190, 810, 400, 130, "SQL analytics endpoint\nRead Lakehouse tables", "green", 29)
    s.arrow([(520, 875), (640, 875)], "teal")
    s.arrow([(1060, 875), (1180, 875)], "blue")
    return s.finish("Validate the consumer's batch marker; files existing, SQL committing and a reader catching up are not synonyms.")


def metadata_sync():
    s = Scene(11, "metadata-sync-generations", "Metadata sync separates discovery from freshness",
              "\"v1\" and \"v2\" are book shorthand for legacy and new sync, not REST API versions.", [15],
              "Conceptual comparison of legacy background synchronization and new preview metadata "
              "sync, where schema discovery and existing-table data freshness are decoupled.",
              "New sync is preview and opt-in for newly created endpoints; existing endpoints are "
              "not automatically upgraded. Query refresh is not synchronous schema discovery.")
    s.container(70, 220, 720, 790, "Legacy sync  |  book shorthand: v1", "blue")
    s.container(910, 220, 720, 790, "New sync  |  preview  |  shorthand: v2", "teal")
    s.box(120, 320, 620, 115, "Lakehouse Delta changes", "teal", 31)
    s.box(120, 535, 620, 145, "Background discovery + sync\nAsynchronous handoff", "blue", 30)
    s.box(120, 790, 620, 120, "SQL-serving representation\nVerify the required data condition", "green", 29)
    s.arrow([(430, 435), (430, 525)], "teal")
    s.arrow([(430, 680), (430, 780)], "blue")
    s.box(960, 320, 620, 115, "Lakehouse Delta changes", "teal", 31)
    s.box(960, 535, 280, 145, "Table / schema\ndiscovery", "blue", 28)
    s.box(1300, 535, 280, 145, "Existing-table\ndata freshness", "teal", 28)
    s.arrow([(1100, 435), (1100, 525)], "blue")
    s.arrow([(1440, 435), (1440, 525)], "teal")
    s.note(960, 710, "Catalog refresh", 280, 27)
    s.note(1300, 710, "Background +\non-read refresh", 280, 27)
    s.box(960, 835, 620, 100, "SQL read of a known table", "green", 30)
    s.arrow([(1100, 747), (1100, 825)], "blue")
    s.arrow([(1440, 786), (1440, 825)], "teal")
    return s.finish("Missing table, missing column, stale rows and poor estimates require different checks.")


def statistics():
    s = Scene(12, "statistics-feedback", "Statistics inform estimates, not business truth",
              "Compare predicted rows with observed work before choosing a targeted maintenance action.", [26],
              "Conceptual diagnostic loop linking distributions, statistics, cardinality estimates, "
              "plan decisions and observed execution evidence.",
              "The return loop is an operator's investigation, not a promised automatic query-feedback feature.")
    s.box(75, 250, 390, 160, "Data distribution\nSkew, correlation,\nnew or changed rows", "teal", 30)
    s.box(650, 250, 390, 160, "Statistics\nCompact summaries\nof column values", "blue", 30)
    s.box(1225, 250, 400, 160, "QO estimates\nExpected rows\nat plan operators", "blue", 30)
    s.arrow([(475, 330), (640, 330)], "teal")
    s.arrow([(1050, 330), (1215, 330)], "blue")
    s.box(1225, 620, 400, 175, "Plan choices\nJoin strategy,\nmovement + memory", "blue", 30)
    s.box(650, 620, 390, 175, "Execution evidence\nActual row volumes\nand resource pressure", "green", 29)
    s.box(75, 620, 390, 175, "Targeted response\nInspect statistics,\nSQL and data shape", "green", 29)
    s.arrow([(1425, 410), (1425, 610)], "blue")
    s.arrow([(1215, 707), (1050, 707)], "blue")
    s.arrow([(640, 707), (475, 707)], "green")
    s.arrow([(270, 620), (270, 515), (845, 515), (845, 420)], "green")
    s.note(310, 550, "Human diagnostic loop: refresh only when evidence justifies it", 880, 27)
    s.box(75, 885, 1550, 112, "A good histogram cannot discover a missing Lakehouse table,\nrepair duplicate dimension keys or guarantee a globally optimal plan.", "gray", 30)
    return s.finish("Validate semantics first; statistics maintenance improves information available to the optimizer.")


def monitoring():
    s = Scene(13, "monitoring-evidence", "Match the evidence to the question",
              "Live activity, completed-query history, capacity consumption and audit records are different lenses.", [29],
              "Conceptual evidence map. WarehouseExecutions.OperationId correlates with Query Insights "
              "distributed_statement_id, not Capacity Metrics Operation ID.",
              "WarehouseExecutions and the Data Warehouse Monitor have preview prerequisites. "
              "Agentic monitoring is announced, coming soon; available operations diagnostics are bounded, not autofix.")
    rows = [
        (230, "What is running now?", "DMVs + Data Warehouse Monitor", "Live activity / waits\nMonitor: preview + admin scope", "blue"),
        (405, "What finished?", "Query Insights +\nWarehouseExecutions (preview)", "Completed query evidence\nCoverage + ingestion lag matter", "teal"),
        (580, "What consumed capacity?", "Capacity Metrics", "CU consumption + pressure\nDo not equate operation IDs", "blue"),
        (755, "Which SQL event was recorded?", "SQL audit", "Enabled groups + capture filter\nExcluded events are lost", "green"),
    ]
    for y, q, lens, caveat, c in rows:
        s.box(65, y, 460, 125, q, c, 28)
        s.box(610, y, 500, 125, lens, c, 27)
        s.box(1195, y, 440, 125, caveat, "gray", 26)
        s.arrow([(535, y + 62), (600, y + 62)], c)
        s.arrow([(1120, y + 62), (1185, y + 62)], c)
    s.box(65, 925, 990, 105,
          "WarehouseExecutions.OperationId\n= Query Insights distributed_statement_id", "teal", 28)
    s.box(1115, 925, 520, 95, "Agentic monitoring\nAnnounced - coming soon", "gray", 26, future=True)
    return s.finish("Preserve UTC timestamps, item context and the correct identifiers before proposing a fix.")


def capacity():
    s = Scene(14, "capacity-models", "Do not confuse three different control points",
              "Existing capacity throttling, future compute ceilings and future spending limits have different effects.", [31, 32],
              "Conceptual comparison of the existing capacity model and announced on-demand Warehouse "
              "model. A compute ceiling queues or slows work; a separate rolling spending limit "
              "can pause new operations while in-flight work finishes.",
              "On-demand Warehouse billing is public preview coming soon at the 9 October 2026 "
              "evidence cutoff. Queue discipline, timeouts and rollout details are not published.")
    s.container(65, 220, 545, 795, "Existing capacity model", "blue")
    s.box(105, 330, 465, 155, "Shared capacity\nConsumption + smoothing\nCapacity pressure matters", "blue", 29)
    s.arrow([(337, 485), (337, 580)], "blue")
    s.box(105, 590, 465, 155, "Capacity throttling\nDelays / rejections under\napplicable capacity rules", "blue", 29)
    s.note(105, 825, "Not the same as the announced\non-demand control model.", 460, 28)
    s.container(675, 220, 960, 795, "On-demand Warehouse  |  Announced - coming soon", "teal", future=True)
    s.box(715, 330, 880, 115, "Planned consumption billing: CU-hours without smoothing\nStorage remains separate", "teal", 29, future=True)
    s.box(715, 550, 410, 160, "Workspace compute ceiling\nWork queues / slows\nat the compute limit", "teal", 28, future=True)
    s.box(1185, 550, 410, 160, "Rolling 24-hour spend limit\nNew operations may pause;\nin-flight work finishes", "green", 27, future=True)
    s.arrow([(940, 445), (940, 540)], "teal", True)
    s.arrow([(1390, 445), (1390, 540)], "green", True)
    s.box(715, 805, 880, 145, "SQL pools (current) classify and isolate workload shares.\nThey are not authorization boundaries or spending caps.\nDo not read \"queues\" as unlimited compute or no quotas.", "gray", 28)
    return s.finish("Treat resource ceilings, budget safeguards and existing capacity throttling as separate operational policies.")


def cache():
    s = Scene(15, "cache-lifecycle", "Cache warmth changes work, not query semantics",
              "Managed data caching exists today. Configurable cooldown is a forthcoming capability.", [28],
              "Conceptual cache lifecycle: a read may fetch data from OneLake or reuse managed "
              "disk and memory caches. Announced cooldown controls are not shown as an existing UI.",
              "Cache cooldown public preview is coming soon. Exact timers, defaults, scope, affected "
              "layers and billing are unpublished. Result-set caching is a separate feature.")
    s.container(70, 220, 1560, 420, "Current managed data caching", "blue")
    s.box(110, 330, 365, 160, "Read request\nNeed table data", "blue", 31)
    s.box(670, 330, 390, 160, "Warm data cache\nMemory / local disk", "teal", 31)
    s.box(1220, 330, 370, 160, "OneLake\nRemote table data", "teal", 31)
    s.arrow([(485, 365), (660, 365)], "blue")
    s.note(485, 305, "cache lookup", 180, 26)
    s.arrow([(1070, 410), (1210, 410)], "teal")
    s.note(1090, 352, "on miss", 125, 26)
    s.arrow([(1405, 500), (1405, 560), (865, 560), (865, 500)], "teal")
    s.note(1100, 569, "fetched data can warm caches", 465, 26)
    s.container(70, 725, 970, 280, "Cooldown controls  |  Announced - coming soon", "teal", future=True)
    s.box(110, 820, 890, 115, "Intent: balance warm performance and cache lifecycle cost\nNo documented timer, ALTER setting or configuration UI here", "teal", 28, future=True)
    s.box(1120, 760, 510, 205, "Separate feature\nResult-set cache reuses\nan eligible prior answer;\na data cache reuses data.", "gray", 29)
    return s.finish("A faster second run is evidence to investigate, not proof of a changed plan or complete answer reuse.")


def release():
    s = Scene(16, "release-pipeline", "A deployment is a reviewed change, not just a file push",
              "CI/CD 2.0 DacFx and deployment scripts are preview; check the project's upgrade prerequisites.", [36],
              "Conceptual release pipeline with schema comparison, a reviewed deployment artifact, "
              "one designated pre-deployment script, model deployment, one post-deployment "
              "script and validation.",
              "Scripts run every deployment, must be idempotent and are not model-validated at build. "
              "Failures halt deployment. Existing Git projects require the documented upgrade.")
    s.box(75, 235, 380, 140, "Source-controlled model\nSQL project / Git", "blue", 31)
    s.box(655, 235, 390, 140, "Schema compare\nReview / exclude / script", "blue", 30)
    s.box(1245, 235, 380, 140, "Approved artifact\nDACPAC / deployment", "green", 29)
    s.arrow([(465, 305), (645, 305)], "blue")
    s.arrow([(1055, 305), (1235, 305)], "blue")
    s.container(75, 505, 1550, 320, "Target deployment  |  preview integration", "teal")
    s.box(115, 610, 360, 140, "1  Pre-deploy script\nIdempotent preparation", "teal", 29)
    s.box(670, 610, 360, 140, "2  Model deployment\nIncremental changes", "blue", 29)
    s.box(1225, 610, 360, 140, "3  Post-deploy script\nIdempotent follow-up", "teal", 29)
    s.arrow([(485, 680), (660, 680)], "blue")
    s.arrow([(1040, 680), (1215, 680)], "blue")
    s.arrow([(1435, 375), (1435, 443), (295, 443), (295, 495)], "green")
    s.box(75, 900, 700, 100, "Failure: stop and inspect the evidence", "gray", 30)
    s.box(965, 900, 660, 100, "Validate schema + data + permissions", "green", 30)
    s.arrow([(1405, 825), (1405, 890)], "green")
    return s.finish("Schema Compare being GA does not make the Fabric deployment integration GA or eliminate review.")


def migration():
    s = Scene(17, "migration-flow", "Migrate schema and data as separate workstreams",
              "Translation is a starting point; reconciliation and a reversible cutover prove the migration.", [37, 40, 41, 42],
              "Conceptual migration plan with parallel schema/logic and data movement workstreams "
              "converging on correctness validation and an approved cutover.",
              "Assistant and connector capabilities vary. Watermarks do not propagate deletes; "
              "CDC requires a supported CDC-enabled source. No translation equivalence is promised.")
    s.box(535, 215, 630, 105, "Assess source + approve scope\nDependencies, access and rollback plan", "blue", 30)
    s.container(70, 415, 720, 365, "Schema and SQL logic", "blue")
    s.container(910, 415, 720, 365, "Data movement", "teal")
    s.box(110, 510, 640, 100, "Translate definitions → remediate", "blue", 30)
    s.box(110, 655, 640, 90, "Review unsupported behavior + orchestration", "blue", 27)
    s.box(950, 510, 640, 100, "Initial full load → incremental catch-up", "teal", 29)
    s.box(950, 655, 640, 90, "Watermark ≠ deletes; CDC is source-specific", "teal", 27)
    s.arrow([(700, 320), (700, 370), (430, 370), (430, 405)], "blue")
    s.arrow([(1000, 320), (1000, 370), (1270, 370), (1270, 405)], "teal")
    s.box(70, 900, 460, 105, "Reconcile\nRows, totals, edge cases", "green", 30)
    s.box(620, 900, 460, 105, "Controlled cutover\nFreeze / catch up / switch", "green", 29)
    s.box(1170, 900, 460, 105, "Rollback readiness\nKeep a tested route back", "gray", 29)
    s.arrow([(430, 780), (430, 890)], "blue")
    s.arrow([(1270, 780), (1270, 835), (300, 835), (300, 890)], "teal")
    s.arrow([(540, 952), (610, 952)], "green")
    s.arrow([(1090, 952), (1160, 952)], "green")
    return s.finish("Do not equate successful translation, successful copying and a business-correct destination.")


def iq():
    s = Scene(18, "fabric-iq-context", "Business context does not replace the query engine",
              "Ontology bindings, current IQ MCP access and future Warehouse integration are distinct contracts.", [13],
              "Conceptual Fabric IQ map. Preview ontology binds business entities to sources; it "
              "is not a new storage or query engine. Current IQ MCP supports read-only semantic-model "
              "and report discovery plus DAX; Warehouse-specific IQ integration is future.",
              "Optional graph materialization is not a universal execution path. Current IQ MCP "
              "does not establish ontology or data-agent support; source execution remains source-specific.")
    s.container(70, 220, 745, 795, "Ontology  |  preview business context", "teal")
    s.box(110, 325, 665, 145, "Customer → Sale → Product\nEntities, properties, relationships\nDefinitions + bindings", "teal", 30)
    s.box(110, 610, 300, 145, "Warehouse source\nSupported binding\nSQL execution", "blue", 28)
    s.box(475, 610, 300, 145, "Other bound source\nSource-specific\nexecution", "blue", 28)
    s.arrow([(265, 470), (265, 600)], "teal")
    s.arrow([(625, 470), (625, 600)], "teal")
    s.note(305, 518, "bindings", 275, 28)
    s.box(110, 855, 665, 105, "Not a query engine or a new data lake", "gray", 30)
    s.container(905, 220, 725, 485, "IQ MCP  |  current documented scope", "blue")
    s.box(945, 325, 645, 120, "Authorized client\nDelegated user identity", "blue", 30)
    s.box(945, 525, 645, 120, "Power BI semantic models + reports\nRead-only discovery and DAX", "green", 29)
    s.arrow([(1267, 445), (1267, 515)], "blue")
    s.container(905, 780, 725, 235, "Warehouse-specific IQ integration", "teal", future=True)
    s.box(945, 860, 645, 110, "Announced - coming soon\nNot a shipped MCP-to-Warehouse contract", "teal", 27, future=True)
    return s.finish("Business meaning can guide a request; permissions, execution and freshness still belong to the actual data route.")


def clone():
    s = Scene(19, "clone-scopes", "Table clone and whole-Warehouse clone differ in scope",
              "A current table-level capability must not be used as proof that the announced Warehouse clone exists.", [35],
              "Conceptual clone-scope comparison. Current CREATE TABLE AS CLONE OF targets a "
              "table; announced whole-Warehouse cloning is a separate forthcoming capability.",
              "Warehouse-level clone public preview is coming soon. No Warehouse syntax, security "
              "inheritance or cross-workspace behavior is implied.")
    s.container(70, 220, 725, 800, "Current: table-level clone", "blue")
    s.box(110, 325, 645, 120, "Warehouse contains multiple tables", "blue", 30)
    s.box(110, 515, 285, 130, "FactSales\nSelected table", "teal", 30)
    s.box(470, 515, 285, 130, "FactSales_Copy\nTable clone", "green", 28)
    s.arrow([(403, 580), (460, 580)], "teal")
    s.box(110, 755, 645, 140, "CREATE TABLE ... AS CLONE OF ...\nTable scope, subject to documented limits", "blue", 27)
    s.note(110, 935, "Other tables are not cloned by this statement.", 650, 27)
    s.container(905, 220, 725, 800, "Whole Warehouse  |  future scope", "teal", future=True)
    s.box(945, 325, 645, 120, "Announced - coming soon\nWarehouse-level clone public preview", "teal", 28, future=True)
    s.container(945, 515, 290, 180, "Source", "teal", future=True)
    s.container(1300, 515, 290, 180, "Clone", "green", future=True)
    s.box(965, 595, 250, 65, "Warehouse", "teal", 27, future=True)
    s.box(1320, 595, 250, 65, "Warehouse", "green", 27, future=True)
    s.arrow([(1243, 625), (1290, 625)], "teal", True)
    s.box(945, 790, 645, 165, "Unknown until documented\nExact syntax, inheritance and\ncross-workspace contracts", "gray", 29, future=True)
    return s.finish("Choose recovery and isolation designs using the scope that is documented and available in your environment.")


def logical_sql():
    s = Scene(20, "sql-logical-processing", "SQL's logical filter order",
              "Reason about which rows a clause sees. This is not the physical execution order chosen by QO.", [7],
              "Conceptual logical SQL evaluation order: sources and joins, WHERE, grouping and HAVING, "
              "window computation, QUALIFY, and final ORDER BY. QUALIFY filters window results.",
              "Simplified reasoning model, not a complete clause grammar or physical plan. New analytical "
              "syntax is preview for Fabric Warehouse and SQL analytics endpoints at the evidence cutoff.")
    nodes = [
        (70, 230, "1  FROM + JOIN", "Build the input relation", "blue"),
        (650, 230, "2  WHERE", "Filter individual input rows", "blue"),
        (1230, 230, "3  GROUP BY + HAVING", "Aggregate, then filter groups", "teal"),
        (1230, 625, "4  WINDOW", "Compute window values", "teal"),
        (650, 625, "5  QUALIFY", "Filter using window results", "green"),
        (70, 625, "6  ORDER BY", "Sort the surviving result", "green"),
    ]
    for x, y, title, body, c in nodes:
        s.box(x, y, 400, 100, title, c, 29, bold=True)
        s.box(x, y + 130, 400, 115, body, c, 27)
    s.arrow([(480, 410), (640, 410)], "blue")
    s.arrow([(1060, 410), (1220, 410)], "teal")
    s.arrow([(1430, 475), (1430, 615)], "teal")
    s.arrow([(1220, 810), (1060, 810)], "teal")
    s.arrow([(640, 810), (480, 810)], "green")
    s.box(70, 930, 1560, 88, "Latest sale per customer: ROW_NUMBER by DateKey DESC, SalesKey DESC → QUALIFY rank = 1", "gray", 28)
    return s.finish("WHERE cannot perform QUALIFY's job: the window value does not exist yet in this logical reasoning order.")


SEED = [
    (1001, 20260101, 1, 10, 2, 25),
    (1002, 20260101, 2, 20, 1, 80),
    (1003, 20260102, 1, 30, 3, 10),
    (1004, 20260102, 3, 10, 1, 25),
    (1005, 20260103, 2, 40, 2, 50),
    (1006, 20260103, 3, 20, 1, 80),
]


def seed_panel(s, x=75, y=535, w=920):
    s.container(x, y, w, 465, "Canonical book model  |  January 1-3, 2026", "teal")
    s.box(x + 35, y + 90, 265, 140, "DimCustomer\n3 customers\nGB / DE", "teal", 28)
    s.box(x + 330, y + 90, 265, 140, "DimProduct\n4 products\n4 categories", "teal", 28)
    s.box(x + 625, y + 90, 260, 140, "DimDate\n3 dates\nJanuary 2026", "teal", 28)
    s.box(x + 200, y + 300, 520, 120, "book.FactSales\n6 rows  |  SalesKey 1001-1006", "blue", 30)
    for xx in [x + 167, x + 462, x + 755]:
        target = min(max(xx, x + 270), x + 650)
        s.arrow([(xx, y + 230), (xx, y + 255), (target, y + 255), (target, y + 290)], "teal")


def validation_panel(s, title, route):
    s.container(1100, 535, 525, 465, title, "green")
    s.box(1140, 625, 445, 160, "6 facts\n10 units\n365.00 revenue", "green", 33)
    s.box(1140, 825, 445, 125, "Country reconciliation\nGB 185.00  |  DE 180.00", "green", 28)
    s.arrow([(1005, 895), (1090, 895)], "green")
    s.note(1100, 493, route, 525, 27)


def first_warehouse():
    s = Scene(21, "first-warehouse", "First Warehouse: create, seed, then reconcile",
              "BookWarehouse / book  |  SQL writes own this independent teaching dataset.", [4],
              "Concrete high-level walkthrough of the book's Warehouse seed: create BookWarehouse, "
              "run 04-create-book-warehouse.sql, then verify the six canonical sales, ten units "
              "and 365.00 revenue, with GB 185.00 and DE 180.00.",
              "Expected values are computed offline from the canonical seed, not measured against a live tenant. "
              "Run write scripts only in the isolated book lab.")
    s.box(75, 235, 430, 165, "1  Create Warehouse\nName: BookWarehouse\nOpen its SQL context", "blue", 30)
    s.box(635, 235, 430, 165, "2  Run the seed script\nCreate book schema + tables\nInsert canonical rows", "blue", 29)
    s.box(1195, 235, 430, 165, "3  Query and reconcile\nCheck object names,\nrow counts and revenue", "green", 29)
    s.arrow([(515, 317), (625, 317)], "blue")
    s.arrow([(1075, 317), (1185, 317)], "green")
    s.note(75, 443, "Script: 04-create-book-warehouse.sql", 960, 29)
    seed_panel(s)
    validation_panel(s, "Warehouse SQL check", "Read-only verification after seeding")
    return s.finish("These rows are separate from BookLakehouse's identical starting seed; changing one does not update the other.")


def first_lakehouse():
    s = Scene(22, "first-lakehouse", "First Lakehouse: write with Spark, read through SQL",
              "BookLakehouse / book  |  Same canonical seed, independent tables and write ownership.", [5],
              "Concrete high-level walkthrough: create a schema-enabled BookLakehouse, attach it "
              "to a Spark notebook, run 05-create-book-lakehouse.py, then verify discovery and "
              "read the canonical rows through the SQL analytics endpoint.",
              "The endpoint is a read surface for Lakehouse tables. Metadata readiness must be "
              "verified; no fixed wait guarantees freshness. Expected totals are offline seed checks.")
    s.box(65, 235, 350, 180, "1  Create Lakehouse\nBookLakehouse\nSchema-enabled", "teal", 29)
    s.box(470, 235, 350, 180, "2  Attach notebook\nSpark seed script\nWrites Delta tables", "teal", 29)
    s.box(875, 235, 350, 180, "3  Verify SQL metadata\nDiscover book tables\nCheck freshness", "blue", 28)
    s.box(1280, 235, 350, 180, "4  Read with SQL\nUse the Lakehouse\nSQL analytics endpoint", "green", 27)
    for a, b in [(425, 460), (830, 865), (1235, 1270)]:
        s.arrow([(a, 325), (b, 325)], "teal")
    s.note(75, 453, "Script: 05-create-book-lakehouse.py", 980, 29)
    seed_panel(s)
    validation_panel(s, "SQL endpoint check", "Read-only verification after discovery")
    return s.finish("Spark seeds the Lakehouse. The SQL endpoint reads its tables; it is not a second writer or a Warehouse copy.")


def hybrid_warehouse():
    s = Scene(
        23, "hybrid-warehouse-architecture",
        "Warehouse + Lakehouse: one SQL architecture",
        "Hosted Delta and cloud/OneLake shortcuts feed a governed, same-workspace SQL route.",
        [9],
        "Cloud Delta tables and mirrored-database targets are exposed through integration "
        "Lakehouse shortcuts beside hosted Delta tables. The Lakehouse SQL analytics endpoint "
        "serves Warehouse three-part reads, with optional Warehouse-owned gold materialization.",
        "Conceptual current architecture, not a measured deployment or a claim that arbitrary "
        "files are SQL tables. Shortcut/source identities, formats and freshness remain separate.",
        evidence_reviewed_on="2026-11-09",
    )
    s.box(65, 270, 300, 220,
          "Cloud Delta tables\nADLS Gen2\nAmazon S3 / GCS", "teal", 26)
    s.box(65, 560, 300, 190,
          "Mirrored databases\nOneLake table targets\nProducer-owned", "teal", 25)
    s.note(65, 770, "GCS = Google Cloud Storage", 330, 22)
    s.note(65, 815, "A shortcut is a reference,\nnot an immutable archive.", 330, 24)
    s.container(425, 220, 1220, 790,
                "Consumer workspace: SQL three-part scope", "gray")
    s.container(460, 290, 530, 490, "Integration Lakehouse", "teal")
    s.box(495, 365, 230, 150,
          "Tables shortcuts\nCloud + OneLake\nRead references", "teal", 25)
    s.box(755, 365, 200, 150,
          "Hosted\nDelta tables\nLocal writer", "teal", 26)
    s.box(495, 640, 460, 105,
          "SQL analytics endpoint\nExposes eligible tables", "blue", 27)
    s.box(1125, 345, 475, 235,
          "Warehouse\nSQL joins + transformation\nOptional gold tables", "blue", 29)
    s.box(1125, 700, 475, 130,
          "Governed consumers\nSQL clients / Power BI", "green", 26)
    s.arrow([(365, 380), (410, 380), (410, 405), (485, 405)], "teal")
    s.arrow([(365, 655), (410, 655), (410, 470), (485, 470)], "teal")
    s.arrow([(610, 525), (610, 630)], "teal")
    s.arrow([(855, 525), (855, 630)], "teal")
    s.arrow([(965, 692), (1055, 692), (1055, 470), (1115, 470)], "blue")
    s.note(1005, 715, "SQL read", 105, 24)
    s.arrow([(1360, 590), (1360, 690)], "green")
    s.box(460, 855, 1140, 100,
          "Warehouse SQL: [IntegrationLakehouse].[schema].[table]\n"
          "Formats, identities, freshness and write ownership still matter.", "gray", 25)
    return s.finish(
        "Query in place when appropriate. Materialize gold deliberately; a shortcut does not transfer write ownership."
    )


def delta_anatomy():
    s = Scene(
        24, "delta-table-anatomy",
        "Anatomy of a Delta table: values plus valid state",
        "Parquet encodes values. Delta selects a table snapshot. Warehouse publishes outward after SQL commit.",
        [3, 11, 39],
        "A simplified Delta table combines Parquet data files, JSON transaction actions and "
        "checkpoint metadata. Warehouse SQL commit, background Delta publication and an "
        "authorized external reader observing that state are separate boundaries.",
        "Conceptual format/publishing map, not a private Warehouse directory layout. "
        "A checkpoint holds metadata, not another batch of business rows; external access "
        "does not automatically inherit SQL RLS or CLS.",
        evidence_reviewed_on="2026-11-09",
    )
    s.container(65, 225, 1000, 770, "A Delta table (simplified)", "teal")
    s.box(100, 320, 425, 200,
          "Parquet data files\nRow groups > column chunks\nEncoded/compressed pages\nFooter + type annotations",
          "teal", 25)
    s.box(100, 600, 425, 170,
          "Version 0: A + B\nVersion 1: B + C\nA can remain for retention", "gray", 25)
    s.container(575, 300, 455, 545, "_delta_log (metadata)", "blue")
    s.box(610, 385, 385, 160,
          "JSON commit versions\nSchema + protocol\nAdd/remove file actions", "blue", 24)
    s.box(610, 625, 385, 155,
          "Checkpoint metadata\nSummarizes log state\nNot sales rows", "blue", 24)
    s.arrow([(800, 555), (800, 615)], "blue")
    s.box(100, 895, 895, 70,
          "Delta selects active files; a Parquet glob does not.", "gray", 25)
    s.container(1115, 225, 525, 770, "Warehouse publication", "gray")
    s.box(1150, 335, 455, 145,
          "1  SQL transaction commits\nNew SQL reads can be current", "blue", 25)
    s.box(1150, 565, 455, 145,
          "2  Background publisher\nEmits compatible Delta state", "teal", 25)
    s.box(1150, 795, 455, 145,
          "3  External Delta reader\nChecks its own access and\nobserves published state", "green", 25)
    s.arrow([(1375, 490), (1375, 555)], "teal")
    s.arrow([(1375, 720), (1375, 785)], "green")
    return s.finish(
        "Persisted types and reader compatibility are contracts; visible files alone do not prove a committed table state."
    )


BUILDERS = [
    platform, concepts, onelake_paths, ownership, decision, gpu, security,
    workspace_identity, query_lifecycle, storage, metadata_sync, statistics,
    monitoring, capacity, cache, release, migration, iq, clone, logical_sql,
    first_warehouse, first_lakehouse, hybrid_warehouse, delta_anatomy,
]


def stroke(draw, points, fill, width, dashed=False):
    if not dashed:
        draw.line(points, fill=fill, width=width, joint="curve")
        return
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        length = math.hypot(x2 - x1, y2 - y1)
        if not length:
            continue
        for offset in range(0, math.ceil(length), 22):
            end = min(offset + 13, length)
            draw.line([(x1 + (x2 - x1) * offset / length, y1 + (y2 - y1) * offset / length),
                       (x1 + (x2 - x1) * end / length, y1 + (y2 - y1) * end / length)],
                      fill=fill, width=width)


def arrow_head(points, length=15, half=7):
    ex, ey = points[-1]
    for px, py in reversed(points[:-1]):
        distance = math.hypot(ex - px, ey - py)
        if distance:
            dx, dy = (ex - px) / distance, (ey - py) / distance
            return [(ex, ey), (ex - dx * length - dy * half, ey - dy * length + dx * half),
                    (ex - dx * length + dy * half, ey - dy * length - dx * half)]
    raise ValueError("Arrow has no direction")


def render_png(scene):
    scale = 2
    image = Image.new("RGB", (W * scale, H * scale), "white")
    d = ImageDraw.Draw(image)
    for e in scene.elements:
        kind = e["kind"]
        if kind == "text":
            f = font(e["size"] * scale, e["bold"])
            for i, line in enumerate(e["text"].split("\n")):
                x = e["x"]
                if e["align"] == "center":
                    x += (e["w"] - f.getlength(line) / scale) / 2
                y = e["y"] + i * e["size"] * 1.32
                d.text((round(x * scale), round(y * scale)), line,
                       font=f, fill="#000000", anchor="lt")
        elif kind == "rect":
            border, fill = COLORS[e["color"]]
            x, y, w, h = [e[k] * scale for k in ("x", "y", "w", "h")]
            bbox = (x, y, x + w, y + h)
            if e["dashed"]:
                if e["fill"]:
                    d.rounded_rectangle(bbox, radius=e["radius"] * scale, fill=fill)
                stroke(d, [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)],
                       border, 3 * scale, True)
            else:
                d.rounded_rectangle(bbox, radius=e["radius"] * scale,
                                    fill=fill if e["fill"] else None,
                                    outline=border, width=3 * scale)
        else:
            border = COLORS[e["color"]][0]
            pts = [(x * scale, y * scale) for x, y in e["points"]]
            stroke(d, pts, border, e["stroke_width"] * scale, e["dashed"])
            if kind == "arrow":
                d.polygon(arrow_head(pts, 16 * scale, 7 * scale), fill=border)
    return image.resize((W, H), Image.Resampling.LANCZOS)


def render_svg(scene):
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        f"<title id=\"title\">{escape(scene.title)}</title>",
        f"<desc id=\"desc\">{escape(scene.caption + ' ' + scene.caveat)}</desc>",
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
    ]
    for e in scene.elements:
        kind = e["kind"]
        if kind == "text":
            x = e["x"] + (e["w"] / 2 if e["align"] == "center" else 0)
            anchor = "middle" if e["align"] == "center" else "start"
            weight = 700 if e["bold"] else 400
            parts.append(f'<text id="{e["id"]}" x="{x}" y="{e["y"]}" fill="#000000" '
                         f'font-family="Segoe UI, Arial, sans-serif" font-size="{e["size"]}" '
                         f'font-weight="{weight}" text-anchor="{anchor}" dominant-baseline="text-before-edge">')
            for i, line in enumerate(e["text"].split("\n")):
                y = e["y"] + i * e["size"] * 1.32
                parts.append(f'<tspan x="{x}" y="{y}">{escape(line)}</tspan>')
            parts.append("</text>")
        elif kind == "rect":
            border, fill = COLORS[e["color"]]
            fill = fill if e["fill"] else "none"
            dash = ' stroke-dasharray="13 9"' if e["dashed"] else ""
            parts.append(f'<rect id="{e["id"]}" x="{e["x"]}" y="{e["y"]}" width="{e["w"]}" '
                         f'height="{e["h"]}" rx="{e["radius"]}" fill="{fill}" '
                         f'stroke="{border}" stroke-width="3"{dash}/>')
        else:
            border = COLORS[e["color"]][0]
            pts = " ".join(f"{x},{y}" for x, y in e["points"])
            dash = ' stroke-dasharray="13 9"' if e["dashed"] else ""
            parts.append(f'<polyline id="{e["id"]}" points="{pts}" fill="none" stroke="{border}" '
                         f'stroke-width="{e["stroke_width"]}" stroke-linejoin="round"{dash}/>')
            if kind == "arrow":
                pts = " ".join(f"{x:.2f},{y:.2f}" for x, y in arrow_head(e["points"], 16, 7))
                parts.append(f'<polygon points="{pts}" fill="{border}"/>')
    parts.append("</svg>")
    return "\n".join(parts)


def render_excalidraw(scene):
    elements = []
    for i, e in enumerate(scene.elements):
        token = int(hashlib.sha256(e["id"].encode()).hexdigest()[:7], 16)
        base = {
            "id": e["id"], "type": e["kind"], "angle": 0,
            "strokeColor": "#000000", "backgroundColor": "transparent",
            "fillStyle": "solid", "strokeWidth": 3, "strokeStyle": "solid",
            "roughness": 0, "opacity": 100, "groupIds": [],
            "frameId": None, "index": None, "roundness": None,
            "seed": token, "version": 1, "versionNonce": token + 1,
            "isDeleted": False, "boundElements": None, "updated": 1791500400000,
            "link": None, "locked": False,
        }
        if e["kind"] == "text":
            base.update(type="text", x=e["x"], y=e["y"], width=e["w"],
                        height=e["size"] * 2.5 * len(e["text"].split("\n")),
                        fontSize=e["size"], fontFamily=2, text=e["text"],
                        textAlign=e["align"], verticalAlign="top",
                        containerId=None, originalText=e["text"],
                        autoResize=False, lineHeight=1.32,
                        baseline=e["size"])
            if e["parent"]:
                base["groupIds"] = [e["parent"] + "-group"]
        elif e["kind"] == "rect":
            border, fill = COLORS[e["color"]]
            base.update(type="rectangle", x=e["x"], y=e["y"], width=e["w"],
                        height=e["h"], strokeColor=border,
                        backgroundColor=fill if e["fill"] else "transparent",
                        roundness={"type": 3},
                        strokeStyle="dashed" if e["dashed"] else "solid")
            if not e["container"]:
                base["groupIds"] = [e["id"] + "-group"]
        else:
            x0, y0 = e["points"][0]
            xs, ys = zip(*e["points"])
            base.update(type=e["kind"], x=x0, y=y0,
                        width=max(xs) - min(xs), height=max(ys) - min(ys),
                        points=[[x - x0, y - y0] for x, y in e["points"]],
                        strokeColor=COLORS[e["color"]][0],
                        strokeWidth=e["stroke_width"],
                        strokeStyle="dashed" if e["dashed"] else "solid",
                        startBinding=None, endBinding=None, startArrowhead=None,
                        endArrowhead="arrow" if e["kind"] == "arrow" else None,
                        lastCommittedPoint=None, elbowed=False)
        elements.append(base)
    return {
        "type": "excalidraw", "version": 2, "source": "Fabric Warehouse Book",
        "elements": elements,
        "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None,
                     "scrollX": 0, "scrollY": 0, "zoom": {"value": 1}},
        "files": {},
    }


def validate(scene):
    ids = [e["id"] for e in scene.elements]
    assert len(ids) == len(set(ids)), scene.id
    by_id = {e["id"]: e for e in scene.elements}
    for e in scene.elements:
        if e["kind"] in ("arrow", "line"):
            assert len(e["points"]) >= 2
            assert all(0 <= x <= W and 0 <= y <= H for x, y in e["points"]), e
        elif e["kind"] == "rect":
            assert 0 <= e["x"] and e["x"] + e["w"] <= W
            assert 0 <= e["y"] and e["y"] + e["h"] <= H
            assert not e["container"] or not e["fill"]
        elif e["parent"]:
            p = by_id[e["parent"]]
            assert e["y"] >= p["y"]
            assert e["y"] + e["h"] <= p["y"] + p["h"] + 0.1
    for arrow in (e for e in scene.elements if e["kind"] == "arrow"):
        for t in (e for e in scene.elements if e["kind"] == "text"):
            f = font(t["size"], t["bold"])
            for i, line in enumerate(t["text"].split("\n")):
                width = f.getlength(line)
                x = t["x"] + ((t["w"] - width) / 2 if t["align"] == "center" else 0)
                y = t["y"] + i * t["size"] * 1.32
                left, top, right, bottom = x - 3, y - 3, x + width + 3, y + t["size"] + 3
                for (x1, y1), (x2, y2) in zip(arrow["points"], arrow["points"][1:]):
                    horizontal = (y1 == y2 and top < y1 < bottom
                                  and max(min(x1, x2), left) < min(max(x1, x2), right))
                    vertical = (x1 == x2 and left < x1 < right
                                and max(min(y1, y2), top) < min(max(y1, y2), bottom))
                    assert not (horizontal or vertical), f"{scene.id}: arrow crosses label: {line}"
    excal = json.loads((OUT / f"{scene.id}.excalidraw").read_text("utf-8"))
    for e in excal["elements"]:
        if e["type"] == "text":
            assert e["strokeColor"] == "#000000"
            assert e["width"] > 0 and e["height"] > 0
    svg = ET.parse(OUT / f"{scene.id}.svg").getroot()
    assert svg.attrib["width"] == str(W) and svg.attrib["height"] == str(H)
    with Image.open(OUT / f"{scene.id}.png") as image:
        assert image.size == (W, H)
        image.verify()


def contact_sheets(scenes):
    names = []
    for page, start in enumerate(range(0, len(scenes), 6), 1):
        batch = scenes[start:start + 6]
        tw, th, gap, labelh = 680, 480, 25, 45
        rows = math.ceil(len(batch) / 2)
        sheet = Image.new("RGB", (tw * 2 + gap * 3, (th + labelh + gap) * rows + 95), "#F3F2F1")
        d = ImageDraw.Draw(sheet)
        d.text((gap, 22), f"Fabric Warehouse Book | Diagram QA | Sheet {page}",
               font=font(30, True), fill="black")
        for n, scene in enumerate(batch):
            x = gap + (n % 2) * (tw + gap)
            y = 85 + (n // 2) * (th + labelh + gap)
            with Image.open(OUT / f"{scene.id}.png") as im:
                sheet.paste(im.resize((tw, th), Image.Resampling.LANCZOS), (x, y))
            d.text((x + 3, y + th + 8), scene.id, font=font(23), fill="black")
        name = f"contact-sheet-{page:02d}.png"
        sheet.save(OUT / name)
        names.append(name)
    return names


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    scenes = [builder() for builder in BUILDERS]
    assert len(scenes) == 24
    assert len(SEED) == 6
    assert sum(row[4] for row in SEED) == 10
    assert sum(row[4] * row[5] for row in SEED) == 365
    assert sum(row[4] * row[5] for row in SEED if row[2] != 2) == 185
    assert sum(row[4] * row[5] for row in SEED if row[2] == 2) == 180
    manifest = {
        "schema_version": 1,
        "evidence_cutoff": "2026-10-09",
        "evidence_cutoff_scope": "Original figures 1-22; later figures carry their own evidence_reviewed_on.",
        "latest_diagram_addition": "2026-11-09",
        "diagram_count": len(scenes),
        "canvas": {"width": W, "height": H, "background": "#ffffff"},
        "generation": "Offline Pillow + standard-library SVG + editable Excalidraw, one shared scene",
        "validation": {
            "all_formats_parsed": True,
            "png_svg_dimensions_checked": True,
            "unique_element_ids_checked": True,
            "text_widths_and_box_heights_checked": True,
            "arrow_label_intersections_checked": True,
            "canonical_seed_totals_checked_offline": True,
        },
        "rendering_limits": [
            "Conceptual diagrams are not measured tenant topology, observed plans or performance benchmarks.",
            "PNG uses local Segoe UI. SVG has Segoe UI/Arial fallbacks; Excalidraw uses its Helvetica family.",
            "Excalidraw text has explicit generous dimensions and groups with leaf shapes; font metrics may vary when edited.",
            "Roadmap boundaries are dashed and labeled; preview is not synonymous with coming soon.",
        ],
        "figures": [],
    }
    for scene in scenes:
        files = {ext: f"{scene.id}.{ext}" for ext in ("png", "svg", "excalidraw")}
        render_png(scene).save(OUT / files["png"], optimize=True)
        (OUT / files["svg"]).write_text(render_svg(scene), encoding="utf-8")
        (OUT / files["excalidraw"]).write_text(
            json.dumps(render_excalidraw(scene), ensure_ascii=False, indent=2), encoding="utf-8")
        validate(scene)
        manifest["figures"].append({
            "id": scene.id, "title": scene.title, "intended_chapters": scene.chapters,
            "filenames": files, "caption": scene.caption,
            "conceptual_status_caveat": scene.caveat,
            "evidence_reviewed_on": scene.evidence_reviewed_on,
            "width": W, "height": H, "element_count": len(scene.elements),
        })
    manifest["contact_sheets"] = contact_sheets(scenes)
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Rendered and validated {len(scenes)} diagrams x 3 formats.")
    print(f"Manifest: {OUT / 'manifest.json'}")
    print(f"Contact sheets: {', '.join(manifest['contact_sheets'])}")


if __name__ == "__main__":
    main()
