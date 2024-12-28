import requests

def get_weather(city_name, api_key):
    """
    Fetch the current weather for a given city using the OpenWeatherMap API.
    
    Args:
        city_name (str): The name of the city.
        api_key (str): Your OpenWeatherMap API key.
        
    Returns:
        dict: Parsed weather data or an error message.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def display_weather(data):
    """
    Display weather data in a user-friendly format.

    Args:
        data (dict): Weather data from OpenWeatherMap API.
    """
    if "error" in data:
        print("Error fetching weather data:", data["error"])
    elif data.get("cod") != 200:
        print(f"Error: {data.get('message', 'Unknown error')} (Code: {data.get('cod')})")
    else:
        city = data.get("name")
        country = data["sys"].get("country")
        temp = data["main"].get("temp")
        weather_desc = data["weather"][0].get("description")
        humidity = data["main"].get("humidity")
        wind_speed = data["wind"].get("speed")

        print(f"Current Weather in {city}, {country}:\n")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather_desc.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    API_KEY = "890a2a107622a5383b9783c127949ada"

    # Ask the user for a city name
    city = input("Enter the name of the city: ")

    # Fetch and display weather data
    weather_data = get_weather(city, API_KEY)
    display_weather(weather_data)

