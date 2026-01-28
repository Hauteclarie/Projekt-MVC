import tkinter as tk
from tkinter import ttk, messagebox
from weather_app.config.app_config import AppConfig


class WeatherView:
    """
    Widok – interfejs graficzny aplikacji.
    """

    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.config = AppConfig()

        self.root.title(self.config.tittle)
        self.style = ttk.Style()

        # Wybór miasta
        self.default_cities = [
            "Warszawa",
            "Kraków",
            "Łódź",
            "Wrocław",
            "Poznań",
            "Gdańsk",
            "Szczecin",
            "Bydgoszcz",
            "Lublin",
            "Białystok",
            "Katowice",
            "Gdynia",
            "Częstochowa",
            "Radom",
            "Sosnowiec",
            "Toruń",
            "Kielce",
            "Rzeszów",
            "Gliwice",
            "Zabrze"
        ]

        self.default_cities.sort()

        #Combobox Wyboru miasta
        self.city_var = tk.StringVar()
        self.city_combo = ttk.Combobox(
            root,
            textvariable=self.city_var,
            values=self.default_cities
        )
        self.city_combo.pack(pady=5)
        self.city_combo.current(0)

        # Przycisk pobierania pogody
        ttk.Button(
            root,
            text="Pobierz pogodę",
            command=self.controller.update_weather
        ).pack(pady=5)

        # Przycisk trybu ciemnego
        ttk.Button(
            root,
            text="Przełącz tryb ciemny",
            command=self.toggle_dark_mode
        ).pack(pady=5)

        # Wyniki
        self.result_label = ttk.Label(root, text="", justify="left")
        self.result_label.pack(pady=10)

        self.apply_theme()

    def apply_theme(self):
        """
        Zmienia wygląd aplikacji (jasny / ciemny).
        """
        if self.config.dark_mode:
            self.root.configure(bg="#2b2b2b")
            self.style.configure("TLabel", background="#2b2b2b", foreground="white")
        else:
            self.root.configure(bg="SystemButtonFace")
            self.style.configure("TLabel", background="SystemButtonFace", foreground="black")

    def toggle_dark_mode(self):
        """
        Przełącza tryb ciemny.
        """
        self.config.dark_mode = not self.config.dark_mode
        self.apply_theme()

    def update_city_list(self, history_cities):
        """
        Aktualizuje listę miast: domyślne + historia bez duplikatów.
        Zachowuje aktualnie wybrane miasto, jeśli istnieje w nowej liście.
        """
        all_cities = []

        for city in self.default_cities + history_cities:
            if city not in all_cities:
                all_cities.append(city)

        current_city = self.city_var.get()

        self.city_combo["values"] = all_cities

        # jeśli aktualnie wybrane miasto jest w liście, zostaw je
        if current_city in all_cities:
            self.city_combo.set(current_city)
        else:
            # w przeciwnym wypadku ustaw pierwsze miasto z listy
            self.city_combo.set(all_cities[0])

    def display_weather(self, weather):
        """
        Wyświetla dane pogodowe.
        """
        text = (
            f" Temperatura: {weather['temperature']} °C\n"
            f" Wilgotność: {weather['humidity']} %\n"
            f" Prędkość wiatru: {weather['wind_speed']} m/s\n"
            f" Szansa na opady: {weather['rain_chance']} %"
        )
        self.result_label.config(text=text)

    def show_error(self, message):
        messagebox.showerror("Błąd", message)
