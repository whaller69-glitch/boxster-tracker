from playwright.sync_api import TimeoutError, sync_playwright

from .base import ListingScraper


class AutoTraderScraper(ListingScraper):
    """
    Capture rendered HTML from an AutoTrader listing.
    """

    SOURCE = "autotrader"

    def scrape(
        self,
        url: str,
    ) -> str:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True,
            )

            page = browser.new_page()

            try:
                print("Opening page...")

                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=30_000,
                )

                print("Waiting for JSON-LD...")

                page.wait_for_selector(
                    'script[type="application/ld+json"]',
                    timeout=10_000,
                )

                print("Capturing HTML...")

                html = page.content()

            except TimeoutError:
                print(
                    "JSON-LD not found; capturing current page."
                )
                html = page.content()

            finally:
                browser.close()

        return html
