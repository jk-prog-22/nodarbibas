# Saraksts jeb List līdzīgs array, jeb masīvs
# indeksi        0           1          2         3        4
iepirkumi = ["sviests", "biezpiens", "piens", "krejums", "olas"]

#Izdrukāt visu sarakstu
print(iepirkumi)

#Izdrukāt vienu konkrētu elementu, ar attiecīgu indeksu
print(iepirkumi[2])

#Elementu pievienošana beigās
iepirkumi.append("jogurts")

#Elementa pievienošana konkrētā pozīcijā
iepirkumi.insert(2, "siers")

#Izdrukāt visu sarakstu
print(iepirkumi)

#Izdzēst konkrētu elementu
iepirkumi.remove("krejums")

#Izdrukāt visu sarakstu
print(iepirkumi)

#Izdzēst pēdējo, vai pēc indeksa
iepirkumi.pop()
iepirkumi.pop(1)

#Izdrukāt visu sarakstu
print(iepirkumi)

#Atrast elementa indeksu
indeks = iepirkumi.index("olas")
print("Olas indeks", indeks)


# praktisks piemērs
if "piens" in iepirkumi:
    # ja tiešām ir tad vienkārši dzēšam
    iepirkumi.remove("piens")

    # dzēst atrodot indeksu
    # indeks = iepirkumi.index("piens")
    # iepirkumi.pop(indeks)

print(iepirkumi)

iepirkumi.sort()

print(iepirkumi)


print("Saraksta garums", len(iepirkumi))