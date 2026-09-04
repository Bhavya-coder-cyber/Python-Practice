import requests 
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_headers(URL):
    #These are user agent strings that can be used to mimic the behavior of a specific browser or device. Without this, the server may respond with a 403 Forbidden error.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/139.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(URL, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")

    headers_list = []
    for tag in h2_tags:
        header = tag.get_text(strip=True)
        if header and header.lower() != "contents":
            headers_list.append(header)
    print(headers_list)

get_headers(URL)