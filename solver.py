import json
from pprint import pprint

maradt_ido = 7 * 24 - ((15-8) * 5 + 7 * 8)

# nevsor = ["VM", "Giliczó Benjámin", "Vikor Tamás 10.A", "Csővári Csaba 12.A", "Hunor Abonyi", "Marcell Bencze", "Máté Csabányi", "Balázs Gáspár", "Balázs Harnóczi", "Lefkovits Jenő Hunor", "János Norbert Kovács", "Zalán Kőrösi", "Patrik Kusztos", "Bencze1 Marcell", "Bence Nyúl", "12A Soós Máté", "Zsolt Szeg", "Aron Szepvolgyi", "Dávid Szlovák", "Máté Tapodi"]
nevsor = ["VM"]
adatok = {}

for nev in nevsor:
    with open("adatok\\"+nev+".json", "r", encoding="utf-8") as fajl:
        betoltott_json = json.load(fajl)
        adatok.update({nev: betoltott_json})


pprint(adatok)

print(f"Heti {24*7} órából {maradt_ido} van minden másra, mint alvás és suli.\nEbből kinek mennyi óra megy el játékkal és hány óra marad bármi másra?")

for felhasznalo, adat in adatok.items():
    sumtime = 0
    for game, playtime in adat["playtime"].items():
        sumtime += playtime
    print(f"{felhasznalo} össz lógása: {sumtime}, tehát így marad heti {maradt_ido - sumtime} óra, ami napi {(maradt_ido - sumtime) // 7} óra 'szabadidőt' jelent")
