n, x = map(int, input().split())
num_list = list(map(int, input().split()))

for num in num_list:
    if x > num:
        print(num, end=" ")
