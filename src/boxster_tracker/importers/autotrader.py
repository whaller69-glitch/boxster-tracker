from boxster_tracker.parsers.autotrader import AutoTraderParser
from boxster_tracker.scrapers.autotrader import AutoTraderScraper
from boxster_tracker.schemas import ListingData


class AutoTraderImporter:
    """
    Imports AutoTrader listings by scraping and parsing pages.
    """

    SOURCE = "autotrader"

    def __init__(
        self,
        scraper: AutoTraderScraper | None = None,
        parser: AutoTraderParser | None = None,
    ):
        self.scraper = scraper or AutoTraderScraper()
        self.parser = parser or AutoTraderParser()

    def import_url(
        self,
        url: str,
    ) -> ListingData:
        html = self.scraper.scrape(url)

        return self.parser.parse(
            html,
            url,
        )
