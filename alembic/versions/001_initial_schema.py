"""Initial schema: daily_picks and run_sessions tables.

Revision ID: 001
Revises:
Create Date: 2026-06-30
"""
from __future__ import annotations

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "daily_picks",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("pick_date", sa.Date(), nullable=False),
        sa.Column("symbol", sa.String(12), nullable=False),
        sa.Column("rank", sa.Integer(), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_daily_picks_pick_date", "daily_picks", ["pick_date"])
    op.create_index("ix_daily_picks_date_rank", "daily_picks", ["pick_date", "rank"])

    op.create_table(
        "run_sessions",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("session_id", sa.String(36), nullable=False),
        sa.Column("run_date", sa.Date(), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        sa.Column("universe_size", sa.Integer(), nullable=True),
        sa.Column("candidates_evaluated", sa.Integer(), nullable=True),
        sa.Column("picks_count", sa.Integer(), nullable=True),
        sa.Column("elapsed_seconds", sa.Float(), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column(
            "started_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("session_id"),
    )
    op.create_index("ix_run_sessions_date", "run_sessions", ["run_date"])


def downgrade() -> None:
    op.drop_index("ix_run_sessions_date", table_name="run_sessions")
    op.drop_table("run_sessions")
    op.drop_index("ix_daily_picks_date_rank", table_name="daily_picks")
    op.drop_index("ix_daily_picks_pick_date", table_name="daily_picks")
    op.drop_table("daily_picks")
