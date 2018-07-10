import requests
from bs4 import BeautifulSoup
from .models import Currency
# get the web data and do it beautiful by beautiful soup


def scrape():
    r = requests.get("https://www.ecb.europa.eu/rss/fxref-usd.html")
    soup = BeautifulSoup(r.content, "html.parser")

    links = soup.find_all("title")
    splited_link = str(links[1]).split(' ')

    datesplit = splited_link[6].split('-')

    curr = Currency.objects.last()

    try:
        if curr.date.year != int(datesplit[0]) or curr.date.month != int(datesplit[1]) or curr.date.day != int(datesplit[2]):
            create_currency()
    except:
        create_currency()

# Nie zdążyłem, ale zastanowiłbym sie jak zmniejszyć tą funkcje używając fukncji exec()
def create_currency():
    new_curr = Currency()

    r = requests.get("https://www.ecb.europa.eu/rss/fxref-usd.html")
    soup = BeautifulSoup(r.content, "html.parser")

    links = soup.find_all("title")
    splited_link = str(links[1]).split(' ')
    new_curr.USD = splited_link[1].split('>')[1]

    r = requests.get("https://www.ecb.europa.eu/rss/fxref-jpy.html")
    soup = BeautifulSoup(r.content, "html.parser")

    links = soup.find_all("title")
    splited_link = str(links[1]).split(' ')
    new_curr.JPY = splited_link[1].split('>')[1]

    r = requests.get("https://www.ecb.europa.eu/rss/fxref-bgn.html")
    soup = BeautifulSoup(r.content, "html.parser")

    links = soup.find_all("title")
    splited_link = str(links[1]).split(' ')
    new_curr.BGN = splited_link[1].split('>')[1]

    r = requests.get("https://www.ecb.europa.eu/rss/fxref-czk.html")
    soup = BeautifulSoup(r.content, "html.parser")

    links = soup.find_all("title")
    splited_link = str(links[1]).split(' ')
    new_curr.CZK = splited_link[1].split('>')[1]

    new_curr.save()