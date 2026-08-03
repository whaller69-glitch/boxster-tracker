from pathlib import Path

from boxster_tracker.parsers.autotrader import (
    AutoTraderParser,
)


def test_parse_real_autotrader_fixture():

    html = Path(
        "tests/fixtures/autotrader_real.html"
    ).read_text()

    listing = AutoTraderParser().parse(
        html,
        "https://autotrader.ca/test",
    )

    assert listing.make == "Porsche"
    assert listing.model == "Boxster"
    assert listing.price == 15598
    assert listing.mileage == 104898
    assert listing.colour == "Red"
