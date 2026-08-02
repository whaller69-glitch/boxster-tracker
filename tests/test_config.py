from boxster_tracker.config import load_config
from boxster_tracker.paths import AppPaths


def test_load_default_config():
    config = load_config()

    assert config["application"]["name"] == "boxster-tracker"


def test_create_paths(tmp_path):
    config = load_config()

    config["storage"]["root"] = str(tmp_path / "data")

    paths = AppPaths(config)
    paths.create()

    assert paths.photos.exists()
    assert paths.history.exists()
