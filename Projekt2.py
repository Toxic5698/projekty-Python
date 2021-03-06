# Projekt 2 Python Academy Engeto - Cows and Bulls
from pprint import pprint
import random
import time
ODD = 59 * "="

# uvitani
print(ODD)
jmeno_hrace = input("Zadejte jmeno hrace: ")

print(ODD + "\n" 
    f'Vitejte ve hre Cows and Bulls, {jmeno_hrace.title()}.\n'
    "Uhadnete 4mistne cislo!\n"
    "Po kazdem pokusu se dozvite,\n"
    "kolik cisel je spravnych a na spravne pozici (bulls) a\n"
    "kolik cisel je spravnych, ale na nespravne pozici (cows).\n"+
    ODD)

# telo hry
def main() -> None:
    # generovani cisla
    skryte_cislo = generator()
    start = time.time()
    print(skryte_cislo)

    # hadani
    pocet_pokusu = 0
    # cas?
    while True:
        pocet_pokusu += 1
        hadane_cislo = hadani()
        konec_hry = porovnani(skryte_cislo, hadane_cislo)
        if konec_hry == 4:
            end = time.time()
            print(f'Vyborne, konec hry. {pocet_pokusu} pokusu za {round(end - start)} sekund.')
            break
        else:
            continue

def generator() -> list:
    skryte_cislo = set()
    while len(skryte_cislo) < 4:
        skryte_cislo.add(random.randint(0, 9))
    return list(skryte_cislo)

def hadani() -> list:
    while True:
        hadane_cislo = input("Zadejte 4mistne cislo: ")
        if len(hadane_cislo) == 4 and hadane_cislo.isdigit():
            break
        else:
            print('Vlozena data nejsou cislo nebo cislo neni 4mistne.')
            continue
    hadane_cislo = [int(i) for i in str(hadane_cislo)]
    return hadane_cislo

def porovnani(skryte_cislo: list, hadane_cislo: list) -> int:
    porovnani_bulls = 0
    porovnani_cows = 0
    a = 0
    b = 0
    for skryte in skryte_cislo:
        if skryte == hadane_cislo[a]:
            porovnani_bulls += 1
        a += 1
    for hadane in skryte_cislo:
        if skryte_cislo[b] in hadane_cislo:
            porovnani_cows += 1
        b += 1
    print(f'{porovnani_bulls} bulls, {porovnani_cows - porovnani_bulls} cows!')
    return porovnani_bulls

main()
