import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

BASE_URL = "https://books.toscrape.com/"
STARTUP_PAGE = "catalogue/page-1.html"
TARGET_COUNT = 50
OUTPUT_FILE = "books.json"

def scraoe_books(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price = article.select_one("p.price_color").text.strip()
        books.append({"title": title, "price": price})

    next_url = soup.select_one("li.next > a")
    next_page = urljoin(url, next_url.get("href")) if next_url else None

    return books, next_page

def main():
    collected = []
    current_url = urljoin(BASE_URL, STARTUP_PAGE)
    while len(collected) < TARGET_COUNT and current_url:
        print(f"Scraping {current_url}")
        books, next_url = scraoe_books(current_url)
        collected.extend(books)
        current_url = next_url

    collected = collected[:TARGET_COUNT]
    print(f"Collected {len(collected)} books")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(collected, f, indent=2)

    print(f"Successfully saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()