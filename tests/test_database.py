from pathlib import Path

from boxster_tracker.database import create_database
from boxster_tracker.models import Listing


def test_database_creation(tmp_path):

    db = tmp_path / "test.db"

    engine = create_database(db)

    assert db.exists()

    assert Listing.__tablename__ == "listings"

