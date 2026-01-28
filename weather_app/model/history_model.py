class CityHistory:
    """
    Singleton przechowujący historię wyszukiwanych miast.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CityHistory, cls).__new__(cls)
            cls._instance.cities = []
        return cls._instance

    def add_city(self, city):
        """
        Dodaje miasto do historii (bez duplikatów).
        """
        if city not in self.cities:
            self.cities.append(city)

    def get_history(self):
        """
        Zwraca listę miast.
        """
        return self.cities
