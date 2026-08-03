import re


def extract_vehicle_state(
    html: str,
) -> dict:
    """
    Extract vehicle details embedded in AutoTrader page state.
    """

    result = {
        "mileage": None,
        "transmission": None,
    }

    if not html:
        return result

    mileage_match = re.search(
        r'(\d{1,3}(?:,\d{3})*)\s*km',
        html,
        re.IGNORECASE,
    )

    if mileage_match:
        result["mileage"] = int(
            mileage_match.group(1).replace(",", "")
        )

    transmission_match = re.search(
        r'"transmission(?:Type)?"\s*:\s*"([^"]+)"',
        html,
        re.IGNORECASE,
    )

    if transmission_match:
        value = transmission_match.group(1).strip()

        transmission_map = {
            "Manual": "M",
            "Automatic": "A",
            "Manual Transmission": "M",
            "Automatic Transmission": "A",
        }

        result["transmission"] = transmission_map.get(
            value,
            value,
        )

    return result
