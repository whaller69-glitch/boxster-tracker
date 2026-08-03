from sqlalchemy.orm import Session

from .models import Listing, PriceHistory
from .schemas import ListingData


class ListingRepository:

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def create(
        self,
        data: ListingData,
    ):
        listing = Listing(
            source=data.source,
            url=data.url,
            year=data.year,
            make=data.make,
            model=data.model,
            price=data.price,
            mileage=data.mileage,
            colour=data.colour,
            transmission=data.transmission,
            trim=data.trim,
            seller=data.seller,
            location=data.location,
            captured_at=data.captured_at,
        )

        self.session.add(listing)
        self.session.commit()
        self.session.refresh(listing)

        return listing

    def get_all(self):
        return (
            self.session
            .query(Listing)
            .order_by(Listing.id)
            .all()
        )

    def filter(
        self,
        year: int | None = None,
        max_price: float | None = None,
        max_mileage: int | None = None,
    ):
        query = self.session.query(Listing)

        if year is not None:
            query = query.filter(
                Listing.year == year
            )

        if max_price is not None:
            query = query.filter(
                Listing.price <= max_price
            )

        if max_mileage is not None:
            query = query.filter(
                Listing.mileage <= max_mileage
            )

        return (
            query
            .order_by(Listing.id)
            .all()
        )

    def add_price_history(
        self,
        listing_id: int,
        price: float,
    ):
        record = PriceHistory(
            listing_id=listing_id,
            price=price,
        )

        self.session.add(record)
        self.session.commit()
        self.session.refresh(record)

        return record

    def get_price_history(
        self,
        listing_id: int,
    ):
        return (
            self.session
            .query(PriceHistory)
            .filter(
                PriceHistory.listing_id == listing_id
            )
            .order_by(
                PriceHistory.recorded_at
            )
            .all()
        )
