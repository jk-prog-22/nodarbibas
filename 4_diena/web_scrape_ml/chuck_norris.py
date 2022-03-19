import requests
import json


kategorija = "dev"
URL = f"https://api.chucknorris.io/jokes/random?category={kategorija}"

lapa = requests.get(URL)

if lapa.status_code == 200:
    #print("Viss ir ok varam strādāt!")
    saturs = lapa.text
    saturs = json.loads(saturs)
else:
    print("Radās kļūda lapas pieprasīšanā!")



print("Joks:", saturs['value'])