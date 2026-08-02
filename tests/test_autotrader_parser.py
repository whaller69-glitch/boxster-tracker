from pathlib import Path

from boxster_tracker.parsers.autotrader import (
    AutoTraderParser,
)


def test_parse_autotrader_fixture():

    html = Path(
        "tests/fixtures/autotrader_boxster.html"
    ).read_text()

    parser = AutoTraderParser()

    listing = parser.parse(
        html,
        "https://example.com",
    )

    assert listing.year == 2007
    assert listing.price == 29995
    assert listing.mileage == 45000

