import sqlite3  #робота з базою даних
import requests  #HTTP-запити
import time  #затримка
from datetime import datetime  #дата й час


connection = sqlite3.connect("weather.db") #база дани
cursor = connection.cursor()
# Створюємо таблицю
cursor.execute("""                          
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time TEXT,
    temperature REAL
)
""")
connection.commit()


def get_weather(): #температура
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 48.4647,
        "longitude": 35.0462,
        "current": "temperature_2m",
        "timezone": "Europe/Kyiv"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status() #перевірка на помилки

    data = response.json()
    temperature = data["current"]["temperature_2m"]

    return temperature #погода


def save_weather(temperature): #збереження погоди
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO weather (date_time, temperature) VALUES (?, ?)",
        (date_time, temperature)
    )

    connection.commit()

    print(f"{date_time} | Температура: {temperature} °C")


try:
    while True:
        try:
            temperature = get_weather()
            save_weather(temperature)

        except (requests.RequestException, KeyError, ValueError) as error:
            print("Помилка отримання погоди:", error)

        print("Наступне оновлення через 30 хвилин.")
        time.sleep(1800) #час до ноступного показу погоди

except KeyboardInterrupt:
    print("\nПрограму зупинено.")

finally:
    connection.close()
