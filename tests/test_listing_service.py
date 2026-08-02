from boxster_tracker.schemas import ListingData


def test_listing_schema():

    listing = ListingData(
        source="autotrader",
        url="https://example.com",
        year=2007,
        model="Boxster",
    )

    assert listing.year == 2007
    assert listing.source == "autotrader"

