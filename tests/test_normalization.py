from boxster_tracker.normalization import (
    normalize_transmission,
)


def test_normalize_transmission():

    assert normalize_transmission("M") == "Manual"
    assert normalize_transmission("A") == "Automatic"
    assert normalize_transmission(None) is None
