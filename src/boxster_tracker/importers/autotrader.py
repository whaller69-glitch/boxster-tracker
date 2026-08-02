from boxster_tracker.schemas import ListingData


class AutoTraderImporter:
    """
    Converts AutoTrader URLs into listing records.

    Detailed scraping comes later.
    """

    SOURCE = "autotrader"

    def import_url(
        self,
        url: str,
    ) -> ListingData:

        return ListingData(
            source=self.SOURCE,
            url=url,
            make="Porsche",
            model="Boxster",
        )

