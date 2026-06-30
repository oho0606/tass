"""MA rule evaluator registry."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma.ma0001_price_above_sma5 import evaluate_ma0001
from engine.rules.ma.ma0002_price_above_sma20 import evaluate_ma0002
from engine.rules.ma.ma0003_price_above_sma60 import evaluate_ma0003
from engine.rules.ma.ma0004_price_above_sma120 import evaluate_ma0004
from engine.rules.ma.ma0005_price_above_sma240 import evaluate_ma0005
from engine.rules.ma.ma0006_price_below_sma5 import evaluate_ma0006
from engine.rules.ma.ma0007_price_below_sma20 import evaluate_ma0007
from engine.rules.ma.ma0008_price_below_sma60 import evaluate_ma0008
from engine.rules.ma.ma0009_price_below_sma120 import evaluate_ma0009
from engine.rules.ma.ma0010_price_below_sma240 import evaluate_ma0010
from engine.rules.ma.ma0011_price_above_ema5 import evaluate_ma0011
from engine.rules.ma.ma0012_price_above_ema20 import evaluate_ma0012
from engine.rules.ma.ma0013_price_above_ema60 import evaluate_ma0013
from engine.rules.ma.ma0014_price_above_ema120 import evaluate_ma0014
from engine.rules.ma.ma0015_price_above_ema240 import evaluate_ma0015
from engine.rules.ma.ma0016_price_below_ema5 import evaluate_ma0016
from engine.rules.ma.ma0017_price_below_ema20 import evaluate_ma0017
from engine.rules.ma.ma0018_price_below_ema60 import evaluate_ma0018
from engine.rules.ma.ma0019_price_below_ema120 import evaluate_ma0019
from engine.rules.ma.ma0020_price_below_ema240 import evaluate_ma0020
from engine.rules.ma.ma0021_sma_bullish_alignment import evaluate_ma0021
from engine.rules.ma.ma0022_sma_bearish_alignment import evaluate_ma0022
from engine.rules.ma.ma0023_ema_bullish_alignment import evaluate_ma0023
from engine.rules.ma.ma0024_ema_bearish_alignment import evaluate_ma0024
from engine.rules.ma.ma0025_sma_alignment_improving import evaluate_ma0025
from engine.rules.ma.ma0026_sma_alignment_weakening import evaluate_ma0026
from engine.rules.ma.ma0027_ema_alignment_improving import evaluate_ma0027
from engine.rules.ma.ma0028_ema_alignment_weakening import evaluate_ma0028
from engine.rules.ma.ma0029_full_bullish_alignment import evaluate_ma0029
from engine.rules.ma.ma0030_full_bearish_alignment import evaluate_ma0030
from engine.rules.ma.ma0031_sma_golden_cross import evaluate_ma0031
from engine.rules.ma.ma0032_sma_death_cross import evaluate_ma0032
from engine.rules.ma.ma0033_ema_golden_cross import evaluate_ma0033
from engine.rules.ma.ma0034_ema_death_cross import evaluate_ma0034
from engine.rules.ma.ma0035_short_ma_cross_above_mid_ma import evaluate_ma0035
from engine.rules.ma.ma0036_short_ma_cross_below_mid_ma import evaluate_ma0036
from engine.rules.ma.ma0037_mid_ma_cross_above_long_ma import evaluate_ma0037
from engine.rules.ma.ma0038_mid_ma_cross_below_long_ma import evaluate_ma0038
from engine.rules.ma.ma0039_multiple_golden_cross import evaluate_ma0039
from engine.rules.ma.ma0040_multiple_death_cross import evaluate_ma0040
from engine.rules.ma.ma0041_sma_rising import evaluate_ma0041
from engine.rules.ma.ma0042_sma_falling import evaluate_ma0042
from engine.rules.ma.ma0043_ema_rising import evaluate_ma0043
from engine.rules.ma.ma0044_ema_falling import evaluate_ma0044
from engine.rules.ma.ma0045_sma_slope_increasing import evaluate_ma0045
from engine.rules.ma.ma0046_sma_slope_decreasing import evaluate_ma0046
from engine.rules.ma.ma0047_ema_slope_increasing import evaluate_ma0047
from engine.rules.ma.ma0048_ema_slope_decreasing import evaluate_ma0048
from engine.rules.ma.ma0049_moving_average_flat import evaluate_ma0049
from engine.rules.ma.ma0050_moving_average_turning import evaluate_ma0050
from engine.rules.ma.ma0051_price_extended_above_ma import evaluate_ma0051
from engine.rules.ma.ma0052_price_extended_below_ma import evaluate_ma0052
from engine.rules.ma.ma0053_price_near_moving_average import evaluate_ma0053
from engine.rules.ma.ma0054_moving_average_compression import evaluate_ma0054
from engine.rules.ma.ma0055_moving_average_expansion import evaluate_ma0055
from engine.rules.ma.ma0056_moving_average_convergence import evaluate_ma0056
from engine.rules.ma.ma0057_moving_average_divergence import evaluate_ma0057
from engine.rules.ma.ma0058_dynamic_support_holding import evaluate_ma0058
from engine.rules.ma.ma0059_dynamic_resistance_holding import evaluate_ma0059
from engine.rules.ma.ma0060_moving_average_structure_stable import evaluate_ma0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

MA_EVALUATORS: dict[str, RuleEvaluator] = {
    "MA0001": evaluate_ma0001,
    "MA0002": evaluate_ma0002,
    "MA0003": evaluate_ma0003,
    "MA0004": evaluate_ma0004,
    "MA0005": evaluate_ma0005,
    "MA0006": evaluate_ma0006,
    "MA0007": evaluate_ma0007,
    "MA0008": evaluate_ma0008,
    "MA0009": evaluate_ma0009,
    "MA0010": evaluate_ma0010,
    "MA0011": evaluate_ma0011,
    "MA0012": evaluate_ma0012,
    "MA0013": evaluate_ma0013,
    "MA0014": evaluate_ma0014,
    "MA0015": evaluate_ma0015,
    "MA0016": evaluate_ma0016,
    "MA0017": evaluate_ma0017,
    "MA0018": evaluate_ma0018,
    "MA0019": evaluate_ma0019,
    "MA0020": evaluate_ma0020,
    "MA0021": evaluate_ma0021,
    "MA0022": evaluate_ma0022,
    "MA0023": evaluate_ma0023,
    "MA0024": evaluate_ma0024,
    "MA0025": evaluate_ma0025,
    "MA0026": evaluate_ma0026,
    "MA0027": evaluate_ma0027,
    "MA0028": evaluate_ma0028,
    "MA0029": evaluate_ma0029,
    "MA0030": evaluate_ma0030,
    "MA0031": evaluate_ma0031,
    "MA0032": evaluate_ma0032,
    "MA0033": evaluate_ma0033,
    "MA0034": evaluate_ma0034,
    "MA0035": evaluate_ma0035,
    "MA0036": evaluate_ma0036,
    "MA0037": evaluate_ma0037,
    "MA0038": evaluate_ma0038,
    "MA0039": evaluate_ma0039,
    "MA0040": evaluate_ma0040,
    "MA0041": evaluate_ma0041,
    "MA0042": evaluate_ma0042,
    "MA0043": evaluate_ma0043,
    "MA0044": evaluate_ma0044,
    "MA0045": evaluate_ma0045,
    "MA0046": evaluate_ma0046,
    "MA0047": evaluate_ma0047,
    "MA0048": evaluate_ma0048,
    "MA0049": evaluate_ma0049,
    "MA0050": evaluate_ma0050,
    "MA0051": evaluate_ma0051,
    "MA0052": evaluate_ma0052,
    "MA0053": evaluate_ma0053,
    "MA0054": evaluate_ma0054,
    "MA0055": evaluate_ma0055,
    "MA0056": evaluate_ma0056,
    "MA0057": evaluate_ma0057,
    "MA0058": evaluate_ma0058,
    "MA0059": evaluate_ma0059,
    "MA0060": evaluate_ma0060,
}

MA_ENGINE_RULES: tuple[str, ...] = (
    "MA0002",
    "MA0003",
    "MA0007",
    "MA0012",
    "MA0021",
    "MA0029",
)

MA_ENGINE_WEIGHTS: dict[str, float] = {
    "MA0002": 1.2,
    "MA0003": 1.1,
    "MA0007": 0.9,
    "MA0012": 1.1,
    "MA0021": 1.3,
    "MA0029": 1.4,
}


def get_ma_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for MA rule ID."""
    return MA_EVALUATORS[rule_id]
