import asyncio
import os

import python_weather


class GetWeatherService:
    def __init__(self, *args, **kwargs) -> None:
        self.town = kwargs["town"]
        self.country = kwargs["country"]

    async def _getweather(self) -> dict:
        temperature: float = None
        temperatures: list = []
        hourly_forecats: list = []

        # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            # fetch a weather forecast from a city
            weather = await client.get(self.town)

            # returns the current day's forecast temperature (int)
            print(weather.temperature)
            temperature = weather.temperature

            # get the weather forecast for a few days
            for daily in weather.daily_forecasts:
                print(daily)
                temperatures.append(daily)

            # hourly forecasts
            for hourly in daily.hourly_forecasts:
                print(f" --> {hourly!r}")
                hourly_forecats.append(hourly)

        return {
            "day_temp": temperature,
            "week_temp": temperatures,
            "hourly_forecasts": hourly_forecats,
        }

    def get_forecast(self):
        if os.name == "nt":
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy()
            )
        return asyncio.run(self._getweather())


# if __name__ == '__main__':
#   # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
#   # for more details
#   if os.name == 'nt':
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

#   asyncio.run(getweather())
