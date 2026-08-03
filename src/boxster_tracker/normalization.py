def normalize_transmission(
    value: str | None,
) -> str | None:

    if value is None:
        return None

    mappings = {
        "M": "Manual",
        "A": "Automatic",
        "MANUAL": "Manual",
        "AUTOMATIC": "Automatic",
    }

    return mappings.get(
        value.upper(),
        value,
    )
