from dotenv import load_dotenv
import os
import requests
from datetime import datetime
import pytz

load_dotenv()

weather_api_key = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric&lang=fi"
    response = requests.get(url).json()
    # print(response)

    if response["cod"] == 200:
        # Convert sunrise and sunset times to Helsinki/Finland time
        helsinki_tz = pytz.timezone("Europe/Helsinki")
        # Use fromtimestamp with UTC timezone instead of deprecated utcfromtimestamp
        sunrise_utc = datetime.fromtimestamp(response["sys"]["sunrise"], tz=pytz.UTC)
        sunset_utc = datetime.fromtimestamp(response["sys"]["sunset"], tz=pytz.UTC)
        sunrise_local = sunrise_utc.astimezone(helsinki_tz)
        sunset_local = sunset_utc.astimezone(helsinki_tz)

        # Format sunrise and sunset times
        sunrise_time = sunrise_local.strftime("%H.%M")
        sunset_time = sunset_local.strftime("%H.%M")

        print(
            f"Sää - {response['name']}\n"
            f"{response['weather'][0]['description']}, tuuli: {response['wind']['speed']}m/s\n"
            f"lämpötila: {response['main']['temp']}°C"
            f" (tuntuu {response['main']['feels_like']}°C)"
        )
        print(f"Auringonnousu: {sunrise_time}, Auringonlasku: {sunset_time}")
    else:
        print(f"City '{city}' not found! (response: {response})")


if __name__ == "__main__":
    get_weather("Helsinki")
