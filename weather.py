import requests, json
def climet(city):
    api_key = "YOUR API"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = city
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
        y = x["main"]


        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        wind_speed = x["wind"]["speed"]
        z = x["weather"]
        weather_description = z[0]["description"]
        return([str(round(current_temperature - 273, 2)), str(current_pressure), str(current_humidity), str(weather_description), str(round(wind_speed*18/5,2))])

    else:
        return ["City Not Found"]
