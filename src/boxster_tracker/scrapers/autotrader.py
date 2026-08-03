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

            page = browser.new_page()

            page.goto(
                url,
                wait_until="networkidle",
            )

            html = page.content()

            browser.close()

        return html
