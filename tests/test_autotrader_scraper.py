from boxster_tracker.scrapers.autotrader import (
    AutoTraderScraper,
)


def test_autotrader_scraper():

    scraper = AutoTraderScraper()

    assert scraper.SOURCE == "autotrader"

