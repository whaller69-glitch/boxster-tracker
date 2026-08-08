import re

from boxster_tracker.normalization import normalize_transmission
from boxster_tracker.schemas import ListingData

from .autotrader_state import extract_vehicle_state
from .jsonld import extract_jsonld


def extract_year(value: str) -> int | None:
    match = re.search(
        r"\b(19|20)\d{2}\b",
        value or "",
    )

    if match:
        return int(match.group())

    return None


def extract_price(value) -> float | None:
    if value is None:
        return None

    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def clean_value(value: str | None) -> str | None:
    if not value:
        return None

    return value.strip()


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

        brand = product.get(
            "brand",
            {},
        )

        offers = product.get(
            "offers",
            {},
        )

        return ListingData(
            source="autotrader",
            url=url,

            year=extract_year(
                product.get("name", "")
            ),

            make=clean_value(
                brand.get("name")
            ),

            model="Boxster",

            price=extract_price(
                offers.get("price")
            ),

            colour=clean_value(
                product.get("color")
            ),

            mileage=state.get(
                "mileage"
            ),

            transmission=normalize_transmission(
                state.get("transmission")
            ),
        )
