def group_checker(string):
    num_list: list[str] = []
    for index, c in enumerate(string):
        if index == 0:
            num_list += c
        elif c != string[index - 1]:
            if c not in num_list:
                num_list += c
            else:
                # not group
                return 0
    # group
    return 1


n = int(input())
res = 0
for i in range(n):
    res += group_checker(input())
print(res)
