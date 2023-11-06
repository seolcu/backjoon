t = int(input())
list_of_tuples = []
for i in range(t):
    a, b = map(int, input().split())
    list_of_tuples.append((a, b))
for a_tuple in list_of_tuples:
    print(a_tuple[0] + a_tuple[1])
