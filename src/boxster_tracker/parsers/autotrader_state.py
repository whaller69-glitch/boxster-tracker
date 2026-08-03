import re


def extract_vehicle_state(
    html: str,
) -> dict:

    data = {}

    mileage = re.search(
        r'"mileageInKmRaw":(\d+)',
        html,
    )

    if mileage:
        data["mileage"] = int(
            mileage.group(1)
        )

    transmission = re.search(
        r'"gear":"([^"]+)"',
        html,
    )

    if transmission:
        data["transmission"] = (
            transmission.group(1)
        )

    return data
