"""Generate all remaining catalog atomic rule packages from YAML/markdown catalogs."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG_DIR = ROOT / "rules" / "catalog"
RULES_DIR = ROOT / "engine" / "rules"

YAML_CATEGORIES = [
    "MO",
    "VO",
    "MS",
    "SR",
    "BO",
    "PB",
    "PT",
    "GP",
    "RK",
    "EN",
    "EX",
    "MR",
    "MT",
    "CF",
    "DQ",
]

MARKDOWN_CATEGORIES = {
    "PA": ROOT / "docs" / "TASS-016_PA_Rule_Catalog_v1.0.md",
    "CS": ROOT / "docs" / "TASS-021_CS_Rule_Catalog_v1.0.md",
}


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def _load_yaml_rules(path: Path) -> list[tuple[str, str]]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    rules: list[tuple[str, str]] = []
    for sub in data.get("subcategories", []):
        for rule in sub.get("rules", []):
            rules.append((rule["id"], rule["name"]))
    return rules


def _load_markdown_rules(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    matches = re.findall(r"(PA|CS)(\d{4})\s{1,}([^\n]+)", text)
    rules: list[tuple[str, str]] = []
    seen: set[str] = set()
    for prefix, num, name in matches:
        rule_id = f"{prefix}{num}"
        if rule_id in seen:
            continue
        if not (1 <= int(num) <= 60):
            continue
        seen.add(rule_id)
        rules.append((rule_id, name.strip()))
    return rules


def _load_rules(category: str) -> list[tuple[str, str]]:
    cat = category.upper()
    yaml_path = CATALOG_DIR / f"{cat}_v1.0.yaml"
    if yaml_path.exists():
        return _load_yaml_rules(yaml_path)
    md_path = MARKDOWN_CATEGORIES.get(cat)
    if md_path and md_path.exists():
        return _load_markdown_rules(md_path)
    raise FileNotFoundError(f"No catalog source for {cat}")


def _write_rule_file(category: str, rule_id: str, rule_name: str) -> None:
    code = category.lower()
    slug = _slug(rule_name)
    class_safe = re.sub(r"[^A-Za-z0-9]", "", rule_id + rule_name)
    class_name = f"{class_safe}Rule"
    module = f"{rule_id.lower()}_{slug}"
    path = RULES_DIR / code / f"{module}.py"
    content = f'''"""{rule_id} — {rule_name}. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class {class_name}(SpecRule):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"


def evaluate_{rule_id.lower()}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return run_spec_rule({class_name}, df)
'''
    path.write_text(content, encoding="utf-8")


def generate_category(category: str) -> int:
    code = category.lower()
    out_dir = RULES_DIR / code
    out_dir.mkdir(parents=True, exist_ok=True)
    rules = _load_rules(category)
    for rule_id, rule_name in rules:
        _write_rule_file(category, rule_id, rule_name)

    imports = []
    entries = []
    for rule_id, rule_name in rules:
        slug = _slug(rule_name)
        module = f"engine.rules.{code}.{rule_id.lower()}_{slug}"
        fn = f"evaluate_{rule_id.lower()}"
        imports.append(f"from {module} import {fn}")
        entries.append(f'    "{rule_id}": {fn},')

    registry = f'''"""{category} rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
{chr(10).join(imports)}

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

{category}_EVALUATORS: dict[str, RuleEvaluator] = {{
{chr(10).join(entries)}
}}


def get_{code}_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for {category} rule ID."""
    return {category}_EVALUATORS[rule_id]
'''
    (out_dir / "registry.py").write_text(registry, encoding="utf-8")
    return len(rules)


def main() -> None:
    total = 0
    categories = YAML_CATEGORIES + list(MARKDOWN_CATEGORIES.keys())
    for category in categories:
        count = generate_category(category)
        total += count
        print(f"{category}: {count} rules")
    print(f"generated {total} rules across {len(categories)} categories")


if __name__ == "__main__":
    main()
