r, c = map(int, input().split())

mat_a = [list(map(int, input().split())) for r_index in range(r)]
mat_b = [list(map(int, input().split())) for r_index in range(r)]


def matrix_add(matrix_a, matrix_b, row, column):
    return [
        [
            matrix_a[r_index][c_index] + matrix_b[r_index][c_index]
            for c_index in range(column)
        ]
        for r_index in range(row)
    ]


def print_matrix(matrix):
    for r_index in range(len(matrix)):
        for c_index in range(len(matrix[r_index])):
            print(matrix[r_index][c_index], end=" ")
        print("\n", end="")


print_matrix(matrix_add(mat_a, mat_b, r, c))
