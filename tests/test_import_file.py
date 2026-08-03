from pathlib import Path

from boxster_tracker.services.import_file import (
    ImportFileService,
)


def test_load_urls(tmp_path: Path):
    file = tmp_path / "favourites.txt"

    file.write_text(
        """
# My favourite Boxsters

https://example.com/car1

https://example.com/car2

# Ignore this comment

https://example.com/car3
"""
    )

    urls = ImportFileService().load_urls(
        str(file)
    )

    assert urls == [
        "https://example.com/car1",
        "https://example.com/car2",
        "https://example.com/car3",
    ]
