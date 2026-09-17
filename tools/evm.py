#!/usr/bin/env python3
"""محاسبه‌گر کوچک و بدون وابستگی برای ارزش کسب‌شده.

این ابزار فقط شاخص‌های کنترلی را محاسبه می‌کند و دربارهٔ سلامت پروژه،
تأیید پرداخت، تغییر یا ادعا تصمیم نمی‌گیرد.
"""
from __future__ import annotations

import argparse
import json
from decimal import Decimal, InvalidOperation
from typing import Optional


def dec(value: str) -> Decimal:
    try:
        number = Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError(f"عدد معتبر نیست: {value}") from exc
    if number < 0:
        raise argparse.ArgumentTypeError("مقدارها نمی‌توانند منفی باشند")
    return number


def ratio(numerator: Decimal, denominator: Decimal) -> Optional[Decimal]:
    return None if denominator == 0 else numerator / denominator


def money(value: Decimal) -> str:
    return f"{value.quantize(Decimal('0.01'))}"


def main() -> int:
    parser = argparse.ArgumentParser(description="محاسبهٔ شاخص‌های پایهٔ ارزش کسب‌شده.")
    parser.add_argument("--pv", required=True, type=dec, help="ارزش برنامه‌ریزی‌شده")
    parser.add_argument("--ev", required=True, type=dec, help="ارزش کسب‌شده")
    parser.add_argument("--ac", required=True, type=dec, help="هزینهٔ واقعی")
    parser.add_argument("--bac", type=dec, help="بودجه در زمان تکمیل")
    parser.add_argument("--json", action="store_true", dest="as_json", help="خروجی JSON")
    args = parser.parse_args()

    sv = args.ev - args.pv
    cv = args.ev - args.ac
    spi = ratio(args.ev, args.pv)
    cpi = ratio(args.ev, args.ac)
    result = {
        "PV": money(args.pv),
        "EV": money(args.ev),
        "AC": money(args.ac),
        "SV": money(sv),
        "CV": money(cv),
        "SPI": None if spi is None else str(spi.quantize(Decimal("0.0001"))),
        "CPI": None if cpi is None else str(cpi.quantize(Decimal("0.0001"))),
    }
    if args.bac is not None:
        eac_cpi = None if cpi in (None, Decimal("0")) else args.bac / cpi
        eac_remaining_at_budget = args.ac + (args.bac - args.ev)
        result.update({
            "BAC": money(args.bac),
            "EAC_using_CPI": None if eac_cpi is None else money(eac_cpi),
            "EAC_remaining_at_budget": money(eac_remaining_at_budget),
            "ETC_using_CPI": None if eac_cpi is None else money(eac_cpi - args.ac),
            "VAC_using_CPI": None if eac_cpi is None else money(args.bac - eac_cpi),
        })

    if args.as_json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for key, value in result.items():
            print(f"{key}={value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
