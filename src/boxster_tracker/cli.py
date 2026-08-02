
import typer

from boxster_tracker import __version__

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
    """Initialize Boxster Tracker."""
    typer.echo("Boxster Tracker initialized")


@app.command()
def status():
    """Show application status."""
    typer.echo("Status command not implemented yet")


if __name__ == "__main__":
    app()
