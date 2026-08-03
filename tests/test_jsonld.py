from boxster_tracker.parsers.jsonld import (
    extract_jsonld,
)


def test_extract_jsonld():

    html = """
    <script type="application/ld+json">
    {
      "name": "2007 Porsche Boxster",
      "price": "29995"
    }
    </script>
    """

    data = extract_jsonld(html)

    assert data[0]["price"] == "29995"

