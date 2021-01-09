from utils import NetworkHelper, Commons
from weather.models import Temperature


class WeatherService(NetworkHelper):
    def __init__(self):
        super().__init__(Commons.OWM_BASE_URL.value)

    def getWeatherCity(self, city: str) -> (str, Temperature):
        params = {"q": city, "units": "metric", "lang": "it", "isFindCall": False}
        data = self.get(params)
        print(data)
        weather = data["weather"][0]
        return weather["description"], Temperature.fromJson(data["main"]),

    def getWeatherPhrase(self, city: str, weatherCondition: str, temperature: Temperature) -> str:
        return f"A {city} il tempo è: {weatherCondition}. La temperatura attuale è di {temperature.actual} gradi, " \
               f"percepita di {temperature.feels} gradi. La minima e la massima di oggi saranno rispettivamente di " \
               f"{temperature.min} gradi e di {temperature.max} gradi."


if __name__ == '__main__':
    weather = WeatherService()
    print(weather.getWeatherCity("Bussero"))