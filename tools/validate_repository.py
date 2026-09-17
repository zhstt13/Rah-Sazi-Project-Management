#!/usr/bin/env python3
"""کنترل‌های قرارداد مخزن بدون وابستگی خارجی.

این ابزار اعتبارسنج کامل JSON Schema نیست. ساختار قابل‌استفادهٔ مخزن،
قابل‌خواندن‌بودن فایل‌های JSON، هم‌خوانی شناسه‌های نمونه و اجرای ابزارهای
کنترلی قطعی را بررسی می‌کند.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "CHECKLIST_FA.md",
    "ARCHITECTURE.md",
    "REPOSITORY_MAP.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "docs/00-foundations/PERSIAN_FIRST_POLICY.md",
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
        raise ValidationError(f"{path.relative_to(ROOT)}: JSON نامعتبر است: {exc}") from exc


def require_keys(value: dict[str, Any], keys: Iterable[str], label: str) -> None:
    missing = [key for key in keys if key not in value]
    if missing:
        raise ValidationError(f"{label}: کلیدهای لازم وجود ندارند: {', '.join(missing)}")


def unique_ids(records: list[dict[str, Any]], key: str, label: str) -> None:
    ids = [record.get(key) for record in records]
    if any(value in (None, "") for value in ids):
        raise ValidationError(f"{label}: هر رکورد باید {key} داشته باشد")
    if len(ids) != len(set(ids)):
        raise ValidationError(f"{label}: مقدار {key} تکراری است")


def main() -> int:
    errors: list[str] = []
    checked_json = 0

    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"مسیر لازم وجود ندارد: {relative}")

    for path in sorted(ROOT.rglob("*.json")):
        if any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        try:
            read_json(path)
            checked_json += 1
        except ValidationError as exc:
            errors.append(str(exc))

    dashboard_path = ROOT / "apps/dashboard/index.html"
    if dashboard_path.is_file():
        dashboard = dashboard_path.read_text(encoding="utf-8")
        if 'lang="fa"' not in dashboard or 'dir="rtl"' not in dashboard:
            errors.append("داشبورد باید زبان فارسی و جهت راست‌به‌چپ داشته باشد")
    else:
        errors.append("داشبورد وجود ندارد: apps/dashboard/index.html")

    try:
        project = read_json(ROOT / "data/examples/demo-road-project/project.json")
        wbs = read_json(ROOT / "data/examples/demo-road-project/wbs.json")
        progress = read_json(ROOT / "data/examples/demo-road-project/progress.json")
        risks = read_json(ROOT / "data/examples/demo-road-project/risks.json")
        daily = read_json(ROOT / "data/examples/demo-road-project/daily-report.json")
        changes = read_json(ROOT / "data/examples/demo-road-project/change-requests.json")

        project_id = project["project_id"]
        require_keys(project, ["project_id", "name", "status", "contract", "location", "dates", "baselines", "reporting"], "پروژه")
        if wbs["project_id"] != project_id or progress["project_id"] != project_id:
            raise ValidationError("شناسهٔ پروژه در WBS یا پیشرفت با پروژه یکسان نیست")
        if risks["project_id"] != project_id or daily["project_id"] != project_id or changes["project_id"] != project_id:
            raise ValidationError("شناسهٔ پروژه در ریسک، گزارش روزانه یا تغییر یکسان نیست")

        unique_ids(wbs["items"], "wbs_id", "WBS")
        unique_ids(progress["records"], "progress_id", "پیشرفت")
        unique_ids(risks["records"], "risk_id", "ریسک‌ها")
        unique_ids(changes["records"], "change_id", "تغییرها")
        require_keys(daily, ["report_id", "date", "work_fronts", "quantities", "quality", "hse", "evidence"], "گزارش روزانه")

        wbs_ids = {item["wbs_id"] for item in wbs["items"]}
        wbs_status = {item["wbs_id"]: item["status"] for item in wbs["items"]}
        for record in progress["records"]:
            if record["wbs_id"] not in wbs_ids:
                raise ValidationError(f"پیشرفت {record['progress_id']}: wbs_id ناشناخته است")
            for field in ("planned_value", "earned_value", "actual_cost"):
                if not isinstance(record[field], (int, float)) or record[field] < 0:
                    raise ValidationError(f"پیشرفت {record['progress_id']}: {field} نامعتبر است")
            if record.get("quantity") == 0 and (record["earned_value"] > 0 or record["physical_progress_pct"] > 0):
                raise ValidationError(f"پیشرفت {record['progress_id']}: مقدار صفر با ارزش یا پیشرفت مثبت سازگار نیست")
            if wbs_status[record["wbs_id"]] == "planned" and (record["earned_value"] > 0 or record["physical_progress_pct"] > 0):
                raise ValidationError(f"پیشرفت {record['progress_id']}: WBS برنامه‌ریزی‌شده نمی‌تواند پیشرفت کسب‌شده داشته باشد")

        total_pv = sum(record["planned_value"] for record in progress["records"])
        total_ev = sum(record["earned_value"] for record in progress["records"])
        total_ac = sum(record["actual_cost"] for record in progress["records"])
        if not (total_pv > 0 and total_ev >= 0 and total_ac >= 0):
            raise ValidationError("جمع پیشرفت برای محاسبهٔ ارزش کسب‌شده قابل استفاده نیست")

    except (KeyError, TypeError, ValidationError) as exc:
        errors.append(f"دادهٔ نمونه: {exc}")

    if errors:
        print("اعتبارسنجی ناموفق بود")
        for error in errors:
            print(f"- {error}")
        return 1

    print("اعتبارسنجی موفق بود")
    print(f"- تعداد فایل‌های JSON خوانده‌شده: {checked_json}")
    print("- مسیرهای لازم موجود هستند")
    print("- شناسه‌ها و ارجاع‌های پروژهٔ نمونه هم‌خوان هستند")
    print("- دادهٔ پیشرفت برای ارزش کسب‌شده قابل استفاده است")
    print("- داشبورد فارسی و راست‌به‌چپ است")
    return 0


if __name__ == "__main__":
    sys.exit(main())
