import requests
from bs4 import BeautifulSoup

def shorten_url(long_url):
    result = requests.post("https://www.shorturl.at/shortener.php", data={"u": long_url})
    return BeautifulSoup(result.text, 'html.parser').find("input", {"id": "shortenurl"}).get('value', "Error: Shortened URL not found.")

def main():
    short_url = shorten_url(input("Enter the URL: "))
    color_code = "\033[1;32m" if 'http' in short_url else "\033[1;31m"
    print(f"=========================\n{color_code}{short_url}\033[0m\n=========================")

if __name__ == '__main__':
    main()