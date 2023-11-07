num_list = []
for i in range(10):
    num_list.append(int(input()) % 42)

unique_list = []
for num in num_list:
    if num not in unique_list:
        unique_list.append(num)

print(len(unique_list))
