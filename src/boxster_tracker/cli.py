import typer

from boxster_tracker import __version__
from boxster_tracker.config import load_config
from boxster_tracker.database import get_session
from boxster_tracker.import_service import ImportService
from boxster_tracker.paths import AppPaths
from boxster_tracker.scrapers.capture import PageCapture
from boxster_tracker.services import ListingService


app = typer.Typer(
    name="boxster",
    help="Porsche Boxster market tracking tool",
)


@app.command()
def version():
    """Show application version."""
    typer.echo(__version__)


@app.command()
def init():
    """Initialize Boxster Tracker workspace."""

    config = load_config()
    paths = AppPaths(config)

    paths.create()

    typer.echo("Boxster Tracker initialized")
    typer.echo("")
    typer.echo("Created:")
    typer.echo(f"  {paths.root}")
    typer.echo(f"  {paths.photos}")
    typer.echo(f"  {paths.history}")
    typer.echo(f"  {paths.reports}")
    typer.echo(f"  {paths.exports}")


@app.command()
def status():
    """Show application status."""

    config = load_config()

    typer.echo("Configuration loaded")
    typer.echo(
        f"Application: {config['application']['name']}"
    )


@app.command()
def import_url(
    url: str,
):
    """
    Import a vehicle listing URL.
    """

    config = load_config()
    paths = AppPaths(config)

    paths.create()

    session = get_session(
        paths.database
    )

    service = ImportService(session)

    listing = service.import_autotrader_url(
        url
    )

    typer.echo(
        f"Imported listing #{listing.id}"
    )


@app.command()
def capture_url(
    url: str,
):
    """
    Capture an AutoTrader page.
    """

    config = load_config()
    paths = AppPaths(config)

    paths.create()

    capture = PageCapture(
        paths.pages
    )

    output = capture.capture(
        url,
        "capture.html",
    )

    typer.echo(
        f"Saved page: {output}"
    )


@app.command(name="list")
def list_listings():
    """
    List all stored vehicle listings.
    """

    config = load_config()
    paths = AppPaths(config)

    session = get_session(
        paths.database
    )

    service = ListingService(session)

    listings = service.get_all()

    if not listings:
        typer.echo("No listings found")
        return

    for listing in listings:
        typer.echo(
            f"{listing.id}: "
            f"{listing.year} "
            f"{listing.make} "
            f"{listing.model} "
            f"${listing.price} "
            f"{listing.mileage} km"
        )


@app.command()
def search(
    year: int | None = typer.Option(
        None,
        help="Filter by model year",
    ),
    max_price: float | None = typer.Option(
        None,
        help="Maximum price",
    ),
    max_mileage: int | None = typer.Option(
        None,
        help="Maximum mileage",
    ),
):
    """
    Search stored listings.
    """

    config = load_config()
    paths = AppPaths(config)

    session = get_session(
        paths.database
    )

    service = ListingService(session)

    listings = service.search(
        year=year,
        max_price=max_price,
        max_mileage=max_mileage,
    )

    if not listings:
        typer.echo("No matching listings")
        return

    for listing in listings:
        typer.echo(
            f"{listing.id}: "
            f"{listing.year} "
            f"{listing.make} "
            f"{listing.model} "
            f"${listing.price} "
            f"{listing.mileage} km"
        )


if __name__ == "__main__":
    app()
