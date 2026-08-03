from playwright.sync_api import sync_playwright

from .base import ListingScraper


class AutoTraderScraper(ListingScraper):
    """
    Capture AutoTrader listing HTML.
    """

    SOURCE = "autotrader"

    def scrape(
        self,
        url: str,
    ) -> str:
        """
        Return rendered HTML for parsing.
        """

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True
            )

            try:
                page = browser.new_page()

                page.goto(
                    url,
                    wait_until="networkidle",
                    timeout=30000,
                )

                return page.content()

            finally:
                browser.close()
