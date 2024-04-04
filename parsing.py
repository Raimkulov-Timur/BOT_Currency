import requests
import csv
from bs4 import BeautifulSoup as Bs

URL = "https://www.optimabank.kg/index.php?option=com_nbrates&view=default&Itemid=196&lang=ru"

def usd():
    response = requests.get(url=URL)
    soup = Bs(response.content,"html.parser")
    itembuy = soup.find("div" , class_ = "iso-USD row0").find("div" , class_ = "rate buy").get_text(strip=True)
    itemsell = soup.find("div" , class_ = "iso-USD row0").find("div" , class_ = "rate sell").get_text(strip=True)
    return itembuy,itemsell
a = usd()


def euro():
    response = requests.get(url=URL)
    soup = Bs(response.content,"html.parser")
    itembuy = soup.find("div" , class_ = "iso-EUR row1").find("div" , class_ = "rate buy").get_text(strip=True)
    itemsell = soup.find("div" , class_ = "iso-EUR row1").find("div" , class_ = "rate sell").get_text(strip=True)
    return itembuy,itemsell
b = euro()

def tenge():
    response = requests.get(url=URL)
    soup = Bs(response.content,"html.parser")
    itembuy = soup.find("div" , class_ = "iso-KZT row0").find("div" , class_ = "rate buy").get_text(strip=True)
    itemsell = soup.find("div" , class_ = "iso-KZT row0").find("div" , class_ = "rate sell").get_text(strip=True)
    return itembuy,itemsell
c = tenge()

def rub():
    response = requests.get(url=URL)
    soup = Bs(response.content,"html.parser")
    itembuy = soup.find("div" , class_ = "iso-RUB row1").find("div" , class_ = "rate buy").get_text(strip=True)
    itemsell = soup.find("div" , class_ = "iso-RUB row1").find("div" , class_ = "rate sell").get_text(strip=True)
    return itembuy,itemsell
d = rub()

    
