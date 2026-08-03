from pathlib import Path


class ImportFileService:
    def load_urls(
        self,
        filename: str,
    ) -> list[str]:

        lines = Path(filename).read_text().splitlines()

        urls = []

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            urls.append(line)

        return urls
