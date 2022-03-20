from pprint import pprint
import requests
import time
from bs4 import BeautifulSoup

class Bot:
    headers = {
    'authority': 'statsroyale.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://statsroyale.com/fr',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cp-extension-installed': 'Yes',
}

    def getPseudo(self, soup):
        try:
            return soup.find("span", {"class": "profileHeader__nameCaption"}).get_text().strip()
        except:
            return None

    def getMaxTrophies(self, soup):
        try:
            div_statistics_profile_statistics = soup.find("div", {"class": "statistics profile__statistics"})
            return int(div_statistics_profile_statistics.find("div", {"class": "statistics__metricCounter ui__headerExtraSmall"}).get_text().strip())
        except:
            return None

    def getTrophies(self, soup):
        try:
            div_statistics_metricCounter_ui_headerExtraSmall = soup.find("div", {"class": "statistics profile__statistics"})
            liste_TR = div_statistics_metricCounter_ui_headerExtraSmall.find_all("div", {"class": "statistics__metricCounter ui__headerExtraSmall"})
            return int(liste_TR[1].get_text().strip())
        except:
            return None

    def getLevel(self, soup):
        try:
            return soup.find("span", {"class": "profileHeader__userLevel"}).get_text().strip()
        except:
            return None

    def getData(self, product_url):
        r = requests.get(product_url, headers=self.headers)
        soup = BeautifulSoup(r.content, "html.parser")
        pseudo = self.getPseudo(soup)
        maxTrophies = self.getMaxTrophies(soup)
        trophies = self.getTrophies(soup)
        level = self.getLevel(soup)
        return {
            "pseudo": pseudo,
            "maxTrophies": maxTrophies,
            "trophies": trophies,
            "level": level,
        }