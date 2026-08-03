import re

from boxster_tracker.schemas import ListingData
from boxster_tracker.normalization import normalize_transmission
from .jsonld import extract_jsonld
from .autotrader_state import extract_vehicle_state

def extract_year(value: str) -> int | None:
    match = re.search(
        r"\b(19|20)\d{2}\b",
        value,
    )

    if match:
        return int(match.group())

    return None


class AutoTraderParser:
    """
    Parse AutoTrader structured data.
    """

    def parse(
        self,
        html: str,
        url: str,
    ) -> ListingData:

        documents = extract_jsonld(html)
        state = extract_vehicle_state(html)
        product = None

        for doc in documents:
            if doc.get("@type") == "Product":
                product = doc
                break

        if product is None:
            return ListingData(
                source="autotrader",
                url=url,
            )

        return ListingData(
            source="autotrader",
            url=url,

            year=extract_year(
                product.get("name", "")
            ),

            make=product.get(
                "brand",
                {},
            ).get(
                "name"
            ),

            model="Boxster",

            price=product.get(
                "offers",
                {},
            ).get(
                "price"
            ),
            colour=product.get(
                "color"
            ),

            mileage=state.get(
                "mileage"
            ),

            transmission=normalize_transmission(
                state.get("transmission")
            ),
        )
