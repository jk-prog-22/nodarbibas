sum = 0
skaits = 0

while True:
    ievade = int(input("Ievadi skaitli (0 - lai beigtu):"))
    if ievade == 0:
        break

    if ievade % 2 == 0:
        sum = sum + ievade
        skaits = skaits + 1

if skaits > 0:
    print("Vidējais no pāra skaitļiem:", sum / skaits)
else:
    print("Netika ievadīts neviens pāra skaitlis")