"""SR rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.sr.sr0001_price_above_horizontal_support import evaluate_sr0001
from engine.rules.sr.sr0002_price_below_horizontal_support import evaluate_sr0002
from engine.rules.sr.sr0003_price_at_horizontal_support import evaluate_sr0003
from engine.rules.sr.sr0004_price_near_horizontal_support import evaluate_sr0004
from engine.rules.sr.sr0005_price_touching_horizontal_support import evaluate_sr0005
from engine.rules.sr.sr0006_horizontal_support_level_identified import evaluate_sr0006
from engine.rules.sr.sr0007_prior_low_as_horizontal_support import evaluate_sr0007
from engine.rules.sr.sr0008_swing_low_as_horizontal_support import evaluate_sr0008
from engine.rules.sr.sr0009_n_period_low_as_horizontal_support import evaluate_sr0009
from engine.rules.sr.sr0010_price_crossing_above_horizontal_support import evaluate_sr0010
from engine.rules.sr.sr0011_price_above_horizontal_resistance import evaluate_sr0011
from engine.rules.sr.sr0012_price_below_horizontal_resistance import evaluate_sr0012
from engine.rules.sr.sr0013_price_at_horizontal_resistance import evaluate_sr0013
from engine.rules.sr.sr0014_price_near_horizontal_resistance import evaluate_sr0014
from engine.rules.sr.sr0015_price_touching_horizontal_resistance import evaluate_sr0015
from engine.rules.sr.sr0016_horizontal_resistance_level_identified import evaluate_sr0016
from engine.rules.sr.sr0017_prior_high_as_horizontal_resistance import evaluate_sr0017
from engine.rules.sr.sr0018_swing_high_as_horizontal_resistance import evaluate_sr0018
from engine.rules.sr.sr0019_n_period_high_as_horizontal_resistance import evaluate_sr0019
from engine.rules.sr.sr0020_price_crossing_below_horizontal_resistance import evaluate_sr0020
from engine.rules.sr.sr0021_price_above_dynamic_support import evaluate_sr0021
from engine.rules.sr.sr0022_price_below_dynamic_support import evaluate_sr0022
from engine.rules.sr.sr0023_price_at_dynamic_support import evaluate_sr0023
from engine.rules.sr.sr0024_price_near_dynamic_support import evaluate_sr0024
from engine.rules.sr.sr0025_price_touching_dynamic_support import evaluate_sr0025
from engine.rules.sr.sr0026_dynamic_support_present import evaluate_sr0026
from engine.rules.sr.sr0027_price_above_dynamic_resistance import evaluate_sr0027
from engine.rules.sr.sr0028_price_below_dynamic_resistance import evaluate_sr0028
from engine.rules.sr.sr0029_price_at_dynamic_resistance import evaluate_sr0029
from engine.rules.sr.sr0030_price_touching_dynamic_resistance import evaluate_sr0030
from engine.rules.sr.sr0031_price_above_pivot_point import evaluate_sr0031
from engine.rules.sr.sr0032_price_below_pivot_point import evaluate_sr0032
from engine.rules.sr.sr0033_price_at_pivot_point import evaluate_sr0033
from engine.rules.sr.sr0034_price_above_s1 import evaluate_sr0034
from engine.rules.sr.sr0035_price_below_s1 import evaluate_sr0035
from engine.rules.sr.sr0036_price_at_s1 import evaluate_sr0036
from engine.rules.sr.sr0037_price_above_r1 import evaluate_sr0037
from engine.rules.sr.sr0038_price_below_r1 import evaluate_sr0038
from engine.rules.sr.sr0039_price_at_r1 import evaluate_sr0039
from engine.rules.sr.sr0040_price_at_s2 import evaluate_sr0040
from engine.rules.sr.sr0041_price_above_fibonacci_23_6_level import evaluate_sr0041
from engine.rules.sr.sr0042_price_below_fibonacci_23_6_level import evaluate_sr0042
from engine.rules.sr.sr0043_price_at_fibonacci_23_6_level import evaluate_sr0043
from engine.rules.sr.sr0044_price_above_fibonacci_38_2_level import evaluate_sr0044
from engine.rules.sr.sr0045_price_below_fibonacci_38_2_level import evaluate_sr0045
from engine.rules.sr.sr0046_price_at_fibonacci_38_2_level import evaluate_sr0046
from engine.rules.sr.sr0047_price_above_fibonacci_50_0_level import evaluate_sr0047
from engine.rules.sr.sr0048_price_below_fibonacci_50_0_level import evaluate_sr0048
from engine.rules.sr.sr0049_price_at_fibonacci_50_0_level import evaluate_sr0049
from engine.rules.sr.sr0050_price_at_fibonacci_61_8_level import evaluate_sr0050
from engine.rules.sr.sr0051_support_level_first_touch import evaluate_sr0051
from engine.rules.sr.sr0052_support_level_second_touch import evaluate_sr0052
from engine.rules.sr.sr0053_support_level_multiple_touches import evaluate_sr0053
from engine.rules.sr.sr0054_resistance_level_first_touch import evaluate_sr0054
from engine.rules.sr.sr0055_resistance_level_second_touch import evaluate_sr0055
from engine.rules.sr.sr0056_resistance_level_multiple_touches import evaluate_sr0056
from engine.rules.sr.sr0057_support_level_holding import evaluate_sr0057
from engine.rules.sr.sr0058_resistance_level_holding import evaluate_sr0058
from engine.rules.sr.sr0059_confluent_support_levels_present import evaluate_sr0059
from engine.rules.sr.sr0060_confluent_resistance_levels_present import evaluate_sr0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

SR_EVALUATORS: dict[str, RuleEvaluator] = {
    "SR0001": evaluate_sr0001,
    "SR0002": evaluate_sr0002,
    "SR0003": evaluate_sr0003,
    "SR0004": evaluate_sr0004,
    "SR0005": evaluate_sr0005,
    "SR0006": evaluate_sr0006,
    "SR0007": evaluate_sr0007,
    "SR0008": evaluate_sr0008,
    "SR0009": evaluate_sr0009,
    "SR0010": evaluate_sr0010,
    "SR0011": evaluate_sr0011,
    "SR0012": evaluate_sr0012,
    "SR0013": evaluate_sr0013,
    "SR0014": evaluate_sr0014,
    "SR0015": evaluate_sr0015,
    "SR0016": evaluate_sr0016,
    "SR0017": evaluate_sr0017,
    "SR0018": evaluate_sr0018,
    "SR0019": evaluate_sr0019,
    "SR0020": evaluate_sr0020,
    "SR0021": evaluate_sr0021,
    "SR0022": evaluate_sr0022,
    "SR0023": evaluate_sr0023,
    "SR0024": evaluate_sr0024,
    "SR0025": evaluate_sr0025,
    "SR0026": evaluate_sr0026,
    "SR0027": evaluate_sr0027,
    "SR0028": evaluate_sr0028,
    "SR0029": evaluate_sr0029,
    "SR0030": evaluate_sr0030,
    "SR0031": evaluate_sr0031,
    "SR0032": evaluate_sr0032,
    "SR0033": evaluate_sr0033,
    "SR0034": evaluate_sr0034,
    "SR0035": evaluate_sr0035,
    "SR0036": evaluate_sr0036,
    "SR0037": evaluate_sr0037,
    "SR0038": evaluate_sr0038,
    "SR0039": evaluate_sr0039,
    "SR0040": evaluate_sr0040,
    "SR0041": evaluate_sr0041,
    "SR0042": evaluate_sr0042,
    "SR0043": evaluate_sr0043,
    "SR0044": evaluate_sr0044,
    "SR0045": evaluate_sr0045,
    "SR0046": evaluate_sr0046,
    "SR0047": evaluate_sr0047,
    "SR0048": evaluate_sr0048,
    "SR0049": evaluate_sr0049,
    "SR0050": evaluate_sr0050,
    "SR0051": evaluate_sr0051,
    "SR0052": evaluate_sr0052,
    "SR0053": evaluate_sr0053,
    "SR0054": evaluate_sr0054,
    "SR0055": evaluate_sr0055,
    "SR0056": evaluate_sr0056,
    "SR0057": evaluate_sr0057,
    "SR0058": evaluate_sr0058,
    "SR0059": evaluate_sr0059,
    "SR0060": evaluate_sr0060,
}


def get_sr_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for SR rule ID."""
    return SR_EVALUATORS[rule_id]
