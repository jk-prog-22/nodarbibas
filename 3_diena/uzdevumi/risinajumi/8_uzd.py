import random

skaitlis = random.randint(1, 20)
meginajumi = 0

print("Minēšanas spēle! Atmini skaitli intervālā no 1 - 20")

while True:
    minejums = int(input("Ievadi skaitli, kuru gribi uzminēt (0 - iziet):"))
    meginajumi += 1

    if minejums == 0:
        print("Man žēl, ka tu padevies!")
        break    

    if skaitlis == minejums:
        print("Apsveicam ar uzvaru!")
        print("Lai uzvarētu tev tas prasīja", meginajumi, "mēģinājumus.")
        break
    else:
        print("Mēģini vēlreiz...")

