from playwright.sync_api import sync_playwright

from boxster_tracker.schemas import ListingData

from .base import ListingScraper


class AutoTraderScraper(ListingScraper):

    SOURCE = "autotrader"

    def scrape(
        self,
        url: str,
    ) -> ListingData:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            page.goto(
                url,
                wait_until="networkidle",
            )

            title = page.title()

            browser.close()

        return ListingData(
            source=self.SOURCE,
            url=url,
            model="Boxster",
        )

