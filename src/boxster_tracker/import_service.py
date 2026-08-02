from sqlalchemy.orm import Session

from .importers.autotrader import AutoTraderImporter
from .services import ListingService


class ImportService:

    def __init__(
        self,
        session: Session,
    ):
        self.listing_service = ListingService(session)
        self.autotrader = AutoTraderImporter()

    def import_autotrader_url(
        self,
        url: str,
    ):

        listing = (
            self.autotrader
            .import_url(url)
        )

        return self.listing_service.add_listing(
            listing
        )

