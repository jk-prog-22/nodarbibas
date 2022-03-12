iepirkumi = ["sviests", "biezpiens", "piens", "krejums", "olas"]
iepirkumi.append("jogurts")


for i in range(len(iepirkumi)):
    print(iepirkumi[i])


for i in range(10):
    print(i)

print("==============================================")
# range(start, stop, step)
for i in range(10, 20, 2):
    print(i)

print("==============================================")
for i in range(20, 4, -3):
    print(i)

print("==============================================")
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    
    print()