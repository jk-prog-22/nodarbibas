virsotne = 5

for i in range(1, virsotne):
    for j in range(i):
        print("*", end="")

    print()

for i in range(virsotne, 0, -1):
    for j in range(i):
        print("*", end="")

    print()