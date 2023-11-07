n, m = map(int, input().split())

num_list = []

for i in range(n):
    num_list.append(0)

for i in range(m):
    start, end, number = map(int, input().split())
    for j in range(start - 1, end):
        num_list[j] = number

for i in range(n):
    print(num_list[i], end=" ")
