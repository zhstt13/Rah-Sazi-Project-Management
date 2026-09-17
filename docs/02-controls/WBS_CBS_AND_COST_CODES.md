# WBS, BOQ and Cost Codes

## Why the model matters

A road project becomes controllable when scope, quantity, location, schedule, responsibility and money refer to the same work package. A WBS is not just a list of headings: it should stop at a level where work can be planned, measured, assigned and valued.

## Minimum coding stack

| Layer | Example | Purpose |
|---|---|---|
| Project | RS-001 | identity |
| Contract | C-01 | commercial boundary |
| WBS | 03.04.02 | deliverable/work package |
| BOQ/pay item | EARTH-EXC-001 | measurable contract item |
| CBS | CIV-ROAD-EXC | cost aggregation |
| Location | CH 12+400–13+100 | spatial control |
| Responsibility | SITE-EAST | accountable team |
| Resource | PLANT-EXC-02 | productivity/equipment |
| Baseline | BL-SCH-001 / BL-CST-001 | time and cost context |

Do not force every code into one opaque string. Store separate fields and provide a reporting key when needed.

## WBS decomposition test

A work package is ready when:

- its scope and acceptance criteria are clear;
- it has a responsible owner;
- it can be linked to activities and measurable quantities;
- its budget or value basis is known;
- its location and interfaces are visible;
- its progress method is defined;
- its risks and quality/HSE controls are identifiable.

Stop decomposing when further splitting would not improve control or evidence.

## BOQ/pay-item contract

For each pay item, keep:

- source schedule/rate book and edition;
- pay-item code and description;
- unit of measure;
- contract quantity and rate;
- revised quantity/rate basis if changed;
- WBS and location mapping;
- measurement rule and evidence type;
- cost code and responsible owner;
- status: draft, approved, superseded or closed.

A local public-works rate library can be added later as a versioned reference package. Never silently mix rate editions.

## Baseline relationship

WBS → BOQ/pay item → planned quantity → activity → planned value → measured quantity → earned value → actual cost → forecast.

If a link is unknown, record unknown and create an action; do not infer it from a similar item.
