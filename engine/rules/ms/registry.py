"""MS rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ms.ms0001_higher_high_formed import evaluate_ms0001
from engine.rules.ms.ms0002_higher_high_confirmed import evaluate_ms0002
from engine.rules.ms.ms0003_higher_high_exceeds_prior import evaluate_ms0003
from engine.rules.ms.ms0004_higher_high_active import evaluate_ms0004
from engine.rules.ms.ms0005_consecutive_higher_high import evaluate_ms0005
from engine.rules.ms.ms0006_higher_low_formed import evaluate_ms0006
from engine.rules.ms.ms0007_higher_low_confirmed import evaluate_ms0007
from engine.rules.ms.ms0008_higher_low_exceeds_prior import evaluate_ms0008
from engine.rules.ms.ms0009_higher_low_active import evaluate_ms0009
from engine.rules.ms.ms0010_consecutive_higher_low import evaluate_ms0010
from engine.rules.ms.ms0011_lower_high_formed import evaluate_ms0011
from engine.rules.ms.ms0012_lower_high_confirmed import evaluate_ms0012
from engine.rules.ms.ms0013_lower_high_below_prior import evaluate_ms0013
from engine.rules.ms.ms0014_lower_high_active import evaluate_ms0014
from engine.rules.ms.ms0015_consecutive_lower_high import evaluate_ms0015
from engine.rules.ms.ms0016_lower_low_formed import evaluate_ms0016
from engine.rules.ms.ms0017_lower_low_confirmed import evaluate_ms0017
from engine.rules.ms.ms0018_lower_low_below_prior import evaluate_ms0018
from engine.rules.ms.ms0019_lower_low_active import evaluate_ms0019
from engine.rules.ms.ms0020_consecutive_lower_low import evaluate_ms0020
from engine.rules.ms.ms0021_swing_high_formed import evaluate_ms0021
from engine.rules.ms.ms0022_swing_low_formed import evaluate_ms0022
from engine.rules.ms.ms0023_swing_high_confirmed import evaluate_ms0023
from engine.rules.ms.ms0024_swing_low_confirmed import evaluate_ms0024
from engine.rules.ms.ms0025_swing_high_active import evaluate_ms0025
from engine.rules.ms.ms0026_swing_low_active import evaluate_ms0026
from engine.rules.ms.ms0027_recent_swing_high import evaluate_ms0027
from engine.rules.ms.ms0028_recent_swing_low import evaluate_ms0028
from engine.rules.ms.ms0029_equal_swing_high import evaluate_ms0029
from engine.rules.ms.ms0030_equal_swing_low import evaluate_ms0030
from engine.rules.ms.ms0031_bullish_break_of_structure import evaluate_ms0031
from engine.rules.ms.ms0032_bearish_break_of_structure import evaluate_ms0032
from engine.rules.ms.ms0033_bos_above_swing_high import evaluate_ms0033
from engine.rules.ms.ms0034_bos_below_swing_low import evaluate_ms0034
from engine.rules.ms.ms0035_bullish_bos_with_close import evaluate_ms0035
from engine.rules.ms.ms0036_bearish_bos_with_close import evaluate_ms0036
from engine.rules.ms.ms0037_bullish_bos_on_current_bar import evaluate_ms0037
from engine.rules.ms.ms0038_bearish_bos_on_current_bar import evaluate_ms0038
from engine.rules.ms.ms0039_price_above_bos_level import evaluate_ms0039
from engine.rules.ms.ms0040_price_below_bos_level import evaluate_ms0040
from engine.rules.ms.ms0041_bullish_change_of_character import evaluate_ms0041
from engine.rules.ms.ms0042_bearish_change_of_character import evaluate_ms0042
from engine.rules.ms.ms0043_choch_above_lower_high import evaluate_ms0043
from engine.rules.ms.ms0044_choch_below_higher_low import evaluate_ms0044
from engine.rules.ms.ms0045_bullish_choch_with_close import evaluate_ms0045
from engine.rules.ms.ms0046_bearish_choch_with_close import evaluate_ms0046
from engine.rules.ms.ms0047_bullish_choch_on_current_bar import evaluate_ms0047
from engine.rules.ms.ms0048_bearish_choch_on_current_bar import evaluate_ms0048
from engine.rules.ms.ms0049_price_above_choch_level import evaluate_ms0049
from engine.rules.ms.ms0050_price_below_choch_level import evaluate_ms0050
from engine.rules.ms.ms0051_swing_spacing_narrow import evaluate_ms0051
from engine.rules.ms.ms0052_swing_spacing_wide import evaluate_ms0052
from engine.rules.ms.ms0053_swing_overlap_present import evaluate_ms0053
from engine.rules.ms.ms0054_swing_overlap_absent import evaluate_ms0054
from engine.rules.ms.ms0055_structure_leg_extended import evaluate_ms0055
from engine.rules.ms.ms0056_structure_leg_compressed import evaluate_ms0056
from engine.rules.ms.ms0057_equal_highs_in_structure import evaluate_ms0057
from engine.rules.ms.ms0058_equal_lows_in_structure import evaluate_ms0058
from engine.rules.ms.ms0059_internal_swing_present import evaluate_ms0059
from engine.rules.ms.ms0060_external_swing_present import evaluate_ms0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

MS_EVALUATORS: dict[str, RuleEvaluator] = {
    "MS0001": evaluate_ms0001,
    "MS0002": evaluate_ms0002,
    "MS0003": evaluate_ms0003,
    "MS0004": evaluate_ms0004,
    "MS0005": evaluate_ms0005,
    "MS0006": evaluate_ms0006,
    "MS0007": evaluate_ms0007,
    "MS0008": evaluate_ms0008,
    "MS0009": evaluate_ms0009,
    "MS0010": evaluate_ms0010,
    "MS0011": evaluate_ms0011,
    "MS0012": evaluate_ms0012,
    "MS0013": evaluate_ms0013,
    "MS0014": evaluate_ms0014,
    "MS0015": evaluate_ms0015,
    "MS0016": evaluate_ms0016,
    "MS0017": evaluate_ms0017,
    "MS0018": evaluate_ms0018,
    "MS0019": evaluate_ms0019,
    "MS0020": evaluate_ms0020,
    "MS0021": evaluate_ms0021,
    "MS0022": evaluate_ms0022,
    "MS0023": evaluate_ms0023,
    "MS0024": evaluate_ms0024,
    "MS0025": evaluate_ms0025,
    "MS0026": evaluate_ms0026,
    "MS0027": evaluate_ms0027,
    "MS0028": evaluate_ms0028,
    "MS0029": evaluate_ms0029,
    "MS0030": evaluate_ms0030,
    "MS0031": evaluate_ms0031,
    "MS0032": evaluate_ms0032,
    "MS0033": evaluate_ms0033,
    "MS0034": evaluate_ms0034,
    "MS0035": evaluate_ms0035,
    "MS0036": evaluate_ms0036,
    "MS0037": evaluate_ms0037,
    "MS0038": evaluate_ms0038,
    "MS0039": evaluate_ms0039,
    "MS0040": evaluate_ms0040,
    "MS0041": evaluate_ms0041,
    "MS0042": evaluate_ms0042,
    "MS0043": evaluate_ms0043,
    "MS0044": evaluate_ms0044,
    "MS0045": evaluate_ms0045,
    "MS0046": evaluate_ms0046,
    "MS0047": evaluate_ms0047,
    "MS0048": evaluate_ms0048,
    "MS0049": evaluate_ms0049,
    "MS0050": evaluate_ms0050,
    "MS0051": evaluate_ms0051,
    "MS0052": evaluate_ms0052,
    "MS0053": evaluate_ms0053,
    "MS0054": evaluate_ms0054,
    "MS0055": evaluate_ms0055,
    "MS0056": evaluate_ms0056,
    "MS0057": evaluate_ms0057,
    "MS0058": evaluate_ms0058,
    "MS0059": evaluate_ms0059,
    "MS0060": evaluate_ms0060,
}


def get_ms_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for MS rule ID."""
    return MS_EVALUATORS[rule_id]
