import typer

from boxster_tracker import __version__
from boxster_tracker.config import load_config
from boxster_tracker.database import get_session
from boxster_tracker.import_service import ImportService
from boxster_tracker.paths import AppPaths
from boxster_tracker.scrapers.capture import PageCapture
from boxster_tracker.services import ImportFileService

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

    typer.echo(f"Importing {len(urls)} URLs...")
    typer.echo("")

    for index, url in enumerate(urls, start=1):
        typer.echo(f"[{index}/{len(urls)}] {url}")

        try:
            listing = importer.import_autotrader_url(url)

            typer.echo(
                f"  ✓ Imported listing #{listing.id}"
            )

        except Exception as exc:
            typer.echo(
                f"  ✗ Failed: {exc}",
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


if __name__ == "__main__":
    app()
