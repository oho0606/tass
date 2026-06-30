"""GP rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.gp.gp0001_gap_up_open_above_prior_high import evaluate_gp0001
from engine.rules.gp.gp0002_gap_up_open_above_prior_close import evaluate_gp0002
from engine.rules.gp.gp0003_gap_up_low_above_prior_high import evaluate_gp0003
from engine.rules.gp.gp0004_gap_up_low_above_prior_close import evaluate_gp0004
from engine.rules.gp.gp0005_gap_up_close_above_prior_high import evaluate_gp0005
from engine.rules.gp.gp0006_gap_up_close_above_prior_close import evaluate_gp0006
from engine.rules.gp.gp0007_gap_up_range_larger_than_prior_range import evaluate_gp0007
from engine.rules.gp.gp0008_gap_up_size_larger_than_prior_range import evaluate_gp0008
from engine.rules.gp.gp0009_gap_up_bar_bullish import evaluate_gp0009
from engine.rules.gp.gp0010_consecutive_gap_up_day import evaluate_gp0010
from engine.rules.gp.gp0011_gap_down_open_below_prior_low import evaluate_gp0011
from engine.rules.gp.gp0012_gap_down_open_below_prior_close import evaluate_gp0012
from engine.rules.gp.gp0013_gap_down_high_below_prior_low import evaluate_gp0013
from engine.rules.gp.gp0014_gap_down_high_below_prior_close import evaluate_gp0014
from engine.rules.gp.gp0015_gap_down_close_below_prior_low import evaluate_gp0015
from engine.rules.gp.gp0016_gap_down_close_below_prior_close import evaluate_gp0016
from engine.rules.gp.gp0017_gap_down_range_larger_than_prior_range import evaluate_gp0017
from engine.rules.gp.gp0018_gap_down_size_larger_than_prior_range import evaluate_gp0018
from engine.rules.gp.gp0019_gap_down_bar_bearish import evaluate_gp0019
from engine.rules.gp.gp0020_consecutive_gap_down_day import evaluate_gp0020
from engine.rules.gp.gp0021_breakaway_gap_up_open_above_n_period_high import evaluate_gp0021
from engine.rules.gp.gp0022_breakaway_gap_up_low_above_n_period_high import evaluate_gp0022
from engine.rules.gp.gp0023_breakaway_gap_down_open_below_n_period_low import evaluate_gp0023
from engine.rules.gp.gp0024_breakaway_gap_down_high_below_n_period_low import evaluate_gp0024
from engine.rules.gp.gp0025_breakaway_gap_up_open_outside_n_period_range import evaluate_gp0025
from engine.rules.gp.gp0026_breakaway_gap_down_open_outside_n_period_range import evaluate_gp0026
from engine.rules.gp.gp0027_breakaway_gap_up_size_exceeds_n_period_average_range import evaluate_gp0027
from engine.rules.gp.gp0028_breakaway_gap_down_size_exceeds_n_period_average_range import evaluate_gp0028
from engine.rules.gp.gp0029_breakaway_gap_up_volume_above_n_period_average import evaluate_gp0029
from engine.rules.gp.gp0030_breakaway_gap_down_volume_above_n_period_average import evaluate_gp0030
from engine.rules.gp.gp0031_continuation_gap_up_low_above_prior_high import evaluate_gp0031
from engine.rules.gp.gp0032_continuation_gap_up_unfilled_at_close import evaluate_gp0032
from engine.rules.gp.gp0033_continuation_gap_up_bar_bullish import evaluate_gp0033
from engine.rules.gp.gp0034_continuation_gap_up_size_below_n_period_average_gap import evaluate_gp0034
from engine.rules.gp.gp0035_continuation_gap_up_after_higher_close import evaluate_gp0035
from engine.rules.gp.gp0036_continuation_gap_down_high_below_prior_low import evaluate_gp0036
from engine.rules.gp.gp0037_continuation_gap_down_unfilled_at_close import evaluate_gp0037
from engine.rules.gp.gp0038_continuation_gap_down_bar_bearish import evaluate_gp0038
from engine.rules.gp.gp0039_continuation_gap_down_size_below_n_period_average_gap import evaluate_gp0039
from engine.rules.gp.gp0040_continuation_gap_down_after_lower_close import evaluate_gp0040
from engine.rules.gp.gp0041_exhaustion_gap_up_open_above_prior_high import evaluate_gp0041
from engine.rules.gp.gp0042_exhaustion_gap_up_filled_intraday import evaluate_gp0042
from engine.rules.gp.gp0043_exhaustion_gap_up_bar_bearish import evaluate_gp0043
from engine.rules.gp.gp0044_exhaustion_gap_up_at_n_period_high import evaluate_gp0044
from engine.rules.gp.gp0045_exhaustion_gap_up_size_exceeds_n_period_average_gap import evaluate_gp0045
from engine.rules.gp.gp0046_exhaustion_gap_down_open_below_prior_low import evaluate_gp0046
from engine.rules.gp.gp0047_exhaustion_gap_down_filled_intraday import evaluate_gp0047
from engine.rules.gp.gp0048_exhaustion_gap_down_bar_bullish import evaluate_gp0048
from engine.rules.gp.gp0049_exhaustion_gap_down_at_n_period_low import evaluate_gp0049
from engine.rules.gp.gp0050_exhaustion_gap_down_size_exceeds_n_period_average_gap import evaluate_gp0050
from engine.rules.gp.gp0051_gap_size_above_n_period_average import evaluate_gp0051
from engine.rules.gp.gp0052_gap_size_below_n_period_average import evaluate_gp0052
from engine.rules.gp.gp0053_gap_size_exceeds_prior_gap_size import evaluate_gp0053
from engine.rules.gp.gp0054_gap_size_below_prior_gap_size import evaluate_gp0054
from engine.rules.gp.gp0055_gap_unfilled_at_close import evaluate_gp0055
from engine.rules.gp.gp0056_gap_filled_intraday import evaluate_gp0056
from engine.rules.gp.gp0057_gap_partially_filled_intraday import evaluate_gp0057
from engine.rules.gp.gp0058_gap_volume_above_n_period_average import evaluate_gp0058
from engine.rules.gp.gp0059_gap_volume_below_n_period_average import evaluate_gp0059
from engine.rules.gp.gp0060_gap_range_above_n_period_average import evaluate_gp0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

GP_EVALUATORS: dict[str, RuleEvaluator] = {
    "GP0001": evaluate_gp0001,
    "GP0002": evaluate_gp0002,
    "GP0003": evaluate_gp0003,
    "GP0004": evaluate_gp0004,
    "GP0005": evaluate_gp0005,
    "GP0006": evaluate_gp0006,
    "GP0007": evaluate_gp0007,
    "GP0008": evaluate_gp0008,
    "GP0009": evaluate_gp0009,
    "GP0010": evaluate_gp0010,
    "GP0011": evaluate_gp0011,
    "GP0012": evaluate_gp0012,
    "GP0013": evaluate_gp0013,
    "GP0014": evaluate_gp0014,
    "GP0015": evaluate_gp0015,
    "GP0016": evaluate_gp0016,
    "GP0017": evaluate_gp0017,
    "GP0018": evaluate_gp0018,
    "GP0019": evaluate_gp0019,
    "GP0020": evaluate_gp0020,
    "GP0021": evaluate_gp0021,
    "GP0022": evaluate_gp0022,
    "GP0023": evaluate_gp0023,
    "GP0024": evaluate_gp0024,
    "GP0025": evaluate_gp0025,
    "GP0026": evaluate_gp0026,
    "GP0027": evaluate_gp0027,
    "GP0028": evaluate_gp0028,
    "GP0029": evaluate_gp0029,
    "GP0030": evaluate_gp0030,
    "GP0031": evaluate_gp0031,
    "GP0032": evaluate_gp0032,
    "GP0033": evaluate_gp0033,
    "GP0034": evaluate_gp0034,
    "GP0035": evaluate_gp0035,
    "GP0036": evaluate_gp0036,
    "GP0037": evaluate_gp0037,
    "GP0038": evaluate_gp0038,
    "GP0039": evaluate_gp0039,
    "GP0040": evaluate_gp0040,
    "GP0041": evaluate_gp0041,
    "GP0042": evaluate_gp0042,
    "GP0043": evaluate_gp0043,
    "GP0044": evaluate_gp0044,
    "GP0045": evaluate_gp0045,
    "GP0046": evaluate_gp0046,
    "GP0047": evaluate_gp0047,
    "GP0048": evaluate_gp0048,
    "GP0049": evaluate_gp0049,
    "GP0050": evaluate_gp0050,
    "GP0051": evaluate_gp0051,
    "GP0052": evaluate_gp0052,
    "GP0053": evaluate_gp0053,
    "GP0054": evaluate_gp0054,
    "GP0055": evaluate_gp0055,
    "GP0056": evaluate_gp0056,
    "GP0057": evaluate_gp0057,
    "GP0058": evaluate_gp0058,
    "GP0059": evaluate_gp0059,
    "GP0060": evaluate_gp0060,
}


def get_gp_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for GP rule ID."""
    return GP_EVALUATORS[rule_id]
