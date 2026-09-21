import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import wget

BASE_URL = "https://books.toscrape.com/"
IMG_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

def download_image(img_url, filename):
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(8192): # Download in the form of chunks of 8 Kb(8*1024 bytes) ideally.
                f.write(chunk) # We also have libraries to handle the raw content of the response.
    except Exception as e:
        print(f"Failed to download {filename} - {e}")

def scrape_and_download_image():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)

    for book in books:
        img_title = book.h3.a["title"]
        relative_img = book.find("img")["src"]
        img_url = urljoin(BASE_URL, relative_img)

        print(f"url - {img_url}")
        filename = sanitize_filename(img_title) + ".jpg"

        filepath = os.path.join(IMG_DIR, filename)
        print(f"filepath - {filepath}")

        print(f"Downloading {img_url} to {filepath}")
        # download_image(img_url, filepath)

        # Using wget library to download images
        wget.download(img_url, filepath)

    print("All images downloaded successfully")

if __name__ == "__main__":
    scrape_and_download_image()