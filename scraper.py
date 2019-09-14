import requests
from bs4 import BeautifulSoup
import urllib.request
import progressbar
phrase = input("Phrase: ")

page = 0
count = 0
while True:
    get_soup = requests.get(
        f"https://www.gettyimages.co.uk/photos/rihanna?family=editorial&page={page}&phrase={phrase}&sort=mostpopular")
    soup = BeautifulSoup(get_soup.text, "lxml")
    pics = soup.findAll("img", {"class": "gallery-asset__thumb gallery-mosaic-asset__thumb"})
    for pic in progressbar.progressbar(pics, prefix=f"Crawling Pictures [{phrase}]"):
        try:
            urllib.request.urlretrieve(pic.get("src"), f"{pic.get('alt')}.jpg")
        except:
            pass
    page +=1
