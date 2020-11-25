"""Engeto, Python academy, Projekt 3 - election scraper"""

import sys
import csv
from pprint import pprint
import requests
from bs4 import BeautifulSoup as bs


def hlavni() -> None:
    # ziskani odkazu
    odpoved = vytvor_pozadavek(url)
    print("ziskavam data...")
    parsered = zpracuj_pozadavek(odpoved.text)
    okres, kody, odkazy = udaje_okresu(parsered)
    
    # ziskani zahlavi
    odpoved_zahlavi = vytvor_pozadavek(odkazy[0])
    parsered_zahlavi = zpracuj_pozadavek(odpoved_zahlavi.text)
    zahlavi_csv = zahlavi(parsered_zahlavi)
    
    # zapis do csv
    soubor = "volby2017_" + okres + ".csv"
    if zapis_csv(soubor, zahlavi_csv, odkazy, kody):
        print(f'zapsano do souboru: {soubor}')
    else:
        print("nelze ulozit")
        

def vytvor_pozadavek(url: str) -> requests.models.Response:
    try:
        with requests.Session() as se:
            return se.get(url)
    except:
        print("spatny link")
        sys.exit()
        
    
def zpracuj_pozadavek(odpoved: str) -> bs:
    return bs(odpoved, "html.parser")


def udaje_okresu(data: bs) -> list:
    okres = data.find_all("h3")[1].text.strip().replace("Okres: ", "")
    list_okresu = data.find_all("td", {"class": "cislo"})
    list_kodu = []
    list_odkazu = []
    for i in list_okresu:
        list_kodu.append(i.text)
        list_odkazu.append("https://volby.cz/pls/ps2017nss/" 
                            + i.find("a").get("href"))
    return okres, list_kodu, list_odkazu


def zahlavi(data: bs) -> list:
    list_zahlavi = ["Kod obce",
                    "Obec", 
                    "Volici v seznamu", 
                    "Vydanych obalek", 
                    "Platnych hlasu"]
    sloupce = ["t1sa1 t1sb2", "t2sa1 t2sb2"]
    for i in sloupce:
        strany = data.select('td[headers="{}"]'.format(i))
        for i in strany:
            list_zahlavi.append(i.text)
    return list_zahlavi


def zpracovani_obce(data: bs) -> list:
    obec = data.find_all("h3")[2].text.strip().replace("Obec: ", "")
    volici = data.find("td", {"headers": "sa2"}).text
    obalky = data.find("td", {"headers": "sa3"}).text
    platne_hlasy = data.find("td", {"headers": "sa6"}).text
    hlasy_stran = []
    sloupce = ["t1sa2 t1sb3", "t2sa2 t2sb3"]
    for i in sloupce:
        hlasy = data.select('td[headers="{}"]'.format(i))
        for i in hlasy:
            hlasy_stran.append(i.text)
    return obec, volici, obalky, platne_hlasy, hlasy_stran

    
def zapis_csv(soubor: str, zahlavi: list, odkazy: list, kod: list) -> bool:
    print('zapisuji soubor na disk')
    with open(soubor, "w", newline="") as csv_s:
        zapisovac = csv.writer(csv_s)
        zapisovac.writerow(zahlavi)
        
        for index, odkaz in enumerate(odkazy):
            odpoved_obec = vytvor_pozadavek(odkazy[index])
            parsered_obec = zpracuj_pozadavek(odpoved_obec.text)
            sl_B, sl_C, sl_D, sl_E, hlasy = zpracovani_obce(parsered_obec)
            data_obce = [kod[index], sl_B, sl_C, sl_D, sl_E] + hlasy
            zapisovac.writerow(data_obce)
    return True


if __name__ == '__main__':
    url = sys.argv[1]
    hlavni()


