"""Composite rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

from engine.core.types import RuleResult
from engine.rules.composite.ctr import evaluate_ctr_rules
from engine.rules.composite.ctr import evaluate_ctr001
from engine.rules.composite.ctr import evaluate_ctr002
from engine.rules.composite.ctr import evaluate_ctr003
from engine.rules.composite.ctr import evaluate_ctr004
from engine.rules.composite.ctr import evaluate_ctr005
from engine.rules.composite.ctr import evaluate_ctr006
from engine.rules.composite.ctr import evaluate_ctr007
from engine.rules.composite.ctr import evaluate_ctr008
from engine.rules.composite.ctr import evaluate_ctr009
from engine.rules.composite.ctr import evaluate_ctr010
from engine.rules.composite.cma001_ma_position_quality import evaluate_cma001
from engine.rules.composite.cma002_ma_alignment_quality import evaluate_cma002
from engine.rules.composite.cma003_golden_cross_strength import evaluate_cma003
from engine.rules.composite.cma004_death_cross_strength import evaluate_cma004
from engine.rules.composite.cma005_ma_trend_quality import evaluate_cma005
from engine.rules.composite.cma006_ma_compression_state import evaluate_cma006
from engine.rules.composite.cma007_ma_expansion_state import evaluate_cma007
from engine.rules.composite.cma008_dynamic_support_quality import evaluate_cma008
from engine.rules.composite.cma009_dynamic_resistance_quality import evaluate_cma009
from engine.rules.composite.cma010_ma_structure_quality import evaluate_cma010
from engine.rules.composite.cpa001_price_strength import evaluate_cpa001
from engine.rules.composite.cpa002_price_weakness import evaluate_cpa002
from engine.rules.composite.cpa003_bullish_price_structure import evaluate_cpa003
from engine.rules.composite.cpa004_bearish_price_structure import evaluate_cpa004
from engine.rules.composite.cpa005_breakout_candle_quality import evaluate_cpa005
from engine.rules.composite.cpa006_pullback_candle_quality import evaluate_cpa006
from engine.rules.composite.cpa007_swing_quality import evaluate_cpa007
from engine.rules.composite.cpa008_range_quality import evaluate_cpa008
from engine.rules.composite.cpa009_price_stability import evaluate_cpa009
from engine.rules.composite.cpa010_price_confirmation import evaluate_cpa010
from engine.rules.composite.cvl001_volume_confirmation import evaluate_cvl001
from engine.rules.composite.cvl002_volume_expansion import evaluate_cvl002
from engine.rules.composite.cvl003_volume_contraction import evaluate_cvl003
from engine.rules.composite.cvl004_accumulation import evaluate_cvl004
from engine.rules.composite.cvl005_distribution import evaluate_cvl005
from engine.rules.composite.cvl006_buying_pressure import evaluate_cvl006
from engine.rules.composite.cvl007_selling_pressure import evaluate_cvl007
from engine.rules.composite.cvl008_volume_quality import evaluate_cvl008
from engine.rules.composite.cvl009_volume_stability import evaluate_cvl009
from engine.rules.composite.cvl010_smart_money_activity import evaluate_cvl010
from engine.rules.composite.cmo001_momentum_strength import evaluate_cmo001
from engine.rules.composite.cmo002_momentum_agreement import evaluate_cmo002
from engine.rules.composite.cmo003_momentum_continuation import evaluate_cmo003
from engine.rules.composite.cmo004_momentum_reversal import evaluate_cmo004
from engine.rules.composite.cmo005_momentum_divergence import evaluate_cmo005
from engine.rules.composite.cmo006_bullish_momentum import evaluate_cmo006
from engine.rules.composite.cmo007_bearish_momentum import evaluate_cmo007
from engine.rules.composite.cmo008_momentum_quality import evaluate_cmo008
from engine.rules.composite.cmo009_momentum_stability import evaluate_cmo009
from engine.rules.composite.cmo010_momentum_confirmation import evaluate_cmo010
from engine.rules.composite.cvo001_volatility_compression import evaluate_cvo001
from engine.rules.composite.cvo002_volatility_expansion import evaluate_cvo002
from engine.rules.composite.cvo003_stable_volatility import evaluate_cvo003
from engine.rules.composite.cvo004_high_volatility import evaluate_cvo004
from engine.rules.composite.cvo005_low_volatility import evaluate_cvo005
from engine.rules.composite.cvo006_breakout_volatility import evaluate_cvo006
from engine.rules.composite.cvo007_risk_volatility import evaluate_cvo007
from engine.rules.composite.cvo008_atr_stability import evaluate_cvo008
from engine.rules.composite.cvo009_volatility_quality import evaluate_cvo009
from engine.rules.composite.cvo010_volatility_confirmation import evaluate_cvo010
from engine.rules.composite.cms001_bull_structure import evaluate_cms001
from engine.rules.composite.cms002_bear_structure import evaluate_cms002
from engine.rules.composite.cms003_structure_break import evaluate_cms003
from engine.rules.composite.cms004_higher_high_sequence import evaluate_cms004
from engine.rules.composite.cms005_lower_low_sequence import evaluate_cms005
from engine.rules.composite.cms006_swing_structure import evaluate_cms006
from engine.rules.composite.cms007_trend_structure import evaluate_cms007
from engine.rules.composite.cms008_structure_quality import evaluate_cms008
from engine.rules.composite.cms009_structure_stability import evaluate_cms009
from engine.rules.composite.cms010_structure_confirmation import evaluate_cms010
from engine.rules.composite.csr001_support_quality import evaluate_csr001
from engine.rules.composite.csr002_resistance_quality import evaluate_csr002
from engine.rules.composite.csr003_support_break import evaluate_csr003
from engine.rules.composite.csr004_resistance_break import evaluate_csr004
from engine.rules.composite.csr005_dynamic_support_quality import evaluate_csr005
from engine.rules.composite.cbo001_breakout_quality import evaluate_cbo001
from engine.rules.composite.cbo002_breakout_confirmation import evaluate_cbo002
from engine.rules.composite.cbo003_false_breakout import evaluate_cbo003
from engine.rules.composite.cbo004_strong_breakout import evaluate_cbo004
from engine.rules.composite.cbo005_breakout_continuation import evaluate_cbo005
from engine.rules.composite.cpb001_healthy_pullback import evaluate_cpb001
from engine.rules.composite.cpb002_deep_pullback import evaluate_cpb002
from engine.rules.composite.cpb003_pullback_recovery import evaluate_cpb003
from engine.rules.composite.cpb004_pullback_quality import evaluate_cpb004
from engine.rules.composite.cpb005_pullback_confirmation import evaluate_cpb005
from engine.rules.composite.cpt001_continuation_pattern import evaluate_cpt001
from engine.rules.composite.cpt002_reversal_pattern import evaluate_cpt002
from engine.rules.composite.cpt003_bullish_pattern import evaluate_cpt003
from engine.rules.composite.cpt004_bearish_pattern import evaluate_cpt004
from engine.rules.composite.cpt005_pattern_quality import evaluate_cpt005
from engine.rules.composite.ccs001_bullish_candle_group import evaluate_ccs001
from engine.rules.composite.ccs002_bearish_candle_group import evaluate_ccs002
from engine.rules.composite.ccs003_reversal_candle_group import evaluate_ccs003
from engine.rules.composite.ccs004_continuation_candle_group import evaluate_ccs004
from engine.rules.composite.ccs005_candle_quality import evaluate_ccs005
from engine.rules.composite.cgp001_bullish_gap import evaluate_cgp001
from engine.rules.composite.cgp002_bearish_gap import evaluate_cgp002
from engine.rules.composite.cgp003_gap_quality import evaluate_cgp003
from engine.rules.composite.crk001_overall_risk import evaluate_crk001
from engine.rules.composite.crk002_volatility_risk import evaluate_crk002
from engine.rules.composite.crk003_gap_risk import evaluate_crk003
from engine.rules.composite.crk004_liquidity_risk import evaluate_crk004
from engine.rules.composite.crk005_position_risk import evaluate_crk005
from engine.rules.composite.cen001_entry_quality import evaluate_cen001
from engine.rules.composite.cen002_breakout_entry import evaluate_cen002
from engine.rules.composite.cen003_pullback_entry import evaluate_cen003
from engine.rules.composite.cen004_trend_entry import evaluate_cen004
from engine.rules.composite.cen005_entry_confirmation import evaluate_cen005
from engine.rules.composite.cex001_exit_quality import evaluate_cex001
from engine.rules.composite.cex002_stop_loss_exit import evaluate_cex002
from engine.rules.composite.cex003_target_exit import evaluate_cex003
from engine.rules.composite.cex004_trailing_exit import evaluate_cex004
from engine.rules.composite.cex005_exit_confirmation import evaluate_cex005
from engine.rules.composite.cmr001_bull_market import evaluate_cmr001
from engine.rules.composite.cmr002_bear_market import evaluate_cmr002
from engine.rules.composite.cmr003_sideways_market import evaluate_cmr003
from engine.rules.composite.cmr004_high_volatility_market import evaluate_cmr004
from engine.rules.composite.cmr005_low_volatility_market import evaluate_cmr005
from engine.rules.composite.cmt001_full_alignment import evaluate_cmt001
from engine.rules.composite.cmt002_partial_alignment import evaluate_cmt002
from engine.rules.composite.cmt003_timeframe_conflict import evaluate_cmt003
from engine.rules.composite.cmt004_higher_timeframe_agreement import evaluate_cmt004
from engine.rules.composite.cmt005_lower_timeframe_agreement import evaluate_cmt005
from engine.rules.composite.ccf001_trend_confirmation import evaluate_ccf001
from engine.rules.composite.ccf002_volume_confirmation import evaluate_ccf002
from engine.rules.composite.ccf003_momentum_confirmation import evaluate_ccf003
from engine.rules.composite.ccf004_breakout_confirmation import evaluate_ccf004
from engine.rules.composite.ccf005_full_confirmation import evaluate_ccf005
from engine.rules.composite.cdq001_data_integrity import evaluate_cdq001
from engine.rules.composite.cdq002_data_reliability import evaluate_cdq002

CompositeEvaluator = Callable[[dict[str, RuleResult]], RuleResult]

COMPOSITE_EVALUATORS: dict[str, CompositeEvaluator] = {
    "CTR001": evaluate_ctr001,
    "CTR002": evaluate_ctr002,
    "CTR003": evaluate_ctr003,
    "CTR004": evaluate_ctr004,
    "CTR005": evaluate_ctr005,
    "CTR006": evaluate_ctr006,
    "CTR007": evaluate_ctr007,
    "CTR008": evaluate_ctr008,
    "CTR009": evaluate_ctr009,
    "CTR010": evaluate_ctr010,
    "CMA001": evaluate_cma001,
    "CMA002": evaluate_cma002,
    "CMA003": evaluate_cma003,
    "CMA004": evaluate_cma004,
    "CMA005": evaluate_cma005,
    "CMA006": evaluate_cma006,
    "CMA007": evaluate_cma007,
    "CMA008": evaluate_cma008,
    "CMA009": evaluate_cma009,
    "CMA010": evaluate_cma010,
    "CPA001": evaluate_cpa001,
    "CPA002": evaluate_cpa002,
    "CPA003": evaluate_cpa003,
    "CPA004": evaluate_cpa004,
    "CPA005": evaluate_cpa005,
    "CPA006": evaluate_cpa006,
    "CPA007": evaluate_cpa007,
    "CPA008": evaluate_cpa008,
    "CPA009": evaluate_cpa009,
    "CPA010": evaluate_cpa010,
    "CVL001": evaluate_cvl001,
    "CVL002": evaluate_cvl002,
    "CVL003": evaluate_cvl003,
    "CVL004": evaluate_cvl004,
    "CVL005": evaluate_cvl005,
    "CVL006": evaluate_cvl006,
    "CVL007": evaluate_cvl007,
    "CVL008": evaluate_cvl008,
    "CVL009": evaluate_cvl009,
    "CVL010": evaluate_cvl010,
    "CMO001": evaluate_cmo001,
    "CMO002": evaluate_cmo002,
    "CMO003": evaluate_cmo003,
    "CMO004": evaluate_cmo004,
    "CMO005": evaluate_cmo005,
    "CMO006": evaluate_cmo006,
    "CMO007": evaluate_cmo007,
    "CMO008": evaluate_cmo008,
    "CMO009": evaluate_cmo009,
    "CMO010": evaluate_cmo010,
    "CVO001": evaluate_cvo001,
    "CVO002": evaluate_cvo002,
    "CVO003": evaluate_cvo003,
    "CVO004": evaluate_cvo004,
    "CVO005": evaluate_cvo005,
    "CVO006": evaluate_cvo006,
    "CVO007": evaluate_cvo007,
    "CVO008": evaluate_cvo008,
    "CVO009": evaluate_cvo009,
    "CVO010": evaluate_cvo010,
    "CMS001": evaluate_cms001,
    "CMS002": evaluate_cms002,
    "CMS003": evaluate_cms003,
    "CMS004": evaluate_cms004,
    "CMS005": evaluate_cms005,
    "CMS006": evaluate_cms006,
    "CMS007": evaluate_cms007,
    "CMS008": evaluate_cms008,
    "CMS009": evaluate_cms009,
    "CMS010": evaluate_cms010,
    "CSR001": evaluate_csr001,
    "CSR002": evaluate_csr002,
    "CSR003": evaluate_csr003,
    "CSR004": evaluate_csr004,
    "CSR005": evaluate_csr005,
    "CBO001": evaluate_cbo001,
    "CBO002": evaluate_cbo002,
    "CBO003": evaluate_cbo003,
    "CBO004": evaluate_cbo004,
    "CBO005": evaluate_cbo005,
    "CPB001": evaluate_cpb001,
    "CPB002": evaluate_cpb002,
    "CPB003": evaluate_cpb003,
    "CPB004": evaluate_cpb004,
    "CPB005": evaluate_cpb005,
    "CPT001": evaluate_cpt001,
    "CPT002": evaluate_cpt002,
    "CPT003": evaluate_cpt003,
    "CPT004": evaluate_cpt004,
    "CPT005": evaluate_cpt005,
    "CCS001": evaluate_ccs001,
    "CCS002": evaluate_ccs002,
    "CCS003": evaluate_ccs003,
    "CCS004": evaluate_ccs004,
    "CCS005": evaluate_ccs005,
    "CGP001": evaluate_cgp001,
    "CGP002": evaluate_cgp002,
    "CGP003": evaluate_cgp003,
    "CRK001": evaluate_crk001,
    "CRK002": evaluate_crk002,
    "CRK003": evaluate_crk003,
    "CRK004": evaluate_crk004,
    "CRK005": evaluate_crk005,
    "CEN001": evaluate_cen001,
    "CEN002": evaluate_cen002,
    "CEN003": evaluate_cen003,
    "CEN004": evaluate_cen004,
    "CEN005": evaluate_cen005,
    "CEX001": evaluate_cex001,
    "CEX002": evaluate_cex002,
    "CEX003": evaluate_cex003,
    "CEX004": evaluate_cex004,
    "CEX005": evaluate_cex005,
    "CMR001": evaluate_cmr001,
    "CMR002": evaluate_cmr002,
    "CMR003": evaluate_cmr003,
    "CMR004": evaluate_cmr004,
    "CMR005": evaluate_cmr005,
    "CMT001": evaluate_cmt001,
    "CMT002": evaluate_cmt002,
    "CMT003": evaluate_cmt003,
    "CMT004": evaluate_cmt004,
    "CMT005": evaluate_cmt005,
    "CCF001": evaluate_ccf001,
    "CCF002": evaluate_ccf002,
    "CCF003": evaluate_ccf003,
    "CCF004": evaluate_ccf004,
    "CCF005": evaluate_ccf005,
    "CDQ001": evaluate_cdq001,
    "CDQ002": evaluate_cdq002,
}


def evaluate_composite(rule_id: str, atomic: dict[str, RuleResult]) -> RuleResult:
    evaluator = COMPOSITE_EVALUATORS.get(rule_id)
    if evaluator is None:
        return RuleResult(
            rule_id=rule_id,
            verdict="UNKNOWN",
            status="UNKNOWN",
            score=0.0,
            reasons=[f"Composite rule not implemented: {rule_id}"],
            metadata={"not_implemented": True},
        )
    return evaluator(atomic)


def evaluate_composites(
    rule_ids: list[str], atomic: dict[str, RuleResult]
) -> dict[str, RuleResult]:
    return {rid: evaluate_composite(rid, atomic) for rid in rule_ids}


__all__ = [
    "COMPOSITE_EVALUATORS",
    "evaluate_composite",
    "evaluate_composites",
    "evaluate_ctr_rules",
]
