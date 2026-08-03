from pathlib import Path

from boxster_tracker.parsers.autotrader_state import (
    extract_vehicle_state,
)


def test_extract_vehicle_state():

    html = Path(
        "tests/fixtures/autotrader_real.html"
    ).read_text()

    data = extract_vehicle_state(html)

    assert data["mileage"] == 104898
    assert data["transmission"] == "M"
