"""Uses the API python-weather forecast."""

import asyncio
import os

import python_weather

from core.services.response.daily_weather_forecast_response import (
    DailyWeatherForecastResponse,
)
from core.services.response.weather_forecast_response import (
    WeatherForecastResponse,
)


class WeatherService:
    """Calls the API py-weather."""

    def __init__(self) -> None:
        """Init the WeatherService instance."""
        self.weather_forecast: WeatherForecastResponse = None
        self.week_forecast: list = None

    async def _getweather(
        self,
        location: str,
        town: str = None,
        country: str = None,
        week_flag: bool = False,
    ) -> dict:
        # temperature: float = None
        # temperatures: list = []
        # hourly_forecats: list = []

        location = (
            town + " " + country
            if town + " " + country is not None
            and town + " " + country not in (" ")
            else location
        )

        # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            weather = None

            try:
                # fetch a weather forecast from a city
                weather = await client.get(location)

                if (
                    weather.location == "Thot Not"
                ):  # Patch for when the location is a description => The API is not ready to read this.
                    raise Exception(
                        "The location {} has not been identified. The weather"
                        " cant be defined.".format(location)
                    )
            except Exception as e:
                return {
                    "status": 1,
                    "error": "{}".format(e),
                    "day": "N/A",
                    "week": "N/A",
                    # "hourly_forecasts": hourly_forecats,
                }

            self.weather_forecast = WeatherForecastResponse(weather)
            # print(type(self.weather_forecast))
            # returns the current day's forecast temperature (int)
            # print(weather.temperature)
            # temperature = weather.temperature

            # get the weather forecast for a few days
            if week_flag:
                self.week_forecast = []
                for daily in weather.daily_forecasts:
                    self.week_forecast.append(
                        DailyWeatherForecastResponse(weather, daily)
                    )
                    # print(daily)
                    # temperatures.append(daily)

            # hourly forecasts
            # if hours_flag:
            #     for hourly in daily.hourly_forecasts:
            #         print(f" --> {hourly!r}")
            #         hourly_forecats.append(hourly)

        return {
            "status": 0,
            "error": "",
            "day": self.weather_forecast.get_forecast_payload(),
            "week": self.week_forecast,
            # "hourly_forecasts": hourly_forecats,
        }

    def get_forecast(self, location, town, country, week=False) -> dict:
        """Read a weather forecast via API call.

        Args:
            location (str): A description of the location. This param is not used
            town (str): The town for the location for the weather forecast.
            country (str): The country for the location for the weather forecast.
            week (bool, optional): Indicates if the whole week of forecasts should be rerieved. Defaults to False.

        Returns:
            dict: a payload for the type of desired forecast weather.
        """
        if os.name == "nt":
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy()
            )
        return asyncio.run(self._getweather(location, town, country, week))


# if __name__ == '__main__':
#   # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
#   # for more details
#   if os.name == 'nt':
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#   asyncio.run(getweather())
