import os
import csv
import requests
from datetime import datetime

FILENAME = "weather.csv"

API_KEY = "48c3c5443bd3830123cb0753afb8e94c"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Conditions"])

def get_weather():
    city = input("Enter a city: ").strip().lower()
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["City"].lower() == city and row["Date"] == date:
                print("Weather already exists")
                return 
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print(f"API Error.")
            return
        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]
        with open(FILENAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, city.title(), temp, condition])
            print("Weather added successfully")
    except Exception as e:
        print("Failed to make API call")

def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))
        if len(reader) <= 1:
            print("No logs found")
            return
        for row in reader[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

def main():
    while True:
        print("1. Get Weather")
        print("2. View Logs")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            get_weather()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            break
        else:
            print("Invalid choice")