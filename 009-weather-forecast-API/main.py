import requests
from datetime import datetime

# Write to text file
def save_weather(city, time, temp, weather):
    file = open("data.txt", "a")
    file.write(f"\n{city}, {time}, {temp}, {weather}")
    file.close()

# Get 5 day weather forcast
def get_weather(city, api_key="c4e92b0f4ba5d7064dc33b9105056006"):
    r = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}")
    content = r.json()
    return content["list"]

def main(city):
    data = get_weather(city)

    for item in data:
        save_weather(city, item["dt_txt"], item["main"]["temp"], item["weather"][0]["description"])

main("montreal")

