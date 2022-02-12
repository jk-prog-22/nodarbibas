# kastīte nosaukums - mainīgā nosaukums
# kastītes saturs - vērtība
# kastītes veids - datu tips


# =  operators - piešķiršanas operators
vards = "Māris" # int i = 5; string vards = "Māris"
uzvards = "Danne"
vertejums = 8
attalums = 5.7
irBrilles = True # True vai False

print("vards")
print(vards)
print(uzvards)
print(vertejums)
print(attalums)
print(irBrilles)

print(type(vards)) # datu tips str - string, jeb simbolu virkne
print(type(vertejums)) # datu tips int - integer, jeb vesels skaitlis
print(type(attalums)) # datu tips float - float, jeb racionāli skaitļi (ar komatiem)
print(type(irBrilles)) # datu tips bool - boolean, var sturēt True vai False

# Mainigo nosaukumi https://www.python.org/dev/peps/pep-0008/
# - mainogo nosaukumu vajag veidot tādu, lai tas parādītu to, ko viņš satur.
# - maksimāli jāizvairas no burtu mainīgo lietošanas, piemēram, x, y, z, c, a, b
# - mainīgo nosaukumā var būt cipars, bet mainīgā nosaukums nevar sākties ar ciparu
vards2 = "Otrs"
# - mainīgo nosaukumu sākam mazo burtu, ja tas satur vairākus vardus, nākmao vārdu sākam ar lielo burtu
camelCaseStyle = "stils"
snake_case_style = "stils"
# - visi lielie burti tiek lietoti tad, ja veidojam konstantes, tad lietojam ari apakšsvītras
GRAVITACIJAS_PAATRINAJUMS = 9.8
# - nekādā gadījumā nelietojam garumzīmes vai atstarpes.

mansVards = "Pēteris"
mansVards = "Juris"

print(vards, uzvards, attalums, irBrilles)
print("Vārds:", vards, "Uzvārds:", uzvards, "Attālums līdz mājai:", attalums, "Valkā brilles", irBrilles)
print(f"Vārds: {vards}, Uzvārds: {uzvards}, Attālums: {attalums}")
print("Vārds: " + vards + " Attālums: " + str(attalums))
