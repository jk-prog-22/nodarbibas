import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://www.ss.lv/lv/transport/cars/today/sell/"

def saglabat_lapu():
    pieprasijums = requests.get(URL)

    if pieprasijums.status_code == 200:
        lapa = pieprasijums.text
    else:
        print("Radās kļūda lapas pieprasīšanā!")
        exit()
    
    with open("lapas/lapa_1.html", "w", encoding="UTF-8") as f:
        f.write(lapa)

# saglabat_lapu()

def info():
    with open("lapas/lapa_1.html", "r", encoding="UTF-8") as f:
        html = f.read()

    zupa = bs(html, "html.parser")

    tabulas = zupa.find_all("table")

    # for tabula in tabulas:
    #     print(tabula)
    #     print("============================================")
    #     print("============================================")
    #     print("============================================")
    #     print("============================================")

    autoTabula = tabulas[4]

    rindas = autoTabula.find_all("tr")

    dati = []

    for rinda in rindas[1:-1]:
        auto = {}

        lauki = rinda.find_all("td")
        
        #auto['apraksts'] = lauki[2].a.text.replace("\n", " ")
        auto['gads'] = lauki[4].text

        tilpums = lauki[5].text

        if "D" in tilpums:
            auto["dzinejs"] = "Dīzelis"
            auto["tilpums"] = tilpums[:-1]
        elif "H" in tilpums:
            auto["dzinejs"] = "Hibrīds"
            auto["tilpums"] = tilpums[:-1]
        elif "E" in tilpums:
            # auto["dzinejs"] = "Elektro"
            # auto["tilpums"] = 0
            continue # izlaižam elektro auto un nepievienojam datiem
        else:
            auto["dzinejs"] = "Benzīns"
            auto["tilpums"] = tilpums

        # Uzstādam nobraukumu
        if "-" not in lauki[6].text:
            auto["nobraukums"] = lauki[6].text.replace(" tūkst.", "")
        else:
            continue # ja nav nobraukums ignorējam

        auto["cena"] = lauki[7].text.replace(",", "").replace("  €", "")

        
        if lauki[3].br:
            lauki[3].br.replace_with("!")
            auto["marka"] = lauki[3].text.replace("!", " ")
            auto["razotajs"] = lauki[3].text.split("!")[0]
            auto["modelis"] = lauki[3].text.split("!")[1]
        else:
            auto["marka"] = lauki[3].text
            auto["razotajs"] = lauki[3].text
            auto["modelis"] = lauki[3].text

        dati.append(auto)

    return dati


info()