from sqlalchemy.orm import Session

from .repositories import ListingRepository
from .schemas import ListingData


class ListingService:

    def __init__(self, session: Session):
        self.repository = ListingRepository(session)

    def add_listing(
        self,
        data: ListingData,
    ):

        return self.repository.create(data)

