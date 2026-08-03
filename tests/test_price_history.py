from boxster_tracker.repositories import ListingRepository
from boxster_tracker.schemas import ListingData
from boxster_tracker.services.listing import ListingService
from boxster_tracker.database import get_session


def test_price_history(tmp_path):

    session = get_session(
        tmp_path / "test.db"
    )

    service = ListingService(session)

    listing = service.add_listing(
        ListingData(
            source="test",
            url="https://example.com/boxster",
            year=2001,
            make="Porsche",
            model="Boxster",
            price=15598,
            mileage=104898,
        )
    )

    service.record_price(
        listing.id,
        15598,
    )

    service.record_price(
        listing.id,
        14998,
    )

    history = service.price_history(
        listing.id
    )

    assert len(history) == 2
    assert history[0].price == 15598
    assert history[1].price == 14998
