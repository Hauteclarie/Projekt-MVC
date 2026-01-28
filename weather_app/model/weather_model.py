import requests
from weather_app.config.app_config import AppConfig


class WeatherModel:
    """
    Model odpowiedzialny za komunikację z API pogodowym.
    """

    def __init__(self):
        self.config = AppConfig()

    def get_weather(self, city):
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "units": "metric",
            "appid": self.config.API_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            raise ValueError(data.get("message", "Błąd API"))

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "rain_chance": data.get("rain", {}).get("1h", 0)
        }
