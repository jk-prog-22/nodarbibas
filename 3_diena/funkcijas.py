# def funkcijas_nosaukums(arguments1, arguments2 ...):
#     darbibas, kas tiek veiktas
#     iekš funkcijas ar vai bez mainīgajiem

#     return atgriezama_vertiba

def sasveicinaties():
    print("Labdien cienījamais klient!")
    print("Lai jums veiksmīga diena.")

def sasveicinatiesv2(vards):
    print("Labdien cienījamais ", vards, "!", sep="")
    print("Lai jums veiksmīga diena.")
    vards = "Nekas"

def saskaitit(a, b):
    sum = a + b
    return sum

sasveicinaties()
sasveicinaties()
sasveicinaties()


sasveicinatiesv2("Māris")
sasveicinatiesv2("Jānis")
sasveicinatiesv2("Anna")
vards = "Pēteris"
print(vards)
sasveicinatiesv2(vards)
print(vards) # ????


print(saskaitit(1, 2))
skaitlis = 7
rezulats = saskaitit(9, skaitlis)
print(rezulats)

print(saskaitit(skaitlis, skaitlis))

