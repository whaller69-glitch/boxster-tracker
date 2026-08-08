from sqlalchemy.orm import Session

from ..repositories import ListingRepository
from ..schemas import ListingData


class ListingService:

    def __init__(
        self,
        session: Session,
    ):
        self.repository = ListingRepository(session)

    def add_listing(
        self,
        data: ListingData,
    ):
        existing = self.repository.get_by_url(
            data.url
        )

        if existing is None:
            return self.repository.create(data)

        old_price = existing.price

        listing = self.repository.update(
            existing,
            data,
        )

        if (
            listing.price is not None
            and listing.price != old_price
        ):
            self.repository.add_price_history(
                listing.id,
                listing.price,
            )

        return listing

    def get(
        self,
        listing_id: int,
    ):
        return self.repository.get(
            listing_id,
        )

    def get_all(self):
        return self.repository.get_all()

    def search(
        self,
        year: int | None = None,
        max_price: float | None = None,
        max_mileage: int | None = None,
    ):
        return self.repository.filter(
            year=year,
            max_price=max_price,
            max_mileage=max_mileage,
        )

    def record_price(
        self,
        listing_id: int,
        price: float,
    ):
        return self.repository.add_price_history(
            listing_id,
            price,
        )

    def price_history(
        self,
        listing_id: int,
    ):
        return self.repository.get_price_history(
            listing_id,
        )
