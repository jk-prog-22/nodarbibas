"""
==      - salīdzināšanas operators, vai ir vienāds
!=      - vai ir nevienāds
<       - mazāks par
>       - lielāks par
<=      - mazāks vai vienāds
>=      - lielāks vai vienāds
"""

sk1 = 13
sk2 = 7
sk3 = 7

print("sk1 == sk2:", sk1 == sk2)
print("sk1 != sk2:", sk1 != sk2)
print("sk1 < sk2:", sk1 < sk2)
print("sk1 > sk2:", sk1 > sk2)
print("sk1 <= sk2:", sk1 <= sk2)
print("sk1 >= sk2:", sk1 >= sk2)

print("sk2 > sk3:", sk2 > sk3)
print("sk2 >= sk3:", sk2 >= sk3)
print("sk2 <= sk3:", sk2 >= sk3)
print("sk2 < sk3:", sk2 > sk3)

vards1 = "Maris"
vards2 = "maris"
vards3 = "maris"

print("Maris == maris:", vards1 == vards2)
print("maris == maris:", vards2 == vards3)

patiesiba = True
meli = False

print("patiesiba != meli", patiesiba != meli)

# Simbolu virknes  salīdzināšana pēc satura, ieteicams ir casefold, bet var arī lietot lower,
# kas visus burtus pārveido par maziem.
print("viss mazie parbaude", vards1.casefold() == vards2.casefold())
print("viss mazie parbaude", vards1.lower() == vards2.lower())


# AND, OR, NOT(!) operatori
"""
AND - skatās vai abas puses ir True
OR - vai kāda no pusēm ir True

A       B       A and B     A or B      A == B
True    True    True        True        True
True    False   False       True        False
False   True    False       True        False
False   False   False       False       True

"""
sk1 = 1
sk2 = 2
sk3 = 3
sk4 = 3

print("Rezulats AND:", (sk2 > sk1) and (sk3 == sk4))
print("Rezulats AND:", (sk2 < sk1) and (sk3 == sk4))
print("Rezulats OR:", (sk2 > sk1) or (sk3 == sk4))
print("Rezulats OR:", (sk2 < sk1) or (sk3 == sk4))
