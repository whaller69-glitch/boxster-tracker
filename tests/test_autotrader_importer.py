from boxster_tracker.importers.autotrader import AutoTraderImporter
from boxster_tracker.schemas import ListingData


class FakeScraper:
    def scrape(self, url):
        return "<html>fixture</html>"


class FakeParser:
    def parse(self, html, url):
        return ListingData(
            source="autotrader",
            url=url,
            year=2001,
            make="Porsche",
            model="Boxster",
            price=15598,
        )


def test_importer_pipeline():

    importer = AutoTraderImporter(
        scraper=FakeScraper(),
        parser=FakeParser(),
    )

    listing = importer.import_url(
        "https://example.com/listing"
    )

    assert listing.source == "autotrader"
    assert listing.year == 2001
    assert listing.make == "Porsche"
    assert listing.model == "Boxster"
    assert listing.price == 15598
