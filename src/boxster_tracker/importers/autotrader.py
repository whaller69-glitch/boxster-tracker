from boxster_tracker.scrapers.autotrader import (
    AutoTraderScraper,
)
from boxster_tracker.parsers.autotrader import (
    AutoTraderParser,
)


class AutoTraderImporter:
    """
    Import AutoTrader listings.
    """

    SOURCE = "autotrader"

    def __init__(self):
        self.scraper = AutoTraderScraper()
        self.parser = AutoTraderParser()

    def import_url(
        self,
        url: str,
    ):

        html = self.scraper.scrape(url)

        return self.parser.parse(
            html,
            url,
        )
