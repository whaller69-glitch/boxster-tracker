from boxster_tracker.importers.autotrader import (
    AutoTraderImporter,
)


def test_autotrader_url_import():

    importer = AutoTraderImporter()

    listing = importer.import_url(
        "https://www.autotrader.ca/offers/test"
    )

    assert listing.source == "autotrader"
    assert listing.make == "Porsche"
    assert listing.model == "Boxster"

