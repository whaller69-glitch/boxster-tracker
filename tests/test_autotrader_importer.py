from pathlib import Path

from boxster_tracker.importers.autotrader import (
    AutoTraderImporter,
)


def test_autotrader_url_import(monkeypatch):

    html = Path(
        "tests/fixtures/autotrader_real.html"
    ).read_text()

    importer = AutoTraderImporter()

    monkeypatch.setattr(
        importer.scraper,
        "scrape",
        lambda url: html,
    )

    listing = importer.import_url(
        "https://www.autotrader.ca/offers/test"
    )

    assert listing.source == "autotrader"
    assert listing.make == "Porsche"
    assert listing.model == "Boxster"
    assert listing.price == 15598
    assert listing.mileage == 104898
