"""Add run_sessions table for pipeline audit trail."""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op

revision = "002_run_sessions"
down_revision = "001_initial"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "run_sessions",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("session_id", sa.String(36), nullable=False, unique=True),
        sa.Column("run_date", sa.Date(), nullable=False, index=True),
        sa.Column("status", sa.String(20), nullable=False, server_default="running"),
        sa.Column("universe_size", sa.Integer(), nullable=True),
        sa.Column("candidates_evaluated", sa.Integer(), nullable=True),
        sa.Column("picks_count", sa.Integer(), nullable=True),
        sa.Column("elapsed_seconds", sa.Float(), nullable=True),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column(
            "started_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
        ),
        sa.Column("finished_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_run_sessions_date", "run_sessions", ["run_date"])


def downgrade() -> None:
    op.drop_index("ix_run_sessions_date", table_name="run_sessions")
    op.drop_table("run_sessions")
