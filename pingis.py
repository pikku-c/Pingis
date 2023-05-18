from itertools import combinations
from tabulate import tabulate
from operator import itemgetter
from random import shuffle


nmb_of_players = int(input("Montako pelaajaa?"))
x = 1
players = []
while x < nmb_of_players:
    player = [input(f"Pelaaja {x}: "), 0, 0]
    players.append(player)
    x += 1
all = players

print()
print("Turnaus alkaa!")
print("Lykkyä pyttyyn kaikille, erityisesti Sohvalle!")
print()

def peli(koti, vieras):
    print(f"Seuraavaksi peli {koti[0]} vs. {vieras[0]}")
    while True:
        tulos = input("Pelin tulos: ")
        if len(tulos) != 3 or tulos[0] not in "012" or tulos[2] not in "012" or tulos[1] != "-" or tulos[0] == tulos[2]:
            print("Tulos ei kelpaa")
        else:
            break
    koti_pisteet = int(tulos.split("-")[0])
    vieras_pisteet = int(tulos.split("-")[1])
    if koti_pisteet == 2:
        if vieras_pisteet == 0:
            koti[2] += 3
        else:
            koti[2] += 2
            vieras[2] += 1
    if vieras_pisteet == 2:
        if koti_pisteet == 0:
            vieras[2] += 3
        else: 
            vieras[2] += 2
            koti[2] += 1
    koti[1] +=1
    vieras[1] += 1
    
    global players
    players = sorted(players, key=itemgetter(2), reverse = True)
    
    sarjataulukko()

def sarjataulukko():
    print()
    sarakkeet = ["Peluri", "Pelattu", "Pisteet"]
    print("Sarjataulukko:")
    print(tabulate(players, headers = sarakkeet, showindex=range(1, len(players)+1)))
    print()

def pelit():
    pelilista = list(combinations(range(0,7), 2))
    shuffle(pelilista)
    for i in pelilista:
       peli(all[i[0]], all[i[1]])
    print(f"Turnauksen voittaja on {players[0][0].upper()}!!")
    print()


pelit()
