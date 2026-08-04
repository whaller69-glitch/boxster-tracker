import re


_PATTERNS = [
    (
        re.compile(r"AIza[0-9A-Za-z_-]{35}"),
        "GOOGLE_API_KEY_REDACTED",
    ),
]


def sanitize_html(html: str) -> str:
    """
    Remove embedded secrets from captured HTML.
    """

    for pattern, replacement in _PATTERNS:
        html = pattern.sub(
            replacement,
            html,
        )

    return html
