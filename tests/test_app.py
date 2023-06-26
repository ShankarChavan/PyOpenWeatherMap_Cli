import json
import pathlib

import pytest
from typer.testing import CliRunner

from pyopenweathermap_cli import __version__
from pyopenweathermap_cli.core.weather import WeatherInfo, print_weather_info
from pyopenweathermap_cli.main import app, weather

runner = CliRunner()

# write pytest_fixture for fake weather api response
@pytest.fixture()
def mock_weather_response():
    file = pathlib.Path("tests/resources/weather.json")
    with open(file) as f:
        sample_weather = json.loads(f.read())
    result = WeatherInfo.from_dict(sample_weather)
    return print_weather_info(result)


# mock get_weather function from weather.py using mocker
# write unit test for weather function from main.py using mock_weather_response and mocker
def test_weather(mocker, mock_weather_response):
    mocker.patch(
        "pyopenweathermap_cli.main.weather", return_value=mock_weather_response
    )
    result = runner.invoke(app, ["weather", "London"])
    captured = result.stdout

    assert result.exit_code == 0
    assert "The weather in London is" in captured


# write unit test for version function from main.py
def test_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout
