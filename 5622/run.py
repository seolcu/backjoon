time = 0

for c in input():
    if c in "ABC":
        time += 3
    elif c in "DEF":
        time += 4
    elif c in "GHI":
        time += 5
    elif c in "JKL":
        time += 6
    elif c in "MNO":
        time += 7
    elif c in "PQRS":
        time += 8
    elif c in "TUV":
        time += 9
    elif c in "WXYZ":
        time += 10

print(time)
