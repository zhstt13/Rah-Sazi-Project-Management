# نقشهٔ ریپو

این فایل مشخص می‌کند هر موضوع مالک کجاست. یک موضوع نباید هم‌زمان چند مرجع رسمی و متناقض داشته باشد.

## شروع سریع

| سؤال | فایل |
|---|---|
| پروژه چیست؟ | README.md |
| چک‌لیست اصلی کجاست؟ | CHECKLIST_FA.md |
| قانون فارسی‌سازی چیست؟ | docs/00-foundations/PERSIAN_FIRST_POLICY.md |
| مرز و معماری چیست؟ | ARCHITECTURE.md |
| تغییرات چگونه انجام می‌شوند؟ | CONTRIBUTING.md |
| تصمیم‌ها کجا ثبت می‌شوند؟ | DECISIONS.md |
| قوانین حاکمیت چیست؟ | GOVERNANCE.md |
| اعتبارسنجی چگونه اجرا می‌شود؟ | tools/validate_repository.py |
| داشبورد کجاست؟ | apps/dashboard/index.html |

## مالکیت موضوع‌ها

| موضوع | مالک رسمی |
|---|---|
| زبان و بومی‌سازی | CHECKLIST_FA.md و PERSIAN_FIRST_POLICY.md |
| هویت پروژه | Project Profile و دادهٔ پروژه |
| WBS، BOQ و کد هزینه | docs/02-controls/WBS_CBS_AND_COST_CODES.md و schemas |
| زمان‌بندی | docs/02-controls/SCHEDULE_CONTROL.md |
| هزینه و EVM | docs/02-controls/COST_AND_EVM.md و tools/evm.py |
| ریسک و مسئله | docs/02-controls/RISK_ISSUE_OPPORTUNITY.md |
| تغییر | docs/02-controls/CHANGE_CONTROL.md |
| قرارداد و Claim | docs/02-controls/CONTRACTS_CLAIMS_AND_PAYMENTS.md |
| کیفیت | docs/02-controls/QUALITY_CONTROL.md |
| HSE و محیط‌زیست | docs/02-controls/HSE_AND_ENVIRONMENT.md |
| تأمین | docs/02-controls/PROCUREMENT_AND_SUPPLY_CHAIN.md |
| زمین و تأسیسات | docs/02-controls/STAKEHOLDER_AND_LAND_UTILITIES.md |
| اسناد | docs/02-controls/DOCUMENT_CONTROL.md |
| گزارش و KPI | docs/03-reporting |
| هوش مصنوعی | docs/04-ai/AI_OPERATING_MODEL.md |

## قرارداد پوشه‌ها

- apps: سطح قابل‌اجرا یا قابل‌مشاهده؛
- config: تنظیمات پروژه، آستانه‌ها و طبقه‌بندی؛
- data: دادهٔ مرجع و نمونهٔ صریحاً فرضی؛
- docs: قواعد، روش‌ها و توضیحات انسانی؛
- schemas: قرارداد ماشین‌خوان؛
- templates: قالب، نه رکورد واقعی؛
- tools: ابزارهای قطعی و کم‌وابستگی؛
- .github: همکاری، فرم‌ها و CI.

## وضعیت داده

هر گزارش باید مشخص کند داده:

- مشاهده‌شده است؛
- محاسبه‌شده است؛
- تخمینی است؛
- فرض موقت است؛
- تصمیم‌گیری شده است؛
- یا نامعلوم است.

نسخهٔ فعلی هنوز دادهٔ واقعی پروژه ندارد.
