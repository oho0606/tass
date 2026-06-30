"""RK rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.rk.rk0001_atr_above_20_period_average import evaluate_rk0001
from engine.rules.rk.rk0002_atr_below_20_period_average import evaluate_rk0002
from engine.rules.rk.rk0003_atr_rising import evaluate_rk0003
from engine.rules.rk.rk0004_atr_falling import evaluate_rk0004
from engine.rules.rk.rk0005_atr_at_20_period_high import evaluate_rk0005
from engine.rules.rk.rk0006_atr_at_20_period_low import evaluate_rk0006
from engine.rules.rk.rk0007_atr_expanding import evaluate_rk0007
from engine.rules.rk.rk0008_atr_contracting import evaluate_rk0008
from engine.rules.rk.rk0009_true_range_above_atr import evaluate_rk0009
from engine.rules.rk.rk0010_true_range_below_atr import evaluate_rk0010
from engine.rules.rk.rk0011_historical_volatility_above_20_period_average import evaluate_rk0011
from engine.rules.rk.rk0012_historical_volatility_below_20_period_average import evaluate_rk0012
from engine.rules.rk.rk0013_historical_volatility_rising import evaluate_rk0013
from engine.rules.rk.rk0014_historical_volatility_falling import evaluate_rk0014
from engine.rules.rk.rk0015_bollinger_band_width_expanding import evaluate_rk0015
from engine.rules.rk.rk0016_bollinger_band_width_contracting import evaluate_rk0016
from engine.rules.rk.rk0017_daily_range_above_20_period_average import evaluate_rk0017
from engine.rules.rk.rk0018_daily_range_below_20_period_average import evaluate_rk0018
from engine.rules.rk.rk0019_close_to_close_volatility_above_20_period_average import evaluate_rk0019
from engine.rules.rk.rk0020_high_low_volatility_above_20_period_average import evaluate_rk0020
from engine.rules.rk.rk0021_overnight_gap_up_present import evaluate_rk0021
from engine.rules.rk.rk0022_overnight_gap_down_present import evaluate_rk0022
from engine.rules.rk.rk0023_gap_size_above_atr import evaluate_rk0023
from engine.rules.rk.rk0024_gap_size_below_atr import evaluate_rk0024
from engine.rules.rk.rk0025_unfilled_gap_up_present import evaluate_rk0025
from engine.rules.rk.rk0026_unfilled_gap_down_present import evaluate_rk0026
from engine.rules.rk.rk0027_gap_up_filled_same_session import evaluate_rk0027
from engine.rules.rk.rk0028_gap_down_filled_same_session import evaluate_rk0028
from engine.rules.rk.rk0029_gap_up_from_prior_high import evaluate_rk0029
from engine.rules.rk.rk0030_gap_down_from_prior_low import evaluate_rk0030
from engine.rules.rk.rk0031_volume_below_20_period_average import evaluate_rk0031
from engine.rules.rk.rk0032_volume_above_20_period_average import evaluate_rk0032
from engine.rules.rk.rk0033_bid_ask_spread_above_20_period_average import evaluate_rk0033
from engine.rules.rk.rk0034_bid_ask_spread_below_20_period_average import evaluate_rk0034
from engine.rules.rk.rk0035_turnover_below_20_period_average import evaluate_rk0035
from engine.rules.rk.rk0036_turnover_above_20_period_average import evaluate_rk0036
from engine.rules.rk.rk0037_volume_declining import evaluate_rk0037
from engine.rules.rk.rk0038_volume_increasing import evaluate_rk0038
from engine.rules.rk.rk0039_dollar_volume_below_20_period_average import evaluate_rk0039
from engine.rules.rk.rk0040_dollar_volume_above_20_period_average import evaluate_rk0040
from engine.rules.rk.rk0041_price_below_20_period_high import evaluate_rk0041
from engine.rules.rk.rk0042_price_at_20_period_low import evaluate_rk0042
from engine.rules.rk.rk0043_current_drawdown_above_10_percent import evaluate_rk0043
from engine.rules.rk.rk0044_current_drawdown_below_10_percent import evaluate_rk0044
from engine.rules.rk.rk0045_new_20_period_low_made import evaluate_rk0045
from engine.rules.rk.rk0046_new_20_period_high_made import evaluate_rk0046
from engine.rules.rk.rk0047_drawdown_increasing import evaluate_rk0047
from engine.rules.rk.rk0048_drawdown_decreasing import evaluate_rk0048
from engine.rules.rk.rk0049_price_underwater_from_peak import evaluate_rk0049
from engine.rules.rk.rk0050_price_above_prior_peak import evaluate_rk0050
from engine.rules.rk.rk0051_atr_near_20_period_average import evaluate_rk0051
from engine.rules.rk.rk0052_atr_extended_above_20_period_average import evaluate_rk0052
from engine.rules.rk.rk0053_atr_extended_below_20_period_average import evaluate_rk0053
from engine.rules.rk.rk0054_volatility_near_20_period_average import evaluate_rk0054
from engine.rules.rk.rk0055_volatility_extended_above_20_period_average import evaluate_rk0055
from engine.rules.rk.rk0056_volatility_extended_below_20_period_average import evaluate_rk0056
from engine.rules.rk.rk0057_volume_near_20_period_average import evaluate_rk0057
from engine.rules.rk.rk0058_drawdown_near_20_period_average import evaluate_rk0058
from engine.rules.rk.rk0059_gap_frequency_above_20_period_average import evaluate_rk0059
from engine.rules.rk.rk0060_risk_structure_stable import evaluate_rk0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

RK_EVALUATORS: dict[str, RuleEvaluator] = {
    "RK0001": evaluate_rk0001,
    "RK0002": evaluate_rk0002,
    "RK0003": evaluate_rk0003,
    "RK0004": evaluate_rk0004,
    "RK0005": evaluate_rk0005,
    "RK0006": evaluate_rk0006,
    "RK0007": evaluate_rk0007,
    "RK0008": evaluate_rk0008,
    "RK0009": evaluate_rk0009,
    "RK0010": evaluate_rk0010,
    "RK0011": evaluate_rk0011,
    "RK0012": evaluate_rk0012,
    "RK0013": evaluate_rk0013,
    "RK0014": evaluate_rk0014,
    "RK0015": evaluate_rk0015,
    "RK0016": evaluate_rk0016,
    "RK0017": evaluate_rk0017,
    "RK0018": evaluate_rk0018,
    "RK0019": evaluate_rk0019,
    "RK0020": evaluate_rk0020,
    "RK0021": evaluate_rk0021,
    "RK0022": evaluate_rk0022,
    "RK0023": evaluate_rk0023,
    "RK0024": evaluate_rk0024,
    "RK0025": evaluate_rk0025,
    "RK0026": evaluate_rk0026,
    "RK0027": evaluate_rk0027,
    "RK0028": evaluate_rk0028,
    "RK0029": evaluate_rk0029,
    "RK0030": evaluate_rk0030,
    "RK0031": evaluate_rk0031,
    "RK0032": evaluate_rk0032,
    "RK0033": evaluate_rk0033,
    "RK0034": evaluate_rk0034,
    "RK0035": evaluate_rk0035,
    "RK0036": evaluate_rk0036,
    "RK0037": evaluate_rk0037,
    "RK0038": evaluate_rk0038,
    "RK0039": evaluate_rk0039,
    "RK0040": evaluate_rk0040,
    "RK0041": evaluate_rk0041,
    "RK0042": evaluate_rk0042,
    "RK0043": evaluate_rk0043,
    "RK0044": evaluate_rk0044,
    "RK0045": evaluate_rk0045,
    "RK0046": evaluate_rk0046,
    "RK0047": evaluate_rk0047,
    "RK0048": evaluate_rk0048,
    "RK0049": evaluate_rk0049,
    "RK0050": evaluate_rk0050,
    "RK0051": evaluate_rk0051,
    "RK0052": evaluate_rk0052,
    "RK0053": evaluate_rk0053,
    "RK0054": evaluate_rk0054,
    "RK0055": evaluate_rk0055,
    "RK0056": evaluate_rk0056,
    "RK0057": evaluate_rk0057,
    "RK0058": evaluate_rk0058,
    "RK0059": evaluate_rk0059,
    "RK0060": evaluate_rk0060,
}


def get_rk_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for RK rule ID."""
    return RK_EVALUATORS[rule_id]
