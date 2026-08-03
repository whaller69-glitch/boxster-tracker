from pathlib import Path


class AppPaths:
    """Application filesystem paths."""

    def __init__(self, config: dict):
        self.root = Path(config["storage"]["root"])

        self.photos = (
            self.root
            / config["directories"]["photos"]
        )

        self.history = (
            self.root
            / config["directories"]["history"]
        )

        output = Path(config["output"]["root"])

        self.reports = (
            output
            / config["output"]["reports"]
        )

        self.exports = (
            output
            / config["output"]["exports"]
        )
    @property
    def pages(self) -> Path:
        return self.root / "history" / "pages"
    def database(self) -> Path:
        return self.root / "boxsters.db"
    def create(self) -> None:
        """Create required directories."""

        for path in [
            self.root,
            self.photos,
            self.history,
            self.reports,
            self.exports,
        ]:
            path.mkdir(parents=True, exist_ok=True)

