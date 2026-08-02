from datetime import datetime

from sqlalchemy import (
    DateTime,
    Float,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Listing(Base):
    __tablename__ = "listings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    source: Mapped[str] = mapped_column(String(50))
    url: Mapped[str] = mapped_column(String(500))

    year: Mapped[int | None]
    make: Mapped[str | None]
    model: Mapped[str | None]

    price: Mapped[float | None]
    mileage: Mapped[int | None]

    status: Mapped[str] = mapped_column(
        String(50),
        default="active",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
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
        default=datetime.utcnow
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

