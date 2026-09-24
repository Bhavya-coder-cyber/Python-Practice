import requests
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import schedule
import time

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
    'sparkline': False,
}

CSV_FILE = 'crypto_prices.csv'

def fetch_coin_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

def save_to_csv(data):
    is_present = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not is_present:
            writer.writerow(["timestamp", "coin", "price"])

        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        for coin in data:
            writer.writerow([timestamp, coin["id"], coin["current_price"]])
    print("Data saved successfully")

def plot_graph(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["coin"].lower() == coin_id:
                times.append(row['timestamp'])
                prices.append(row['price'])

    if not times:
        print("No data found for the coin")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(times, prices, marker='o')
    plt.grid()
    plt.tight_layout()
    plt.show()

def job():
    print("Fetching coin data hourly...")
    crypto_data = fetch_coin_data()
    save_to_csv(crypto_data)

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)

# def main():
    
#     print("Fetching coin data...")
#     crypto_data = fetch_coin_data()
#     save_to_csv(crypto_data)
#     coin_id = input("Enter the coin ID: ").strip().lower()
#     if coin_id:
#         plot_graph(coin_id)

# if __name__ == "__main__":
#     main()