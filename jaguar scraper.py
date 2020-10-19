import requests
import sys
from bs4 import BeautifulSoup as bs
import csv
from pprint import pprint as pp
import datetime


vstup = input("Zadej nazev znacky: ").lower()
list_bazos = []


# hlavni funkce
def hlavni() -> None:
    odkaz = generator(vstup)
    odpoved1 = vytvor_pozadavek(odkaz)
    nadpisy_inzeratu(odpoved1)
    druha = druha_strana(odpoved1)
    odpoved2 = vytvor_pozadavek(druha)
    nadpisy_inzeratu(odpoved2)

    if zapis_csv(vstup + str(datetime.date.today()), list_bazos):
        print(f'zapsano do souboru {vstup} a casovy udaj')
    else:
        print("nelze ulozit")


# generator odkazu
def generator(vstup: str) -> str:
    odkaz = "https://auto.bazos.cz/inzeraty/" + vstup
    return odkaz


# pozadavek na server
def vytvor_pozadavek(url: str) -> bs:
    with requests.Session() as se:
        odpoved = se.get(url).text
    return bs(odpoved, "html.parser")


# vyhledat udaje
def nadpisy_inzeratu(data: bs) -> list:
    tables = data.find_all("table", {"class": "inzeraty"})

    for index, table in enumerate(tables):
        nadpis = table.find("span", {"class": "nadpis"})
        cena = table.find("span", {"class": "cena"})
        odkaz = "https://auto.bazos.cz" + table.find("a").get("href")
        list_bazos.append([nadpis.text, cena.text, odkaz])

    return list_bazos


def druha_strana(data: bs) -> str:
    div = data.find("div", {"class": "strankovani"})
    odkaz = "https://auto.bazos.cz" + div.find("a").get("href")
    return odkaz


def zapis_csv(soubor: str, data: list) -> bool:
    with open(soubor, "w", newline="") as csv_s:
        zahlavi = "Nadpis inzeratu", "Cena", "Odkaz"
        zapisovac = csv.DictWriter(csv_s, fieldnames=zahlavi)
        zapisovac.writeheader()
        for index, radek in enumerate(data):
            zapisovac.writerow(
                {
                "Nadpis inzeratu": data[index][0],
                "Cena": data[index][1],
                "Odkaz": data[index][2]
                }
            )
    return True


hlavni()
