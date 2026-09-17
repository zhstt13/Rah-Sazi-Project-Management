#!/usr/bin/env python3
"""Small, dependency-free earned-value calculator.

This utility calculates signals only. It does not decide whether a project is healthy
or whether a payment, change or claim is approved.
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
        raise argparse.ArgumentTypeError(f"not a number: {value}") from exc
    if number < 0:
        raise argparse.ArgumentTypeError("values cannot be negative")
    return number


def ratio(numerator: Decimal, denominator: Decimal) -> Optional[Decimal]:
    return None if denominator == 0 else numerator / denominator


def money(value: Decimal) -> str:
    return f"{value.quantize(Decimal('0.01'))}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculate basic earned-value indicators.")
    parser.add_argument("--pv", required=True, type=dec, help="planned value")
    parser.add_argument("--ev", required=True, type=dec, help="earned value")
    parser.add_argument("--ac", required=True, type=dec, help="actual cost")
    parser.add_argument("--bac", type=dec, help="budget at completion")
    parser.add_argument("--json", action="store_true", dest="as_json")
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
        print(json.dumps(result, indent=2))
    else:
        for key, value in result.items():
            print(f"{key}={value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
