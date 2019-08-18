import requests, sys
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse

def URLCollector():
    # URL = input("ENTER URL : ")

    URL = "https://www.alexa.com/topsites"

    try:
        page = requests.get(URL)
    except Exception as e:
        print(e)
        print("\nCouldn't load page : Enter Valid URL in format https://www.example.com")
        return []

    soup = bs(page.content, 'html.parser')

    body =soup.find("body")

    lists = body.findAll("div", {"class": "site-listing"})

    urls = []
    for item in lists:
        url = item.find("div", {"class": "DescriptionCell"}).find('a').text
        urls.append(url)


    return urls

if __name__ == "__main__":

    urls = URLCollector()

    for url in urls:
            print(url)
