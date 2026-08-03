from sqlalchemy.orm import Session

from boxster_tracker.repositories import ListingRepository
from boxster_tracker.schemas import ListingData


class ListingService:
    def __init__(self, session: Session):
        self.repository = ListingRepository(session)
    def get_all(self):
        return self.repository.all()

    def add_listing(
        self,
        data: ListingData,
    ):
        return self.repository.create(data)
