import json
from bs4 import BeautifulSoup


def extract_jsonld(html: str) -> list[dict]:

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    results = []

    for script in soup.find_all(
        "script",
        type="application/ld+json",
    ):
        try:
            results.append(
                json.loads(script.string)
            )
        except Exception:
            continue

    return results

