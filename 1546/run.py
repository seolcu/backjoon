n = int(input())

num_list = list(map(int, input().split()))

max_num = max(num_list)

new_num_list = list(map(lambda i: (i / max_num) * 100, num_list))

print(sum(new_num_list) / n)
