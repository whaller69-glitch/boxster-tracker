from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = PROJECT_ROOT / "config" / "default.yaml"


def load_config(path: Path | None = None) -> dict:
    """Load application configuration."""

    config_path = path or DEFAULT_CONFIG

    with config_path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)
