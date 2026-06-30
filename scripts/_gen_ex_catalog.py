"""Generate EX rule catalog YAML from frozen EN catalog."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EN_PATH = ROOT / "rules" / "catalog" / "EN_v1.0.yaml"
EX_PATH = ROOT / "rules" / "catalog" / "EX_v1.0.yaml"


def transform_name(name: str) -> str:
    name = (
        name.replace("Entry Bar", "Exit Bar")
        .replace("Entry ", "Exit ")
        .replace("At Entry Bar", "At Exit Bar")
    )
    name = name.replace(" Above ", " __ABOVE__ ").replace(" Below ", " __BELOW__ ")
    name = name.replace(" __ABOVE__ ", " Below ").replace(" __BELOW__ ", " Above ")
    name = name.replace(" Bullish", " __BULL__").replace(" Bearish", " __BEAR__")
    name = name.replace(" __BULL__", " Bearish").replace(" __BEAR__", " Bullish")
    name = name.replace("Gap Up", "__GUP__").replace("Gap Down", "__GDN__")
    name = name.replace("__GUP__", "Gap Down").replace("__GDN__", "Gap Up")
    name = name.replace("Near Bar High", "__NH__").replace("Near Bar Low", "__NL__")
    name = name.replace("__NH__", "Near Bar Low").replace("__NL__", "Near Bar High")
    name = name.replace("At Support", "__SUP__").replace("At Resistance", "__RES__")
    name = name.replace("__SUP__", "At Resistance").replace("__RES__", "At Support")
    return name


def main() -> None:
    en = yaml.safe_load(EN_PATH.read_text(encoding="utf-8"))
    subcats = []
    for sub in en["subcategories"]:
        rules = [
            {"id": rule["id"].replace("EN", "EX"), "name": transform_name(rule["name"])}
            for rule in sub["rules"]
        ]
        subcats.append({"name": sub["name"].replace("Entry", "Exit"), "rules": rules})

    ex = {
        "catalog_version": "1.0",
        "status": "Frozen",
        "category_code": "EX",
        "category_name": "Exit",
        "rule_count": 60,
        "subcategories": subcats,
    }
    header = (
        "# TASS EX Rule Catalog v1.0 — Frozen\n"
        "# Mirror of EN catalog with exit-oriented conditions\n"
        "# 60 atomic Exit rules (EX0001–EX0060)\n\n"
    )
    EX_PATH.write_text(header + yaml.dump(ex, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Wrote {EX_PATH}")


if __name__ == "__main__":
    main()
