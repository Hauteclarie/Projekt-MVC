class AppConfig:
    """
    Singleton przechowujący konfigurację aplikacji.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)

            cls._instance.API_KEY = "c26bc5d913310b1a10cf0d0c3aefb4bf"

            # Tryb ciemny (domyślnie wyłączony)
            cls._instance.dark_mode = False

            cls._instance.dimensions = "500x200"
            cls._instance.tittle = "Aplikacja Pogodowa"

        return cls._instance
