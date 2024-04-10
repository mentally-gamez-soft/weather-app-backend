import unittest

from core.services.weather_service import WeatherService


class TestApiCall(unittest.TestCase):
    def test_weather_api_single_day_by_town_country(self):
        new_weather_service = WeatherService()
        res = new_weather_service.get_forecast(
            **{
                "location": "",
                "town": "paris",
                "country": "france",
                "week": False,
            }
        )

        print(res)

        self.assertEqual(
            res["status"], 0, "The service didnt answer correctly !!!"
        )
        self.assertEqual(
            res["day"]["location"]["name"],
            "Paris",
            "The city name is not correct !!!",
        )
        self.assertEqual(
            res["day"]["location"]["region"],
            "Ile-de-France",
            "The region name is not correct !!!",
        )
        self.assertEqual(
            res["day"]["location"]["country"],
            "France",
            "The country name is not correct !!!",
        )

    @unittest.skip(
        "The API is not ready to work with a description of the location"
    )
    def test_weather_api_single_day_by_location(self):
        new_weather_service = WeatherService()
        res = new_weather_service.get_forecast(
            **{
                "location": "Versailles Castle, Versailles France",
                "town": "",
                "country": "",
                "week": False,
            }
        )

        print(res)

        self.assertEqual(
            res["status"], 0, "The service didnt answer correctly !!!"
        )
        self.assertEqual(
            res["day"]["location"]["name"],
            "Paris",
            "The city name is not correct !!!",
        )
        self.assertEqual(
            res["day"]["location"]["region"],
            "Ile-de-France",
            "The region name is not correct !!!",
        )
        self.assertEqual(
            res["day"]["location"]["country"],
            "France",
            "The country name is not correct !!!",
        )
