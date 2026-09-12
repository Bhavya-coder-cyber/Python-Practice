import os
import csv
from bs4 import BeautifulSoup
import requests

CSV_FILE = "hn_top20.csv"
HN_URL = "https://news.ycombinator.com/"

def fetch_top_news():
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")

    links_list = []
    for link in post_links:
        title = link.text.strip()
        url = link.get("href").strip()
        links_list.append({"Title": title, "URL": url})
    print(f"Successfully fetched {len(links_list)} links")
    return links_list

def write_to_csv(data):
    if not data:
        print("Data does not exist")
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "URL"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Successfully wrote to {CSV_FILE}")

def main():
    print("Scraping Hacker News Top 20...")
    links_list = fetch_top_news()
    write_to_csv(links_list)

if __name__ == "__main__":
    main()