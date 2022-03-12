def ievadiSkaitli():
    while True:
        try:
            ievade = int(input("Lūdzu ievadi skaitli:"))
        except ValueError:
            print("Kļūda! Lūdzu ievadi skaitli!")
            continue
        else:
            return ievade

def help():
    print("Šī bibliotēka ir domāta, lai palīdzētu ikdienas programmēšanā")
    print("Ir pieejamas dažādas funkcijas, piemēram:")
    print("1. ievadiSkaitli, kas validē, ka ievadītais skaitlis tiešām ir skaitlis")
    print("========================================================")
    print("Lai izmantotu šo bibliotēku programmas augšdaļā raksti import helper")

if __name__ == '__main__':
    help()