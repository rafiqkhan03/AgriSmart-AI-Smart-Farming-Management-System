import requests


API_KEY = "4ed2b8239357c2034735a9031b38d2b7"


def get_weather(city):

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        "&units=metric"
    )

    response = requests.get(url)

    data = response.json()

    if response.status_code != 200:

        return {
            "error": "City not found"
        }

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind = data["wind"]["speed"]

    # Alert Logic

    if temperature > 35:

        alert = "Heat Alert"
        irrigation = (
            "High temperature detected. "
            "Water crops early morning."
        )

    elif "rain" in weather.lower():

        alert = "Rain Alert"
        irrigation = (
            "Rain expected. "
            "Delay irrigation today."
        )

    else:

        alert = "Normal Weather"
        irrigation = (
            "Weather conditions are normal."
        )

    return {

        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "weather": weather,
        "wind_speed": wind,
        "alert": alert,
        "irrigation_suggestion": irrigation

    }