"""Score normalization helpers for Recommendation Engine v1.0."""

from __future__ import annotations

from dataclasses import replace

from engine.core.types import MasterScoreResult, ProbabilityResult
from engine.probability import compute_probability

FULL_SCALE_MAX = 1000.0


def normalized_master_score(master: MasterScoreResult) -> float:
    if not master.mvp_mode and master.max_score >= FULL_SCALE_MAX:
        return master.total_score
    return master.total_score * (FULL_SCALE_MAX / master.max_score)


def normalized_probability(master: MasterScoreResult, probability: ProbabilityResult) -> float:
    if not master.mvp_mode and master.max_score >= FULL_SCALE_MAX:
        return probability.winning_probability
    normalized_master = replace(
        master,
        total_score=normalized_master_score(master),
        max_score=FULL_SCALE_MAX,
        mvp_mode=False,
    )
    return compute_probability(normalized_master).winning_probability
