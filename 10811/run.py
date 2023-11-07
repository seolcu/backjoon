n, m = map(int, input().split())

num_list = list(range(1, n + 1))

for index in range(m):
    i, j = map(int, input().split())
    num_list[i - 1 : j] = reversed(num_list[i - 1 : j])

for num in num_list:
    print(num, end=" ")
