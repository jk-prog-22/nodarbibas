import math

sk1 = 5 / 3
sk2 = 5

print(sk1 + sk2)
print(sk1, "+", sk2, "=", sk1 + sk2)

rez = sk1 + sk2
print("Rezultāts", rez)

print(sk1 + sk2 + 9)


print("Atņemšana", sk1 - sk2)
print("Reizināt", sk1 * sk2)
print("Dalīšana", sk1 / sk2)
print("Dalīšana vesels", sk1 // sk2)

print("Modulis (nesadalītā daļa) - atlikums", sk1 % sk2) # 13 / 5 ==> 3
# 13 // 5 => 2
# 2 * 5 = 10
# 13 - 10 ==> 3 <==

print("Kāpināšana", sk1 ** 2)
cipariAizKomata = 7
apalots = round(sk1 ** 2, cipariAizKomata)
print("Kāpināšana apaļota", apalots)


malaA = 5
malaB = 4
laukums = malaA * malaB / 2
print()
print("Laukums ir:", laukums)

print(math.pi)