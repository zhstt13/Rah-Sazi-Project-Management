#!/usr/bin/env python3
"""Dependency-light repository contract checks.

This is intentionally not a full JSON Schema validator. It checks that the
repository is structurally usable, JSON files parse, core example identifiers
are coherent, and deterministic control utilities remain runnable.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "ARCHITECTURE.md",
    "REPOSITORY_MAP.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "schemas/project.schema.json",
    "schemas/wbs-item.schema.json",
    "schemas/progress-record.schema.json",
    "schemas/risk.schema.json",
    "schemas/change-request.schema.json",
    "schemas/daily-report.schema.json",
    "schemas/document.schema.json",
    "schemas/quality-inspection.schema.json",
    "config/control-thresholds.json",
    "data/examples/demo-road-project/project.json",
    "data/examples/demo-road-project/wbs.json",
    "data/examples/demo-road-project/progress.json",
    "data/examples/demo-road-project/risks.json",
    "data/examples/demo-road-project/daily-report.json",
    "data/examples/demo-road-project/change-requests.json",
    "tools/evm.py",
]


class ValidationError(Exception):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationError(f"{path.relative_to(ROOT)}: invalid JSON: {exc}") from exc


def require_keys(value: dict[str, Any], keys: Iterable[str], label: str) -> None:
    missing = [key for key in keys if key not in value]
    if missing:
        raise ValidationError(f"{label}: missing keys: {', '.join(missing)}")


def unique_ids(records: list[dict[str, Any]], key: str, label: str) -> None:
    ids = [record.get(key) for record in records]
    if any(value in (None, "") for value in ids):
        raise ValidationError(f"{label}: every record needs {key}")
    if len(ids) != len(set(ids)):
        raise ValidationError(f"{label}: duplicate {key}")


def main() -> int:
    errors: list[str] = []
    checked_json = 0

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required path: {relative}")

    for path in sorted(ROOT.rglob("*.json")):
        if any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        try:
            read_json(path)
            checked_json += 1
        except ValidationError as exc:
            errors.append(str(exc))

    try:
        project = read_json(ROOT / "data/examples/demo-road-project/project.json")
        wbs = read_json(ROOT / "data/examples/demo-road-project/wbs.json")
        progress = read_json(ROOT / "data/examples/demo-road-project/progress.json")
        risks = read_json(ROOT / "data/examples/demo-road-project/risks.json")
        daily = read_json(ROOT / "data/examples/demo-road-project/daily-report.json")
        changes = read_json(ROOT / "data/examples/demo-road-project/change-requests.json")

        project_id = project["project_id"]
        require_keys(project, ["project_id", "name", "status", "contract", "location", "dates", "baselines", "reporting"], "project")
        if wbs["project_id"] != project_id or progress["project_id"] != project_id:
            raise ValidationError("demo WBS/progress project_id does not match project")
        if risks["project_id"] != project_id or daily["project_id"] != project_id or changes["project_id"] != project_id:
            raise ValidationError("demo risk/daily/change project_id does not match project")

        unique_ids(wbs["items"], "wbs_id", "wbs")
        unique_ids(progress["records"], "progress_id", "progress")
        unique_ids(risks["records"], "risk_id", "risks")
        unique_ids(changes["records"], "change_id", "changes")
        require_keys(daily, ["report_id", "date", "work_fronts", "quantities", "quality", "hse", "evidence"], "daily report")

        wbs_ids = {item["wbs_id"] for item in wbs["items"]}
        for record in progress["records"]:
            if record["wbs_id"] not in wbs_ids:
                raise ValidationError(f"progress {record['progress_id']}: unknown wbs_id")
            for field in ("planned_value", "earned_value", "actual_cost"):
                if not isinstance(record[field], (int, float)) or record[field] < 0:
                    raise ValidationError(f"progress {record['progress_id']}: invalid {field}")

        total_pv = sum(record["planned_value"] for record in progress["records"])
        total_ev = sum(record["earned_value"] for record in progress["records"])
        total_ac = sum(record["actual_cost"] for record in progress["records"])
        if not (total_pv > 0 and total_ev >= 0 and total_ac >= 0):
            raise ValidationError("progress totals are not usable for EVM")

    except (KeyError, TypeError, ValidationError) as exc:
        errors.append(f"demo data: {exc}")

    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALIDATION PASSED")
    print(f"- JSON files parsed: {checked_json}")
    print("- Required paths present")
    print("- Demo project identifiers and references coherent")
    print("- Demo progress is usable for EVM")
    return 0


if __name__ == "__main__":
    sys.exit(main())
