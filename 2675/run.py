t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    for c in s:
        print(c * r, end="")
    print("\n", end="")
