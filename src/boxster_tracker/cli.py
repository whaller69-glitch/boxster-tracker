import csv
from pathlib import Path

import typer

from boxster_tracker.config import load_config
from boxster_tracker.database import get_session
from boxster_tracker.importers.autotrader import AutoTraderImporter
from boxster_tracker.paths import AppPaths
from boxster_tracker.services.listing import ListingService

app = typer.Typer()


def get_service() -> ListingService:
    config = load_config()

    paths = AppPaths(config)
    paths.create()

    session = get_session(
        paths.database
    )

    return ListingService(session)


@app.command()
def version():
    typer.echo("0.1.0")


@app.command()
def status():
    config = load_config()

    typer.echo("Configuration loaded")
    typer.echo(
        f"Application: {config['application']['name']}"
    )


@app.command("import-url")
def import_url(
    url: str,
):
    service = get_service()

    listing = AutoTraderImporter().import_url(url)
    record = service.add_listing(listing)

    typer.echo(
        f"Imported listing #{record.id}"
    )


@app.command()
def list():
    service = get_service()

    listings = service.get_all()

    if not listings:
        typer.echo("No listings found")
        raise typer.Exit()

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
def show(
    listing_id: int,
):
    service = get_service()

    listing = service.get(listing_id)

    if listing is None:
        typer.echo("Listing not found")
        raise typer.Exit(code=1)

    typer.echo(f"ID:            {listing.id}")
    typer.echo(f"Source:        {listing.source}")
    typer.echo(f"Year:          {listing.year}")
    typer.echo(f"Make:          {listing.make}")
    typer.echo(f"Model:         {listing.model}")
    typer.echo(f"Trim:          {listing.trim}")
    typer.echo(f"Price:         {listing.price}")
    typer.echo(f"Mileage:       {listing.mileage}")
    typer.echo(
        f"Transmission:  {listing.transmission}"
    )
    typer.echo(f"Colour:        {listing.colour}")
    typer.echo(f"Seller:        {listing.seller}")
    typer.echo(f"Location:      {listing.location}")
    typer.echo(
        f"Captured:      {listing.captured_at}"
    )
    typer.echo(f"URL:           {listing.url}")


@app.command()
def search(
    year: int | None = None,
    max_price: float | None = None,
    max_mileage: int | None = None,
):
    service = get_service()

    listings = service.search(
        year=year,
        max_price=max_price,
        max_mileage=max_mileage,
    )

    if not listings:
        typer.echo("No matching listings")
        raise typer.Exit()

    for listing in listings:
        typer.echo(
            f"{listing.id}: "
            f"{listing.year} "
            f"{listing.make} "
            f"{listing.model} "
            f"${listing.price}"
        )


@app.command()
def export():
    config = load_config()

    paths = AppPaths(config)
    paths.create()

    session = get_session(
        paths.database
    )

    service = ListingService(session)
    listings = service.get_all()

    if not listings:
        typer.echo("No listings found")
        raise typer.Exit()

    export_dir = Path("data/exports")
    export_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = (
        export_dir / "boxster-listings.csv"
    )

    fieldnames = [
        "id",
        "source",
        "url",
        "year",
        "make",
        "model",
        "trim",
        "price",
        "mileage",
        "colour",
        "transmission",
        "seller",
        "location",
        "captured_at",
        "status",
    ]

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
        )

        writer.writeheader()

        for listing in listings:
            writer.writerow(
                {
                    "id": listing.id,
                    "source": listing.source,
                    "url": listing.url,
                    "year": listing.year,
                    "make": listing.make,
                    "model": listing.model,
                    "trim": listing.trim,
                    "price": listing.price,
                    "mileage": listing.mileage,
                    "colour": listing.colour,
                    "transmission": listing.transmission,
                    "seller": listing.seller,
                    "location": listing.location,
                    "captured_at": listing.captured_at,
                    "status": listing.status,
                }
            )

    typer.echo(
        f"Exported {len(listings)} listings to "
        f"{output_path}"
    )


if __name__ == "__main__":
    app()
