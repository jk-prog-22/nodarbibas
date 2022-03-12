print("==================== 1. variants ===================")
# 1. variants
for i in range(1, 10):
    for j in range(1, 10):
        print(i, end="")
        if i == j:
            break

    print()

print("==================== 2. variants ===================")
# 2. variants
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, end="")
    print()