import typer

from boxster_tracker import __version__
from boxster_tracker.paths import AppPaths
from boxster_tracker.config import load_config
from boxster_tracker.database import get_session
from boxster_tracker.import_service import ImportService

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


if __name__ == "__main__":
    app()

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

    listing = (
        service
        .import_autotrader_url(url)
    )

    typer.echo(
        f"Imported listing #{listing.id}"
    )

