# for cikla_mainigais in vertiba_kurai_var_iet_cauri:
#     cikla komandas,
#     kas ir jaizpilda

iepirkumi = ["sviests", "biezpiens", "piens", "krejums", "olas"]

for prece in iepirkumi:
    print(prece)

vards = "Māris"

for burts in vards:
    print(burts)


# break - iziet ārā no cikla
# continue - pāriet pie nākamās iterācijas
print("=================================================")
skaitli = [1, 2, 5, 4, 3, 9, 8, 7, 11, 4]

for skaitlis in skaitli:
    if skaitlis % 2 == 0:
        print(skaitlis)

print("=================================================")
for skaitlis in skaitli:
    if skaitlis % 2 != 0:
        continue

    print(skaitlis)

print("=================================================")
for skaitlis in skaitli:
    if skaitlis % 2 == 0:
        if skaitlis == 8:
            break
        
        print(skaitlis)