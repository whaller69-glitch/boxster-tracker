from sqlalchemy.orm import Session

from .models import Listing
from .schemas import ListingData


class ListingRepository:

    def __init__(self, session: Session):
        self.session = session

    def all(self):
       return (
          self.session
          .query(Listing)
          .order_by(Listing.created_at.desc())
          .all()
      )

    def create(
        self,
        data: ListingData,
    ) -> Listing:

        listing = Listing(
            source=data.source,
            url=data.url,
            year=data.year,
            make=data.make,
            model=data.model,
            price=data.price,
            mileage=data.mileage,
        )

        self.session.add(listing)
        self.session.commit()

        return listing

