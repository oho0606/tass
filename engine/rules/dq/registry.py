"""DQ rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.dq.dq0001_open_price_missing import evaluate_dq0001
from engine.rules.dq.dq0002_high_price_missing import evaluate_dq0002
from engine.rules.dq.dq0003_low_price_missing import evaluate_dq0003
from engine.rules.dq.dq0004_close_price_missing import evaluate_dq0004
from engine.rules.dq.dq0005_volume_missing import evaluate_dq0005
from engine.rules.dq.dq0006_ohlc_all_missing import evaluate_dq0006
from engine.rules.dq.dq0007_consecutive_missing_bar import evaluate_dq0007
from engine.rules.dq.dq0008_leading_history_gap import evaluate_dq0008
from engine.rules.dq.dq0009_internal_history_gap import evaluate_dq0009
from engine.rules.dq.dq0010_latest_bar_missing import evaluate_dq0010
from engine.rules.dq.dq0011_high_below_low import evaluate_dq0011
from engine.rules.dq.dq0012_close_outside_high_low_range import evaluate_dq0012
from engine.rules.dq.dq0013_open_outside_high_low_range import evaluate_dq0013
from engine.rules.dq.dq0014_negative_price_present import evaluate_dq0014
from engine.rules.dq.dq0015_zero_price_present import evaluate_dq0015
from engine.rules.dq.dq0016_negative_volume_present import evaluate_dq0016
from engine.rules.dq.dq0017_duplicate_timestamp import evaluate_dq0017
from engine.rules.dq.dq0018_identical_ohlc_values import evaluate_dq0018
from engine.rules.dq.dq0019_timestamp_out_of_sequence import evaluate_dq0019
from engine.rules.dq.dq0020_price_adjustment_mismatch import evaluate_dq0020
from engine.rules.dq.dq0021_stock_split_present import evaluate_dq0021
from engine.rules.dq.dq0022_reverse_split_present import evaluate_dq0022
from engine.rules.dq.dq0023_dividend_present import evaluate_dq0023
from engine.rules.dq.dq0024_rights_issue_present import evaluate_dq0024
from engine.rules.dq.dq0025_merger_present import evaluate_dq0025
from engine.rules.dq.dq0026_spinoff_present import evaluate_dq0026
from engine.rules.dq.dq0027_symbol_change_present import evaluate_dq0027
from engine.rules.dq.dq0028_delisting_event_present import evaluate_dq0028
from engine.rules.dq.dq0029_price_adjustment_applied import evaluate_dq0029
from engine.rules.dq.dq0030_price_unadjusted import evaluate_dq0030
from engine.rules.dq.dq0031_trading_halted import evaluate_dq0031
from engine.rules.dq.dq0032_trading_suspended import evaluate_dq0032
from engine.rules.dq.dq0033_delisted_instrument import evaluate_dq0033
from engine.rules.dq.dq0034_no_trade_session import evaluate_dq0034
from engine.rules.dq.dq0035_zero_volume_session import evaluate_dq0035
from engine.rules.dq.dq0036_low_volume_session import evaluate_dq0036
from engine.rules.dq.dq0037_low_liquidity_session import evaluate_dq0037
from engine.rules.dq.dq0038_wide_bid_ask_spread import evaluate_dq0038
from engine.rules.dq.dq0039_limit_up_lock import evaluate_dq0039
from engine.rules.dq.dq0040_limit_down_lock import evaluate_dq0040
from engine.rules.dq.dq0041_price_spike_present import evaluate_dq0041
from engine.rules.dq.dq0042_abnormal_price_gap import evaluate_dq0042
from engine.rules.dq.dq0043_volume_spike_present import evaluate_dq0043
from engine.rules.dq.dq0044_abnormal_return_present import evaluate_dq0044
from engine.rules.dq.dq0045_abnormal_range_present import evaluate_dq0045
from engine.rules.dq.dq0046_tick_size_violation import evaluate_dq0046
from engine.rules.dq.dq0047_stale_quote_present import evaluate_dq0047
from engine.rules.dq.dq0048_after_hours_trade_present import evaluate_dq0048
from engine.rules.dq.dq0049_erroneous_tick_present import evaluate_dq0049
from engine.rules.dq.dq0050_statistical_outlier_present import evaluate_dq0050
from engine.rules.dq.dq0051_required_history_present import evaluate_dq0051
from engine.rules.dq.dq0052_required_history_absent import evaluate_dq0052
from engine.rules.dq.dq0053_current_bar_present import evaluate_dq0053
from engine.rules.dq.dq0054_current_bar_absent import evaluate_dq0054
from engine.rules.dq.dq0055_session_data_complete import evaluate_dq0055
from engine.rules.dq.dq0056_session_data_incomplete import evaluate_dq0056
from engine.rules.dq.dq0057_data_feed_current import evaluate_dq0057
from engine.rules.dq.dq0058_data_feed_stale import evaluate_dq0058
from engine.rules.dq.dq0059_instrument_data_present import evaluate_dq0059
from engine.rules.dq.dq0060_instrument_data_absent import evaluate_dq0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

DQ_EVALUATORS: dict[str, RuleEvaluator] = {
    "DQ0001": evaluate_dq0001,
    "DQ0002": evaluate_dq0002,
    "DQ0003": evaluate_dq0003,
    "DQ0004": evaluate_dq0004,
    "DQ0005": evaluate_dq0005,
    "DQ0006": evaluate_dq0006,
    "DQ0007": evaluate_dq0007,
    "DQ0008": evaluate_dq0008,
    "DQ0009": evaluate_dq0009,
    "DQ0010": evaluate_dq0010,
    "DQ0011": evaluate_dq0011,
    "DQ0012": evaluate_dq0012,
    "DQ0013": evaluate_dq0013,
    "DQ0014": evaluate_dq0014,
    "DQ0015": evaluate_dq0015,
    "DQ0016": evaluate_dq0016,
    "DQ0017": evaluate_dq0017,
    "DQ0018": evaluate_dq0018,
    "DQ0019": evaluate_dq0019,
    "DQ0020": evaluate_dq0020,
    "DQ0021": evaluate_dq0021,
    "DQ0022": evaluate_dq0022,
    "DQ0023": evaluate_dq0023,
    "DQ0024": evaluate_dq0024,
    "DQ0025": evaluate_dq0025,
    "DQ0026": evaluate_dq0026,
    "DQ0027": evaluate_dq0027,
    "DQ0028": evaluate_dq0028,
    "DQ0029": evaluate_dq0029,
    "DQ0030": evaluate_dq0030,
    "DQ0031": evaluate_dq0031,
    "DQ0032": evaluate_dq0032,
    "DQ0033": evaluate_dq0033,
    "DQ0034": evaluate_dq0034,
    "DQ0035": evaluate_dq0035,
    "DQ0036": evaluate_dq0036,
    "DQ0037": evaluate_dq0037,
    "DQ0038": evaluate_dq0038,
    "DQ0039": evaluate_dq0039,
    "DQ0040": evaluate_dq0040,
    "DQ0041": evaluate_dq0041,
    "DQ0042": evaluate_dq0042,
    "DQ0043": evaluate_dq0043,
    "DQ0044": evaluate_dq0044,
    "DQ0045": evaluate_dq0045,
    "DQ0046": evaluate_dq0046,
    "DQ0047": evaluate_dq0047,
    "DQ0048": evaluate_dq0048,
    "DQ0049": evaluate_dq0049,
    "DQ0050": evaluate_dq0050,
    "DQ0051": evaluate_dq0051,
    "DQ0052": evaluate_dq0052,
    "DQ0053": evaluate_dq0053,
    "DQ0054": evaluate_dq0054,
    "DQ0055": evaluate_dq0055,
    "DQ0056": evaluate_dq0056,
    "DQ0057": evaluate_dq0057,
    "DQ0058": evaluate_dq0058,
    "DQ0059": evaluate_dq0059,
    "DQ0060": evaluate_dq0060,
}


def get_dq_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for DQ rule ID."""
    return DQ_EVALUATORS[rule_id]
