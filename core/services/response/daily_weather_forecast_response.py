"""Parse the response of the api call for a weekly forecast."""

from python_weather.forecast import DailyForecast, Forecast

from core.services.response.weather_forecast_response import (
    WeatherForecastResponse,
)


class DailyWeatherForecastResponse(WeatherForecastResponse):
    """Parse the response of a weatherapi call for muiltiple days forecast."""

    def __init__(
        self, forecast: Forecast, dailyForecast: DailyForecast
    ) -> None:
        """Init the DailyWeatherForecastResponse instance.

        Args:
            forecast (python_weather.forecast.Forecast): the forecast for the current day.
            dailyForecast (python_weather.forecast.dailyForecast): The forecast for another day in the future.
        """
        super().__init__(forecast)
        self.dailyForecast = dailyForecast

    def __get_date_forecast(self):
        return self.dailyForecast.date

    def __get_temperatures(self):
        return {
            "high": self.dailyForecast.highest_temperature,
            "low": self.dailyForecast.lowest_temperature,
            "average": self.dailyForecast.temperature,
        }

    def _get_sun_info(self):
        return {
            "rise": self.dailyForecast.sunrise,
            "light": self.dailyForecast.sunlight,
            "set": self.dailyForecast.sunset,
        }

    def __get_moon_info(self):
        return {
            "rise": self.dailyForecast.moonrise,
            "phase": self.dailyForecast.moon_phase,
            "set": self.dailyForecast.moonset,
            "light": self.dailyForecast.moon_illumination,
        }

    def get_forecast_payload(self) -> dict:
        """Return the payload for a daily forecast object.

        Returns:
            dict: a daily forecast.
        """
        return {
            "location": self.get_location(),
            "date": self.__get_date_forecast(),
            "temperature": self.__get_temperatures(),
            "ephemeride": {
                "sun": self._get_sun_info(),
                "moon": self.__get_moon_info,
            },
        }

    def __repr__(self) -> str:
        """Get a string representation of an instance of this object."""
        return "forecast temperature is {} the {} in {}".format(
            self.get_forecast_payload()["temperature"]["average"],
            self.get_forecast_payload()["date"],
            self.get_forecast_payload()["location"]["name"],
        )
