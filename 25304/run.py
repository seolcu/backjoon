x = int(input())
n = int(input())

value = 0
for i in range(n):
    price, quantity = map(int, input().split())
    value += price * quantity

if x == value:
    print("Yes")
else:
    print("No")
