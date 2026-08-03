from datetime import datetime, UTC

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Listing(Base):
    __tablename__ = "listings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    source: Mapped[str] = mapped_column(
        String(50)
    )

    url: Mapped[str] = mapped_column(
        String(500)
    )

    year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    make: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    model: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    trim: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    price: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    mileage: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    colour: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    transmission: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    seller: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    location: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    captured_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC),
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="active",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC),
    )


class PriceHistory(Base):
    __tablename__ = "price_history"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    listing_id: Mapped[int] = mapped_column(
        ForeignKey("listings.id")
    )

    price: Mapped[float]

    recorded_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC),
    )


class Photo(Base):
    __tablename__ = "photos"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    listing_id: Mapped[int] = mapped_column(
        ForeignKey("listings.id")
    )

    path: Mapped[str]
