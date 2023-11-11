r, c = 9, 9

mat = [list(map(int, input().split())) for r_index in range(r)]


def get_max_from_matrix(matrix) -> tuple[int, tuple[int, int]]:
    maximum_value = 0
    location = (0, 0)
    for r_index in range(r):
        for c_index in range(c):
            if matrix[r_index][c_index] > maximum_value:
                maximum_value = matrix[r_index][c_index]
                location = (r_index, c_index)
    return maximum_value, location


m, loc = get_max_from_matrix(mat)

print(m)
print(loc[0] + 1, loc[1] + 1)
