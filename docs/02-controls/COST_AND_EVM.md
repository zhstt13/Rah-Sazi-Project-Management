# Cost Control and Earned Value

## Cost structure

Separate at least:

- approved budget/baseline;
- commitments and purchase orders;
- actual cost/accruals;
- forecast to complete;
- estimate at completion;
- approved and pending changes;
- contingency and management reserve;
- payment value and cash flow.

Keep the accounting source and cut-off date with every imported number.

## Core metrics

For a reporting period:

- PV (planned value) = budgeted value of planned work.
- EV (earned value) = budgeted value of completed/accepted work.
- AC (actual cost) = cost incurred for the performed work.
- SV = EV − PV.
- CV = EV − AC.
- SPI = EV / PV when PV > 0.
- CPI = EV / AC when AC > 0.
- EAC method 1 = BAC / CPI when CPI > 0.
- EAC method 2 = AC + (BAC − EV) when remaining work is expected at budget.
- ETC = EAC − AC.
- VAC = BAC − EAC.

The repository calculator exposes arithmetic; project controls must select and explain the forecast method.

## Measurement rules

- Earned value comes from an approved progress method, not subjective completion alone.
- Quantity-based work should retain quantity, unit, location, acceptance status and evidence.
- Milestone or weighted rules need an approved basis and should avoid front-loading.
- Do not earn value for rejected work unless the project’s approved measurement rule explicitly allows it.
- Align PV, EV and AC cut-off dates before interpreting indices.
- Explain variance thresholds from config/control-thresholds.json.

## Forecast narrative

Every monthly forecast should answer:

1. What changed since the previous forecast?
2. Which drivers are temporary and which are structural?
3. What is the confidence range and key assumption?
4. What action could change the outcome?
5. Which decision or change request is required?

EVM is a decision signal, not a substitute for commercial accounts or certified payment.
