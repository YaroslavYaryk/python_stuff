import requests

appid = 'APPIID'


class WeatherForecast:
    def __init__(self):
        self.__city_cache = {}

    def get(self, city):
        if city in self.__city_cache:
            return self.__city_cache[city]

        url = f'http://api.openweathermap.org/data/2.5/forecast'

        res = requests.get(url, params={'q': city, 'units': 'metric', 'lang': 'en', 'APPID': appid})
        data = res.json()

        if data['cod'] == '404':
            raise ValueError("City not found")

        forecast = [(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description']) for i in
                    data['list']]

        self.__city_cache[city] = forecast

        return forecast


class CityInfo:
    def __init__(self, city, weather_forecast=None):
        if not isinstance(city, str):
            raise TypeError
        if not city:
            raise ValueError

        self.__city = city
        self.__weather_forecast = weather_forecast or WeatherForecast()

    def weather_forecast(self):
        return self.__weather_forecast.get(self.__city)


def _main():
    try:
        weather = WeatherForecast()
        for i in range(5):
            city = input("Enter a city: ")
            city_info = CityInfo(city, weather)
            forecast = city_info.weather_forecast()
            for item in forecast:
                print(item[0], item[1], item[2])
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    _main()
