from abc import ABC, abstractmethod

from boxster_tracker.schemas import ListingData


class ListingScraper(ABC):

    @abstractmethod
    def scrape(
        self,
        url: str,
    ) -> ListingData:
        pass

