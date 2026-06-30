"""Unit tests for Probability Engine v1.0."""

from __future__ import annotations

from dataclasses import replace

from engine.core.types import MasterScoreResult
from engine.probability import compute_probability
from engine.probability.calibration import CalibrationConfig
from engine.probability.mapping import DEFAULT_SCORE_BUCKETS, find_bucket, level_from_probability
from engine.probability.probability_engine import ProbabilityEngineConfig


def _master(score: float) -> MasterScoreResult:
    return MasterScoreResult(
        total_score=score,
        max_score=1000.0,
        mvp_mode=False,
        domains={},
    )


def test_same_score_same_probability():
    first = compute_probability(_master(875.0))
    second = compute_probability(_master(875.0))
    assert first == second


def test_score_bucket_990_to_1000():
    result = compute_probability(_master(995.0))
    assert 95.0 <= result.winning_probability <= 99.0
    assert result.probability_grade == "Exceptional"
    assert result.score_bucket_min == 990.0


def test_score_bucket_950_to_989():
    result = compute_probability(_master(970.0))
    assert 90.0 <= result.winning_probability <= 94.0
    assert result.probability_grade == "Excellent"


def test_score_bucket_900_to_949():
    result = compute_probability(_master(925.0))
    assert 82.0 <= result.winning_probability <= 89.0
    assert result.probability_grade == "Strong"


def test_score_bucket_850_to_899():
    result = compute_probability(_master(875.0))
    assert 74.0 <= result.winning_probability <= 81.0
    assert result.probability_grade == "Good"


def test_score_bucket_800_to_849():
    result = compute_probability(_master(825.0))
    assert 66.0 <= result.winning_probability <= 73.0
    assert result.probability_grade == "Average"


def test_score_bucket_750_to_799():
    result = compute_probability(_master(775.0))
    assert 58.0 <= result.winning_probability <= 65.0
    assert result.probability_grade == "Average"


def test_score_bucket_700_to_749():
    result = compute_probability(_master(725.0))
    assert 50.0 <= result.winning_probability <= 57.0
    assert result.probability_grade == "Weak"


def test_score_bucket_650_to_699():
    result = compute_probability(_master(675.0))
    assert 42.0 <= result.winning_probability <= 49.0
    assert result.probability_grade == "Reject"


def test_score_bucket_600_to_649():
    result = compute_probability(_master(625.0))
    assert 35.0 <= result.winning_probability <= 41.0
    assert result.probability_grade == "Reject"


def test_score_below_600():
    result = compute_probability(_master(300.0))
    assert result.winning_probability < 35.0
    assert result.probability_grade == "Reject"


def test_explainability_fields():
    result = compute_probability(_master(920.0))
    assert result.master_score == 920.0
    assert result.historical_win_rate > 0
    assert result.sample_size > 0
    assert result.calibration_version == "1.0"
    assert result.last_calibration_date
    assert result.confidence_interval.lower <= result.winning_probability
    assert result.confidence_interval.upper >= result.winning_probability
    assert len(result.reasons) >= 3


def test_accepts_raw_float():
    result = compute_probability(920.0)
    assert result.master_score == 920.0


def test_clamps_out_of_range_scores():
    low = compute_probability(_master(-50.0))
    high = compute_probability(_master(1500.0))
    assert low.master_score == 0.0
    assert high.master_score == 1000.0


def test_level_boundaries():
    assert level_from_probability(95.0).label == "Exceptional"
    assert level_from_probability(94.9).label == "Excellent"
    assert level_from_probability(90.0).label == "Excellent"
    assert level_from_probability(89.9).label == "Strong"
    assert level_from_probability(49.9).label == "Reject"


def test_custom_calibration_config():
    custom = CalibrationConfig(
        version="1.1-test",
        buckets=(replace(DEFAULT_SCORE_BUCKETS[0], historical_win_rate=96.0, sample_size=99), *DEFAULT_SCORE_BUCKETS[1:]),
    )
    result = compute_probability(
        _master(995.0),
        config=ProbabilityEngineConfig(calibration=custom),
    )
    assert result.calibration_version == "1.1-test"
    assert result.historical_win_rate == 96.0
    assert result.sample_size == 99


def test_find_bucket_covers_full_range():
    for score in (0, 300, 600, 700, 800, 900, 950, 1000):
        bucket = find_bucket(score, DEFAULT_SCORE_BUCKETS)
        assert bucket.min_score <= score <= bucket.max_score
