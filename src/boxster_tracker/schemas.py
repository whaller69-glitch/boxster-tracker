from dataclasses import dataclass


@dataclass
class ListingData:
    source: str
    url: str

    year: int | None = None
    make: str | None = None
    model: str | None = None

    price: float | None = None
    mileage: int | None = None

    colour: str | None = None
    transmission: str | None = None

