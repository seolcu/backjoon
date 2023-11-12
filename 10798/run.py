r, c = 5, 15

mat = [list(input()) for r_index in range(r)]

for c_index in range(c):
    for r_index in range(r):
        if len(mat[r_index]) - 1 >= c_index:
            print(mat[r_index][c_index], end="")
