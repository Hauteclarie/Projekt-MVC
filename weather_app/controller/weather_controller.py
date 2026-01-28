from weather_app.model.weather_model import WeatherModel
from weather_app.model.history_model import CityHistory
from weather_app.view.weather_view import WeatherView


class WeatherController:
    """
    Kontroler aplikacji.
    """

    def __init__(self, root):
        self.model = WeatherModel()
        self.history = CityHistory()
        self.view = WeatherView(root, self)

    def update_weather(self):
        """
        Pobiera pogodę i zapisuje miasto do historii.
        """
        city = self.view.city_var.get()
        #print("WYBRANE MIASTO:", repr(city))  # DEBUG
        try:
            weather = self.model.get_weather(city)
            self.view.display_weather(weather)

            self.history.add_city(city)
            self.view.update_city_list(self.history.get_history())

        except Exception as e:
            self.view.show_error(str(e))
