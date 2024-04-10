"""Parse the response of the api call for a today weather forecast."""

from python_weather.forecast import Forecast


class WeatherForecastResponse:
    """Parse the response of a weather api call for crrent day forecast."""

    def __init__(self, forecast: Forecast) -> None:
        """Init the WeatherForecastResponse instance.

        Args:
            forecast (python_weather.forecast.Forecast): the forecast for the current day.
        """
        self.forecast = forecast

    def __get_location(self) -> dict:
        return {
            "name": self.forecast.location,
            "region": self.forecast.region,
            "country": self.forecast.country,
            "latitude": self.forecast.coordinates[0],
            "longitude": self.forecast.coordinates[1],
        }

    def __get_datetime_forecast(self):
        return self.forecast.datetime

    def __get_temperature_feels_like(self):
        return self.forecast.feels_like

    def __get_humidity_rate(self):
        return self.forecast.humidity

    def __get_temperature(self):
        return self.forecast.temperature

    def __get_uv_index(self):
        return self.forecast.ultraviolet

    def __get_wind_info(self):
        return {
            # "direction": self.__get_wind_direction(),
            "speed": self.__get_wind_speed(),
        }

    def __get_wind_direction(self):
        return self.forecast.wind_direction

    def __get_wind_speed(self):
        return self.forecast.wind_speed

    def __get_weather_kind(self):
        return {
            "description": self.forecast.description,
            # "uv": self.__get_uv_index(),
            "icon": self.forecast.kind.emoji,
        }

    def get_forecast_payload(self) -> dict:
        """Return the payload for forecast object for the current day.

        Returns:
            dict: The current day weather forecast.
        """
        return {
            "location": self.__get_location(),
            "date": self.__get_datetime_forecast(),
            "weather": self.__get_weather_kind(),
            "temperature": {
                "real": self.__get_temperature(),
                "feel": self.__get_temperature_feels_like(),
                "humidity": self.__get_humidity_rate(),
            },
            "wind": self.__get_wind_info(),
        }

    def __repr__(self) -> str:
        """Get a string representation of an instance of this object."""
        return "forecast temperature is {} in {}".format(
            self.get_forecast_payload()["temperature"]["real"],
            self.get_forecast_payload()["location"]["name"],
        )
