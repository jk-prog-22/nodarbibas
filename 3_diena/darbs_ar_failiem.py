# Atvērt failu

# režīmi: r - lasīšana, w - rakstīšana, izdzēš saturu, a - pievienošana
with open("dati.txt", "a", encoding="utf-8")  as datne:
    datne.write("test\n")
    datne.write("super puper\n")
    datne.write("saule\n")
    # datne.writelines(["Māris","Anna", "Krista"])
    # datne.writelines("Jānis")

#############################################
# Nolasa visu failu, ieliek vienā lielā simbolu virknē
with open("dati.txt", "r", encoding="utf-8") as datne:
    teksts = datne.read()

print(teksts)

#######################################
# Lasīt pa rindiņai
with open("dati.txt", "r", encoding="utf-8") as datne:
    teksts1 = datne.readline()
    teksts2 = datne.readline()


print(teksts1)
print(teksts2)

# Lasīt pa rindiņai
with open("dati.txt", "r", encoding="utf-8") as datne:
    rindina = datne.readline()
    while rindina:
        print("+++", rindina)
        rindina = datne.readline()


#######################################
# Cikliski lasīt visu pa rindiņai, bet viss tiek ielasīts lielā sarakstā
with open("dati.txt", "r", encoding="utf-8") as datne:
    dati = datne.readlines()
    for rindina in dati:
        print("--", rindina)

print(dati)

