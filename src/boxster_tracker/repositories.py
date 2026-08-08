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
            trim=data.trim,
            price=data.price,
            mileage=data.mileage,
            colour=data.colour,
            transmission=data.transmission,
            seller=data.seller,
            location=data.location,
            captured_at=data.captured_at,
        )

        self.session.add(listing)
        self.session.commit()
        self.session.refresh(listing)

        return listing

    def get(
        self,
        listing_id: int,
    ):
        return (
            self.session
            .query(Listing)
            .filter(
                Listing.id == listing_id
            )
            .first()
        )

    def get_by_url(
        self,
        url: str,
    ):
        return (
            self.session
            .query(Listing)
            .filter(
                Listing.url == url
            )
            .first()
        )

    def update(
        self,
        listing: Listing,
        data: ListingData,
    ):
        listing.source = data.source
        listing.url = data.url
        listing.year = data.year
        listing.make = data.make
        listing.model = data.model
        listing.trim = data.trim
        listing.price = data.price
        listing.mileage = data.mileage
        listing.colour = data.colour
        listing.transmission = data.transmission
        listing.seller = data.seller
        listing.location = data.location

        if data.captured_at is not None:
            listing.captured_at = data.captured_at

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
        history = PriceHistory(
            listing_id=listing_id,
            price=price,
        )

        self.session.add(history)
        self.session.commit()
        self.session.refresh(history)

        return history

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
                PriceHistory.recorded_at.asc()
            )
            .all()
        )
