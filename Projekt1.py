#uvod
ODD = 74 * '='
ODD2 = 74 * '-'
print(f'{ODD}\nVitejte v aplikaci Analyza textu.\nVlozte prosim sve prihlasovaci udaje.\n{ODD}')

#data
dict_USER = {'bob':'123', 'ann' : 'pass123', 'mike': 'password123', 'liz': 'pass123'}
dict_TEXTS = {
  '1':'''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',
  '2': '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',
  '3': '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''' }

#prihlaseni
prepinac = True

while prepinac:
  USER = input('Uzivatel: ')
  if USER in dict_USER.keys():
    print(f'Vitejte {USER}, zadejte heslo.')
    break
  else:
    print('Neznamy uzivatel, zkuste znovu.')
    continue

while prepinac:
  PSWRD = input('Heslo: ')
  if PSWRD == dict_USER[USER]:
    print('Vyborne, pokracujeme.')
    break
  else:
    print('Spatne heslo, zkuste znovu.')
    continue

#vyber textu
print(f'{ODD}\n1:\n{dict_TEXTS["1"]}\n'
      f'{ODD2}\n2:\n{dict_TEXTS["2"]}\n'
      f'{ODD2}\n3:\n{dict_TEXTS["3"]}\n{ODD}')


while prepinac:
  TEXT = input('Vyberte jeden z textu zadanim jeho cisla: ')
  if TEXT in dict_TEXTS.keys():
    print(f'Vybran text č. {TEXT}.')
    break
  else:
    print('Zvolte č. 1 až 3.')
    continue


#analyza textu
atext = dict_TEXTS[TEXT].split()
TOT_WORDS = len(atext)

capital = []
while atext:
    if atext[0].istitle():
        capital.append(atext[0])
    atext = atext[1:]
CAP_WORDS = len(capital)

upper = []
atext = dict_TEXTS[TEXT].split()
while atext:
    if atext[0].isupper():
        upper.append(atext[0])
    atext = atext[1:]
UPP_WORDS = len(upper)

lower = []
atext = dict_TEXTS[TEXT].split()
while atext:
    if atext[0].islower():
        lower.append(atext[0])
    atext = atext[1:]
LOW_WORDS = len(lower)

numerical = []
atext = dict_TEXTS[TEXT].split()
while atext:
    if atext[0].isdigit():
        numerical.append(atext[0])
    atext = atext[1:]
NUM_WORDS = len(numerical)

print(f'{ODD}\n'
      f'Celkovy pocet slov: {TOT_WORDS}\n'
      f'Pocet slov s prvnim velkym pismem: {CAP_WORDS}\n'
      f'Pocet slov psanych jen velkym pismem: {UPP_WORDS}\n'
      f'Pocet slov psanych jen malym pismem: {LOW_WORDS}\n'
      f'Pocet cisel v textu: {NUM_WORDS}\n{ODD}')

graphical =[]
atext = dict_TEXTS[TEXT].split()
while atext:
  graphical.append(len(atext[0]))
  atext = atext[1:]

print('Pocet slov dle jejich delky' + '\n'
  'jednopismenne ' + graphical.count(1) * '*' + str(graphical.count(1))+'\n'
  'dvoupismenne ' + graphical.count(2) * '*' + str(graphical.count(2))+'\n' +
  'tripismenne ' + graphical.count(3) * '*' + str(graphical.count(3))+'\n' +
  'ctyrpismenne ' + graphical.count(4) * '*' + str(graphical.count(4))+'\n' +
  'petipismenne ' + graphical.count(5) * '*' + str(graphical.count(5))+'\n' +
  'sestipismenne ' + graphical.count(6) * '*' + str(graphical.count(6))+'\n' +
  'sedmipismenne ' + graphical.count(7) * '*' + str(graphical.count(7))+'\n' +
  ODD)

soucet = []
atext = dict_TEXTS[TEXT].split()
while atext:
    if atext[0].isnumeric():
        soucet.append(atext[0])
    atext = atext[1:]
soucet = list(map(int, soucet))
SOUCET = sum(soucet)

print(f'Soucet cisel v textu je {SOUCET}.\n{ODD}')