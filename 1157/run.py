alphabet_list = [0] * 26

string = input().upper()
for c in string:
    alphabet_list[ord(c) - 65] += 1

indexes = [
    index for index, value in enumerate(alphabet_list) if value == max(alphabet_list)
]

if len(indexes) != 1:
    print("?")
else:
    print(chr(indexes[0] + 65))
