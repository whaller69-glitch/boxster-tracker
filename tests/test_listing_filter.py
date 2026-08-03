from datetime import datetime

from boxster_tracker.database import get_session
from boxster_tracker.repositories import ListingRepository
from boxster_tracker.schemas import ListingData


def create_listing(
    session,
    *,
    year,
    price,
    mileage,
):
    repository = ListingRepository(session)

    return repository.create(
        ListingData(
            source="test",
            url=f"https://example.com/{year}",
            year=year,
            make="Porsche",
            model="Boxster",
            price=price,
            mileage=mileage,
            colour="Red",
            transmission="Manual",
            trim=None,
            seller="Test Seller",
            location="Ontario",
            captured_at=datetime.now(),
        )
    )


def test_filter_by_year(tmp_path):

    session = get_session(
        tmp_path / "test.db"
    )

    create_listing(
        session,
        year=2001,
        price=15598,
        mileage=104898,
    )

    create_listing(
        session,
        year=1998,
        price=12000,
        mileage=90000,
    )

    repository = ListingRepository(session)

    results = repository.filter(
        year=2001,
    )

    assert len(results) == 1
    assert results[0].year == 2001


def test_filter_by_max_price(tmp_path):

    session = get_session(
        tmp_path / "test.db"
    )

    create_listing(
        session,
        year=2001,
        price=15598,
        mileage=104898,
    )

    create_listing(
        session,
        year=2005,
        price=30000,
        mileage=60000,
    )

    repository = ListingRepository(session)

    results = repository.filter(
        max_price=20000,
    )

    assert len(results) == 1
    assert results[0].price == 15598


def test_filter_by_max_mileage(tmp_path):

    session = get_session(
        tmp_path / "test.db"
    )

    create_listing(
        session,
        year=2001,
        price=15598,
        mileage=104898,
    )

    create_listing(
        session,
        year=2005,
        price=30000,
        mileage=60000,
    )

    repository = ListingRepository(session)

    results = repository.filter(
        max_mileage=80000,
    )

    assert len(results) == 1
    assert results[0].mileage == 60000

