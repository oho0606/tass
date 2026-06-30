"""Master registry for all frozen atomic rule catalogs."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.bo.registry import BO_EVALUATORS, get_bo_evaluator
from engine.rules.cf.registry import CF_EVALUATORS, get_cf_evaluator
from engine.rules.cs.registry import CS_EVALUATORS, get_cs_evaluator
from engine.rules.dq.registry import DQ_EVALUATORS, get_dq_evaluator
from engine.rules.en.registry import EN_EVALUATORS, get_en_evaluator
from engine.rules.ex.registry import EX_EVALUATORS, get_ex_evaluator
from engine.rules.gp.registry import GP_EVALUATORS, get_gp_evaluator
from engine.rules.ma.registry import MA_EVALUATORS, get_ma_evaluator
from engine.rules.mo.registry import MO_EVALUATORS, get_mo_evaluator
from engine.rules.mr.registry import MR_EVALUATORS, get_mr_evaluator
from engine.rules.ms.registry import MS_EVALUATORS, get_ms_evaluator
from engine.rules.mt.registry import MT_EVALUATORS, get_mt_evaluator
from engine.rules.pa.registry import PA_EVALUATORS, get_pa_evaluator
from engine.rules.pb.registry import PB_EVALUATORS, get_pb_evaluator
from engine.rules.pt.registry import PT_EVALUATORS, get_pt_evaluator
from engine.rules.rk.registry import RK_EVALUATORS, get_rk_evaluator
from engine.rules.sr.registry import SR_EVALUATORS, get_sr_evaluator
from engine.rules.tr.registry import TR_EVALUATORS, get_tr_evaluator
from engine.rules.vl.registry import VL_EVALUATORS, get_vl_evaluator
from engine.rules.vo.registry import VO_EVALUATORS, get_vo_evaluator

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

CATEGORY_EVALUATORS: dict[str, dict[str, RuleEvaluator]] = {
    "TR": TR_EVALUATORS,
    "MA": MA_EVALUATORS,
    "VL": VL_EVALUATORS,
    "PA": PA_EVALUATORS,
    "MO": MO_EVALUATORS,
    "VO": VO_EVALUATORS,
    "MS": MS_EVALUATORS,
    "SR": SR_EVALUATORS,
    "BO": BO_EVALUATORS,
    "PB": PB_EVALUATORS,
    "PT": PT_EVALUATORS,
    "CS": CS_EVALUATORS,
    "GP": GP_EVALUATORS,
    "RK": RK_EVALUATORS,
    "EN": EN_EVALUATORS,
    "EX": EX_EVALUATORS,
    "MR": MR_EVALUATORS,
    "MT": MT_EVALUATORS,
    "CF": CF_EVALUATORS,
    "DQ": DQ_EVALUATORS,
}

CATEGORY_GETTERS = {
    "TR": get_tr_evaluator,
    "MA": get_ma_evaluator,
    "VL": get_vl_evaluator,
    "PA": get_pa_evaluator,
    "MO": get_mo_evaluator,
    "VO": get_vo_evaluator,
    "MS": get_ms_evaluator,
    "SR": get_sr_evaluator,
    "BO": get_bo_evaluator,
    "PB": get_pb_evaluator,
    "PT": get_pt_evaluator,
    "CS": get_cs_evaluator,
    "GP": get_gp_evaluator,
    "RK": get_rk_evaluator,
    "EN": get_en_evaluator,
    "EX": get_ex_evaluator,
    "MR": get_mr_evaluator,
    "MT": get_mt_evaluator,
    "CF": get_cf_evaluator,
    "DQ": get_dq_evaluator,
}


def get_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator callable for any registered rule ID."""
    category = rule_id[:2]
    getter = CATEGORY_GETTERS.get(category)
    if getter is None:
        raise KeyError(f"Unknown rule category for {rule_id}")
    return getter(rule_id)


def all_rule_ids() -> list[str]:
    """Return sorted list of all registered atomic rule IDs."""
    ids: list[str] = []
    for mapping in CATEGORY_EVALUATORS.values():
        ids.extend(mapping.keys())
    return sorted(ids)


def rule_count() -> int:
    """Return total registered atomic rule count."""
    return len(all_rule_ids())
