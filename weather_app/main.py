import tkinter as tk
from controller.weather_controller import WeatherController
from config.app_config import AppConfig


def main():
    root = tk.Tk()

    # Ustaw domyślny rozmiar okna (szerokość x wysokość)
    config = AppConfig()
    root.geometry(config.dimensions)

    WeatherController(root)
    root.mainloop()


if __name__ == "__main__":
    main()
