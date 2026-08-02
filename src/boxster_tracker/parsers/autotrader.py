import re

from boxster_tracker.schemas import ListingData


class AutoTraderParser:
    """
    Parse AutoTrader HTML into ListingData.
    """

    def parse(
        self,
        html: str,
        url: str,
    ) -> ListingData:

        year = self._extract_year(html)
        price = self._extract_price(html)
        mileage = self._extract_mileage(html)

        return ListingData(
            source="autotrader",
            url=url,
            make="Porsche",
            model="Boxster",
            year=year,
            price=price,
            mileage=mileage,
        )

    def _extract_year(
        self,
        html: str,
    ) -> int | None:

        match = re.search(
            r"\b(19|20)\d{2}\b",
            html,
        )

        if match:
            return int(match.group())

        return None


    def _extract_price(
        self,
        html: str,
    ) -> float | None:

        match = re.search(
            r"\$(\d{1,3}(?:,\d{3})*)",
            html,
        )

        if match:
            return float(
                match.group(1).replace(",", "")
            )

        return None


    def _extract_mileage(
        self,
        html: str,
    ) -> int | None:

        match = re.search(
            r"(\d{1,3}(?:,\d{3})*)\s*km",
            html,
        )

        if match:
            return int(
                match.group(1).replace(",", "")
            )

        return None

