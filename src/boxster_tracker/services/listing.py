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
        return self.repository.create(data)

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
