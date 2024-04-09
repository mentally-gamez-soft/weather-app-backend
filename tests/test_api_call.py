import unittest

from core.services.weather_call import GetWeatherService


class TestApiCall(unittest.TestCase):
    def test_simple_call(self):
        new_weather_service = GetWeatherService(
            **{"town": "Paris", "country": "france"}
        )
        res = new_weather_service.get_forecast()

        print(res)
