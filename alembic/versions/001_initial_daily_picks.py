"""Initial picks persistence schema."""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

revision = "001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "daily_picks",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("pick_date", sa.Date(), nullable=False, index=True),
        sa.Column("symbol", sa.String(12), nullable=False),
        sa.Column("rank", sa.Integer(), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index("ix_daily_picks_date_rank", "daily_picks", ["pick_date", "rank"])


def downgrade() -> None:
    op.drop_index("ix_daily_picks_date_rank", table_name="daily_picks")
    op.drop_table("daily_picks")
