# 1. variants
for i in range(1, 100):
    isBumRum = False
    if i % 3 == 0:
        print("Bum", end="")
        isBumRum = True
    
    if i % 5 == 0:
        print("Rum", end="")
        isBumRum = True

    if isBumRum:
        print(", ", end="")
    else:
        print(i, ", ", sep="", end="")

print()
print("==================== 2. variants ==================")
# 2. variants
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print("BumRum,", end=" ")
    elif i % 3 == 0:
        print("Bum,", end=" ")
    elif i % 5 == 0:
        print("Rum,", end=" ")        
    else:
        print(i, ",", sep="", end=" ")