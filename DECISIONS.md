# Architecture Decisions

## ADR-001 — GitHub is the control-plane collaboration layer

**Status:** accepted for foundation  
**Decision:** Use GitHub issues, pull requests, commits, releases and structured files as the collaboration and audit layer.

**Why:** It provides reviewable history, ownership, automation and portability. Specialist systems can remain authoritative for detailed scheduling, accounting, CDE, GIS, BIM and field data.

**Consequence:** Every imported snapshot must carry source, revision/date and evidence. GitHub configuration such as branch protection must be completed by the owner.

## ADR-002 — Structured JSON records plus human-readable playbooks

**Status:** accepted for foundation  
**Decision:** Store stable machine-readable records under data/ and schemas/, while keeping operational reasoning and procedures in docs/.

**Why:** Machines need stable fields; people need explanations, exceptions and approval logic. Keeping both in one format would create either opaque or non-validated content.

**Consequence:** Schema changes are compatibility changes and require a PR plus migration note.

## ADR-003 — Evidence-first, append-aware control

**Status:** accepted for foundation  
**Decision:** A status without owner, cut-off date, source and evidence is incomplete. Approved baselines are immutable snapshots; revisions are explicit.

**Why:** Construction decisions often outlive the conversation that produced them. Traceability protects safety, commercial entitlement, forecast quality and institutional memory.

## ADR-004 — Human approval for high-consequence actions

**Status:** accepted for foundation  
**Decision:** AI and automation may classify, calculate, draft and flag; they may not approve safety-critical, contractual, financial, baseline or legal decisions.

**Why:** Automation can reduce administrative effort without transferring accountability.

## ADR-005 — No license in foundation release

**Status:** pending owner decision  
**Decision:** Do not add a license until the owner chooses the intended reuse model.

**Why:** Public visibility does not itself grant reuse rights. A deliberate license and project-specific notices are needed before distribution.
