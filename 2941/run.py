string = input()
length = len(string)

for i in range(len(string)):
    if string[i : i + 3] == "dz=":
        length -= 2
    elif string[i : i + 2] in ["c=", "c-", "d-", "lj", "nj", "s="]:
        length -= 1
    elif string[i : i + 2] == "z=" and string[i - 1] != "d":
        length -= 1

print(length)
