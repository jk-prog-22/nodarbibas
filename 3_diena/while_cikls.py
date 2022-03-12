stop = 10
start = 0
step = 1

while start != stop:
    print(start)
    start = start + step

print("Start", start)
print("Stop", stop)
print("Step", step)

start = 0
while start < stop:
    print(start)
    start = start + step

start = 0
stop = 100
while True:
    print("Maris ir super!")
    if start == stop:
        break

    start = start + 1

