print("========== 1. uzdevums =============")
valstis = ["Latvija", "Lietuva", "Igaunija"]

# 1. variants
for valsts in valstis:
    print(valsts, end=" ")

print() # tukša rinda starp variantiem

# 2. variants
print(', '.join(valstis))