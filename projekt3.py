# Projekt 3 - election parser

import requests
import sys
from bs4 import BeautifulSoup as bs
import csv

# hlavni funkce
def hlavni() -> None:
    # ziskani odkazu
    odpoved = vytvor_pozadavek(url)
    print("ziskavam data...")
    parsered = zpracuj_pozadavek(odpoved.text)
    odkazy = vypis_odkazu(parsered)
    
    # ziskani zahlavi
    odpoved_zahlavi = vytvor_pozadavek(odkazy[0])
    parsered_zahlavi = zpracuj_pozadavek(odpoved_zahlavi.text)
    zahlavi_csv = zahlavi(parsered_zahlavi)
    
    # zpracovani dat
    data = []
    for index, odkaz in enumerate(odkazy):
        odpoved_obec = vytvor_pozadavek(odkazy[index])
        parsered_obec = zpracuj_pozadavek(odpoved_obec.text)
        obec = zpracovani_obce(parsered_obec)
        data.append(obec)
    
    # zapis do csv
    soubor = "volby2017." + nazev_okresu(parsered_zahlavi) + ".csv"
    if zapis_csv(soubor, data, zahlavi_csv):
        print(f'zapsano do souboru: {soubor}')
    else:
        print("nelze ulozit")
        

# pozadavek na server
def vytvor_pozadavek(url: str) -> requests.models.Response:
    try:
        
        with requests.Session() as se:
            return se.get(url)
    except:
        print("spatny link")
        sys.exit()
        
    
# zpracovat odpoved
def zpracuj_pozadavek(odpoved: str) -> bs:
    return bs(odpoved, "html.parser")


# ziskani nazvu okresu 
def nazev_okresu(data: bs) -> str:
    okres = data.find_all("h3")[1].text.strip().replace("Okres: ", "")
    return okres


# ziskani listu s odkazy
def vypis_odkazu(data: bs) -> list:
    list_odkazu = []
    tables = data.find_all("table", {"class": "table"})
    for i in tables:
        odkaz1 = i.find_all("td", {"headers": "t1sa1 t1sb1"})
        odkaz2 = i.find_all("td", {"headers": "t2sa1 t2sb1"})
        odkaz3 = i.find_all("td", {"headers": "t3sa1 t3sb1"})
        for odkaz in odkaz1:
            list_odkazu.append("https://volby.cz/pls/ps2017nss/" + odkaz.find("a").get("href"))
        for odkaz in odkaz2:
            list_odkazu.append("https://volby.cz/pls/ps2017nss/" + odkaz.find("a").get("href"))
        for odkaz in odkaz3:
            list_odkazu.append("https://volby.cz/pls/ps2017nss/" + odkaz.find("a").get("href"))
    return list_odkazu


# zpracovani zahlavi
def zahlavi(data: bs) -> list:
    list_zahlavi = ["Obec", "Volici v seznamu", "Vydanych obalek", "Platnych hlasu"]
    tables = data.find_all("table", {"class": "table"})
    for i in tables:
        strany1 = i.find_all("td", {"headers": "t1sa1 t1sb2"})
        strany2 = i.find_all("td", {"headers": "t2sa1 t2sb2"})
        for strana in strany1:
            list_zahlavi.append(strana.text)
        for strana in strany2:
            list_zahlavi.append(strana.text)
    return list_zahlavi
    

# zpracovani udaju z jednotlivych obci    
def zpracovani_obce(data: bs) -> list:
    list_obce = []
    obec = data.find_all("h3")[2].text.strip().replace("Obec: ", "")
    volici = data.find("td", {"headers": "sa2"}).text
    obalky = data.find("td", {"headers": "sa3"}).text
    platne_hlasy = data.find("td", {"headers": "sa6"}).text
    hlasy_stran = []
    hlasy_stran1 = data.find_all("td", {"headers": "t1sa2 t1sb3"})
    hlasy_stran2 = data.find_all("td", {"headers": "t2sa2 t2sb3"})
    for hlasy in hlasy_stran1:
        hlasy_stran.append(hlasy.text)
    for hlasy in hlasy_stran2:
        hlasy_stran.append(hlasy.text)
    list_obce.append([obec, volici, obalky, platne_hlasy, hlasy_stran])
    return list_obce
        
    
# ulozeni do csv
def zapis_csv(soubor: str, data: list, zahlavi: list) -> bool:
    print(f'zapisuji soubor na disk')
    with open(soubor, "w", newline="") as csv_s:
        zapisovac = csv.DictWriter(csv_s, fieldnames=zahlavi)
        zapisovac.writeheader()
        for index, radek in enumerate(data):
            zapisovac.writerow( # 'Obec', 'Volici v seznamu', 'Vydanych obalek', 'Platnych hlasu', 'Občanská demokratická strana'...
            {
                "Obec": data[index][0][0],
                "Volici v seznamu": data[index][0][1],
                "Vydanych obalek": data[index][0][2],
                "Platnych hlasu": data[index][0][3],
                zahlavi[4]: data[index][0][4][0],
                zahlavi[5]: data[index][0][4][1],
                zahlavi[6]: data[index][0][4][2],
                zahlavi[7]: data[index][0][4][3],
                zahlavi[8]: data[index][0][4][4],
                zahlavi[9]: data[index][0][4][5],
                zahlavi[10]: data[index][0][4][6],
                zahlavi[11]: data[index][0][4][7],
                zahlavi[12]: data[index][0][4][8],
                zahlavi[13]: data[index][0][4][9],
                zahlavi[14]: data[index][0][4][10],
                zahlavi[15]: data[index][0][4][11],
                zahlavi[16]: data[index][0][4][12],
                zahlavi[17]: data[index][0][4][13],
                zahlavi[18]: data[index][0][4][14],
                zahlavi[19]: data[index][0][4][15],
                zahlavi[20]: data[index][0][4][16],
                zahlavi[21]: data[index][0][4][17],
                zahlavi[22]: data[index][0][4][18],
                zahlavi[23]: data[index][0][4][19],
                zahlavi[24]: data[index][0][4][20],
                zahlavi[25]: data[index][0][4][21],
                zahlavi[26]: data[index][0][4][22],
                zahlavi[27]: data[index][0][4][23],
                zahlavi[28]: data[index][0][4][24],
                zahlavi[29]: data[index][0][4][25],
            }
            )
    return True


url = sys.argv[1]   

if __name__ == '__main__':
    hlavni()


