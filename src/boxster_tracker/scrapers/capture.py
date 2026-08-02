from pathlib import Path

from playwright.sync_api import sync_playwright


class PageCapture:

    def __init__(
        self,
        output_dir: Path,
    ):
        self.output_dir = output_dir

    def capture(
        self,
        url: str,
        filename: str,
    ) -> Path:

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = self.output_dir / filename

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            try:
                page = browser.new_page()

                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=60000,
                )

                page.wait_for_timeout(5000)

                html = page.content()

            finally:
                browser.close()

        path.write_text(
            html,
            encoding="utf-8",
        )

        return path

