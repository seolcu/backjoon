input()
num_list = input().split()
v = input()

res = 0
for string in num_list:
    if v == string:
        res += 1

print(res)
