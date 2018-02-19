#
# WeatherData is a Weather Data Library which retrieves weather data from many locations in the world. The data is from https://openweathermap.org https://openweathermap.org
#
# Inputs: 1.Name of the city (default=Moscow) 2. Name of the Country (default=ru) 3. The Units of the measuerments - Metric or Imperial (default=metric)
# Output: 1. A dictionary of weather parameters: a. Temperature b.Humidity c.Cloud description d. Wind speed
#         2. A log file of weather data from https://openweathermap.org which is saved in WeatherDataLog.txt

import urllib.request
import json
import io


def WeatherData(city='Moscow', country='ru', units='metric'):

    city_country = city + ',' + country
    api_key = '50668ca470446067dbdd84d496de8898'
    weatherDataLogFile = 'WeatherDataLog.txt'

    #Getting data from openweathermap.org
    try:
        f = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather"
                                   "?q=%s&appid=%s&units=%s" % (city_country, api_key, units))
    except:
        print("Impossible to connect to http://api.openweathermap.org")

    f1 = io.TextIOWrapper(f, encoding='utf-8')
    weather = f1.read()
    weather_json = json.loads(weather)
    #Logging
    with open(weatherDataLogFile, "w") as log:
        log.write(weather)
    #Creating weather data Dict
    weatherData = {}
    weatherData['curr_temp'] = round((weather_json['main']['temp']))
    weatherData['humidity'] = (weather_json['main']['humidity'])
    cloud = (weather_json['weather'][0])
    weatherData['cloud_description'] = cloud['description']
    weatherData['wind_speed'] = weather_json['wind']['speed']
    f.close()

    return weatherData




if __name__ == '__main__':

    print(WeatherData('Haifa', 'il', 'metric'))
