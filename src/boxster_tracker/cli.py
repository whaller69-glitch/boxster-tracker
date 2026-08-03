import typer
from rich.console import Console
from rich.table import Table
from boxster_tracker.services.listing import ListingService
from boxster_tracker import __version__
from boxster_tracker.config import load_config
from boxster_tracker.database import get_session
from boxster_tracker.import_service import ImportService
from boxster_tracker.paths import AppPaths
from boxster_tracker.scrapers.capture import PageCapture
from boxster_tracker.services import (
    ImportFileService,
    ListingService,
)

app = typer.Typer(
    name="boxster",
    help="Porsche Boxster market tracking tool",
)

console = Console()


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
def list(
    year: int | None = typer.Option(
        None,
        help="Filter by model year",
    ),
    max_price: float | None = typer.Option(
        None,
        help="Maximum price",
    ),
    max_km: int | None = typer.Option(
        None,
        help="Maximum mileage",
    ),
):
    """
    List tracked Boxster listings.
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
        max_mileage=max_km,
    )

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
def import_url(url: str):
    """
    Import a vehicle listing URL.
    """

    config = load_config()
    paths = AppPaths(config)

    paths.create()

    session = get_session(paths.database)

    service = ImportService(session)

    listing = service.import_autotrader_url(url)

    typer.echo(
        f"Imported listing #{listing.id}"
    )


@app.command("import-file")
def import_file(filename: str):
    """
    Import every URL from a text file.
    """

    config = load_config()
    paths = AppPaths(config)

    paths.create()

    session = get_session(paths.database)

    importer = ImportService(session)
    file_service = ImportFileService()

    urls = file_service.load_urls(filename)

    typer.echo(
        f"Importing {len(urls)} URLs..."
    )

    for index, url in enumerate(urls, start=1):

        typer.echo(
            f"[{index}/{len(urls)}] {url}"
        )

        try:
            listing = importer.import_autotrader_url(url)

            typer.echo(
                f"  Imported listing #{listing.id}"
            )

        except Exception as exc:
            typer.echo(
                f"  Failed: {exc}",
                err=True,
            )


@app.command()
def capture_url(url: str):
    """
    Capture an AutoTrader page.
    """

    config = load_config()
    paths = AppPaths(config)

    capture = PageCapture(paths.pages)

    output = capture.capture(
        url,
        "capture.html",
    )

    typer.echo(
        f"Saved page: {output}"
    )

@app.command(name="list")
def list_listings(
    year: int | None = None,
    max_price: float | None = None,
    max_km: int | None = None,
):
    """
    Display stored listings.
    """

    config = load_config()
    paths = AppPaths(config)

    session = get_session(paths.database)

    service = ListingService(session)

    listings = service.get_all()

    table = Table(
        title="Porsche Boxster Listings"
    )

    table.add_column("ID")
    table.add_column("Year")
    table.add_column("Model")
    table.add_column("Price")
    table.add_column("Mileage")
    table.add_column("Colour")

    for listing in listings:

        table.add_row(
            str(listing.id),
            str(listing.year or ""),
            listing.model or "",
            (
                f"${listing.price:,.0f}"
                if listing.price
                else ""
            ),
            (
                f"{listing.mileage:,} km"
                if listing.mileage
                else ""
            ),
            listing.colour or "",
        )

    console.print(table)


if __name__ == "__main__":
    app()
