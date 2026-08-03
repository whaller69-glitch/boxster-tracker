from dataclasses import dataclass
from datetime import datetime


@dataclass
class ListingData:
    source: str
    url: str

    year: int | None = None
    make: str | None = None
    model: str | None = None
    trim: str | None = None

    price: float | None = None
    mileage: int | None = None

    colour: str | None = None
    transmission: str | None = None

    seller: str | None = None
    location: str | None = None
    captured_at: datetime | None = None
