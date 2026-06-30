from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from engine.core.rule_database import RuleRecord, get_rule_database
from engine.core.taxonomy import (
    CategoryCode,
    RuleType,
    parse_category_from_rule_id,
    parse_rule_type,
)


@dataclass(frozen=True)
class RuleRegistryEntry:
    rule_id: str
    name: str
    category: CategoryCode
    rule_type: RuleType
    subcategory: str
    status: str
    function: str
    spec_path: str
    legacy_ids: tuple[str, ...] = ()


def _record_to_entry(record: RuleRecord) -> RuleRegistryEntry:
    impl = record.implementation_path
    function = impl.split(".")[-1] if "." in impl else impl
    return RuleRegistryEntry(
        rule_id=record.rule_id,
        name=record.rule_name,
        category=parse_category_from_rule_id(record.rule_id),
        rule_type=parse_rule_type(record.rule_id),
        subcategory=record.subcategory_name,
        status=record.status,
        function=function,
        spec_path=record.spec_path,
        legacy_ids=(),
    )


class RuleRegistry:
    """
    Facade over TASS-013 Rule Database (SSOT).
    rules/registry.yaml is the seed source; runtime truth is rule_database/tass_rules.db.
    """

    def __init__(self, path: Path | None = None):
        self.path = path  # legacy; seed uses default registry.yaml
        self._db = get_rule_database()

    def get(self, rule_id: str) -> RuleRegistryEntry | None:
        record = self._db.get_rule(rule_id)
        return _record_to_entry(record) if record else None

    def resolve(self, rule_id: str) -> str:
        return self._db.resolve(rule_id)

    def all_rules(self) -> list[RuleRegistryEntry]:
        return [_record_to_entry(r) for r in self._db.all_rules()]

    def rules_by_category(self, category: CategoryCode) -> list[RuleRegistryEntry]:
        return [_record_to_entry(r) for r in self._db.search(category_code=category.value)]

    def is_registered(self, rule_id: str) -> bool:
        return self._db.get_rule(rule_id) is not None

    def category_codes(self) -> list[str]:
        return self._db.list_categories()


_default_registry: RuleRegistry | None = None


def get_registry() -> RuleRegistry:
    global _default_registry
    if _default_registry is None:
        _default_registry = RuleRegistry()
    return _default_registry
