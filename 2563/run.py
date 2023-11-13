paper = [[0] * 100] * 100

n = int(input())


for i in range(n):
    c, r = map(int, input().split())
    for r_index in range(r, r + 10):
        for c_index in range(c, c + 10):
            paper[r_index][c_index] = 1

print(paper)


count = 0
for row in paper:
    count += sum(row)

print(count)
