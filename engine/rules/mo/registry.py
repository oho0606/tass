"""MO rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.mo.mo0001_rsi_above_70 import evaluate_mo0001
from engine.rules.mo.mo0002_rsi_below_30 import evaluate_mo0002
from engine.rules.mo.mo0003_rsi_above_50 import evaluate_mo0003
from engine.rules.mo.mo0004_rsi_below_50 import evaluate_mo0004
from engine.rules.mo.mo0005_rsi_rising import evaluate_mo0005
from engine.rules.mo.mo0006_rsi_falling import evaluate_mo0006
from engine.rules.mo.mo0007_rsi_cross_above_50 import evaluate_mo0007
from engine.rules.mo.mo0008_rsi_cross_below_50 import evaluate_mo0008
from engine.rules.mo.mo0009_rsi_cross_above_70 import evaluate_mo0009
from engine.rules.mo.mo0010_rsi_cross_below_30 import evaluate_mo0010
from engine.rules.mo.mo0011_macd_above_zero import evaluate_mo0011
from engine.rules.mo.mo0012_macd_below_zero import evaluate_mo0012
from engine.rules.mo.mo0013_macd_above_signal_line import evaluate_mo0013
from engine.rules.mo.mo0014_macd_below_signal_line import evaluate_mo0014
from engine.rules.mo.mo0015_macd_cross_above_signal import evaluate_mo0015
from engine.rules.mo.mo0016_macd_cross_below_signal import evaluate_mo0016
from engine.rules.mo.mo0017_macd_histogram_positive import evaluate_mo0017
from engine.rules.mo.mo0018_macd_histogram_negative import evaluate_mo0018
from engine.rules.mo.mo0019_macd_histogram_rising import evaluate_mo0019
from engine.rules.mo.mo0020_macd_histogram_falling import evaluate_mo0020
from engine.rules.mo.mo0021_stochastic_above_80 import evaluate_mo0021
from engine.rules.mo.mo0022_stochastic_below_20 import evaluate_mo0022
from engine.rules.mo.mo0023_stochastic_above_50 import evaluate_mo0023
from engine.rules.mo.mo0024_stochastic_below_50 import evaluate_mo0024
from engine.rules.mo.mo0025_stochastic_k_above_d import evaluate_mo0025
from engine.rules.mo.mo0026_stochastic_k_below_d import evaluate_mo0026
from engine.rules.mo.mo0027_stochastic_k_cross_above_d import evaluate_mo0027
from engine.rules.mo.mo0028_stochastic_k_cross_below_d import evaluate_mo0028
from engine.rules.mo.mo0029_stochastic_rising import evaluate_mo0029
from engine.rules.mo.mo0030_stochastic_falling import evaluate_mo0030
from engine.rules.mo.mo0031_cci_above_100 import evaluate_mo0031
from engine.rules.mo.mo0032_cci_below_negative_100 import evaluate_mo0032
from engine.rules.mo.mo0033_cci_above_zero import evaluate_mo0033
from engine.rules.mo.mo0034_cci_below_zero import evaluate_mo0034
from engine.rules.mo.mo0035_cci_rising import evaluate_mo0035
from engine.rules.mo.mo0036_cci_falling import evaluate_mo0036
from engine.rules.mo.mo0037_cci_cross_above_zero import evaluate_mo0037
from engine.rules.mo.mo0038_cci_cross_below_zero import evaluate_mo0038
from engine.rules.mo.mo0039_cci_cross_above_100 import evaluate_mo0039
from engine.rules.mo.mo0040_cci_cross_below_negative_100 import evaluate_mo0040
from engine.rules.mo.mo0041_mfi_above_80 import evaluate_mo0041
from engine.rules.mo.mo0042_mfi_below_20 import evaluate_mo0042
from engine.rules.mo.mo0043_mfi_above_50 import evaluate_mo0043
from engine.rules.mo.mo0044_mfi_below_50 import evaluate_mo0044
from engine.rules.mo.mo0045_mfi_rising import evaluate_mo0045
from engine.rules.mo.mo0046_mfi_falling import evaluate_mo0046
from engine.rules.mo.mo0047_mfi_cross_above_50 import evaluate_mo0047
from engine.rules.mo.mo0048_mfi_cross_below_50 import evaluate_mo0048
from engine.rules.mo.mo0049_mfi_cross_above_80 import evaluate_mo0049
from engine.rules.mo.mo0050_mfi_cross_below_20 import evaluate_mo0050
from engine.rules.mo.mo0051_rate_of_change_positive import evaluate_mo0051
from engine.rules.mo.mo0052_rate_of_change_negative import evaluate_mo0052
from engine.rules.mo.mo0053_rate_of_change_rising import evaluate_mo0053
from engine.rules.mo.mo0054_rate_of_change_falling import evaluate_mo0054
from engine.rules.mo.mo0055_rate_of_change_cross_above_zero import evaluate_mo0055
from engine.rules.mo.mo0056_rate_of_change_cross_below_zero import evaluate_mo0056
from engine.rules.mo.mo0057_momentum_above_zero import evaluate_mo0057
from engine.rules.mo.mo0058_momentum_below_zero import evaluate_mo0058
from engine.rules.mo.mo0059_momentum_rising import evaluate_mo0059
from engine.rules.mo.mo0060_momentum_falling import evaluate_mo0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

MO_EVALUATORS: dict[str, RuleEvaluator] = {
    "MO0001": evaluate_mo0001,
    "MO0002": evaluate_mo0002,
    "MO0003": evaluate_mo0003,
    "MO0004": evaluate_mo0004,
    "MO0005": evaluate_mo0005,
    "MO0006": evaluate_mo0006,
    "MO0007": evaluate_mo0007,
    "MO0008": evaluate_mo0008,
    "MO0009": evaluate_mo0009,
    "MO0010": evaluate_mo0010,
    "MO0011": evaluate_mo0011,
    "MO0012": evaluate_mo0012,
    "MO0013": evaluate_mo0013,
    "MO0014": evaluate_mo0014,
    "MO0015": evaluate_mo0015,
    "MO0016": evaluate_mo0016,
    "MO0017": evaluate_mo0017,
    "MO0018": evaluate_mo0018,
    "MO0019": evaluate_mo0019,
    "MO0020": evaluate_mo0020,
    "MO0021": evaluate_mo0021,
    "MO0022": evaluate_mo0022,
    "MO0023": evaluate_mo0023,
    "MO0024": evaluate_mo0024,
    "MO0025": evaluate_mo0025,
    "MO0026": evaluate_mo0026,
    "MO0027": evaluate_mo0027,
    "MO0028": evaluate_mo0028,
    "MO0029": evaluate_mo0029,
    "MO0030": evaluate_mo0030,
    "MO0031": evaluate_mo0031,
    "MO0032": evaluate_mo0032,
    "MO0033": evaluate_mo0033,
    "MO0034": evaluate_mo0034,
    "MO0035": evaluate_mo0035,
    "MO0036": evaluate_mo0036,
    "MO0037": evaluate_mo0037,
    "MO0038": evaluate_mo0038,
    "MO0039": evaluate_mo0039,
    "MO0040": evaluate_mo0040,
    "MO0041": evaluate_mo0041,
    "MO0042": evaluate_mo0042,
    "MO0043": evaluate_mo0043,
    "MO0044": evaluate_mo0044,
    "MO0045": evaluate_mo0045,
    "MO0046": evaluate_mo0046,
    "MO0047": evaluate_mo0047,
    "MO0048": evaluate_mo0048,
    "MO0049": evaluate_mo0049,
    "MO0050": evaluate_mo0050,
    "MO0051": evaluate_mo0051,
    "MO0052": evaluate_mo0052,
    "MO0053": evaluate_mo0053,
    "MO0054": evaluate_mo0054,
    "MO0055": evaluate_mo0055,
    "MO0056": evaluate_mo0056,
    "MO0057": evaluate_mo0057,
    "MO0058": evaluate_mo0058,
    "MO0059": evaluate_mo0059,
    "MO0060": evaluate_mo0060,
}


def get_mo_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for MO rule ID."""
    return MO_EVALUATORS[rule_id]
