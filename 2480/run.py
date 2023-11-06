a, b, c = map(int, input().split())

if a == b and b == c and c == a:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
elif c == a:
    print(1000 + c * 100)
else:
    if a < b:
        biggest = b
    else:
        biggest = a
    if biggest < c:
        biggest = c
    print(biggest * 100)
