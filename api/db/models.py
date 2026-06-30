"""SQLAlchemy ORM models for TASS persistence."""

from __future__ import annotations

try:
    import sqlalchemy as sa
    from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

    class Base(DeclarativeBase):
        pass

    class DailyPickRow(Base):
        """One ranked pick for a trading day."""

        __tablename__ = "daily_picks"

        id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
        pick_date: Mapped[sa.Date] = mapped_column(sa.Date, nullable=False, index=True)
        symbol: Mapped[str] = mapped_column(sa.String(12), nullable=False)
        rank: Mapped[int] = mapped_column(sa.Integer, nullable=False)
        payload: Mapped[dict] = mapped_column(sa.JSON, nullable=False)
        created_at: Mapped[sa.DateTime] = mapped_column(
            sa.DateTime(timezone=True), server_default=sa.func.now()
        )

        __table_args__ = (
            sa.Index("ix_daily_picks_date_rank", "pick_date", "rank"),
        )

    class RunSession(Base):
        """Records each analysis pipeline run (for audit / history)."""

        __tablename__ = "run_sessions"

        id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
        session_id: Mapped[str] = mapped_column(sa.String(36), nullable=False, unique=True)
        run_date: Mapped[sa.Date] = mapped_column(sa.Date, nullable=False, index=True)
        status: Mapped[str] = mapped_column(sa.String(20), nullable=False, default="running")
        universe_size: Mapped[int | None] = mapped_column(sa.Integer, nullable=True)
        candidates_evaluated: Mapped[int | None] = mapped_column(sa.Integer, nullable=True)
        picks_count: Mapped[int | None] = mapped_column(sa.Integer, nullable=True)
        elapsed_seconds: Mapped[float | None] = mapped_column(sa.Float, nullable=True)
        error_message: Mapped[str | None] = mapped_column(sa.Text, nullable=True)
        started_at: Mapped[sa.DateTime] = mapped_column(
            sa.DateTime(timezone=True), server_default=sa.func.now()
        )
        finished_at: Mapped[sa.DateTime | None] = mapped_column(
            sa.DateTime(timezone=True), nullable=True
        )

        __table_args__ = (sa.Index("ix_run_sessions_date", "run_date"),)

except ImportError:
    # SQLAlchemy not installed — models unavailable
    Base = None  # type: ignore[assignment,misc]
    DailyPickRow = None  # type: ignore[assignment,misc]
    RunSession = None  # type: ignore[assignment,misc]
