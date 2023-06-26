import typer

from pyopenweathermap_cli import __version__

# from pytemplates_typer_cli import __version__
from pyopenweathermap_cli.core.weather import get_weather, print_weather_info

app = typer.Typer()


@app.command()
def weather(location: str) -> None:
    """Display weather forecast for given location.
    Args:
        location: location or country name.
    """
    weather_info = get_weather(city=location)
    typer.echo(print_weather_info(weather_info), color=typer.colors.BRIGHT_GREEN)


@app.command()
def version() -> None:
    """Display the CLI version number."""
    typer.echo(__version__)


if __name__ == "__main__":
    app()
