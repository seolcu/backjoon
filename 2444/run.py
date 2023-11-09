n = int(input())

for i in range(0, n):
    print(" " * (-i + n - 1), end="")
    print("*" * (2 * i + 1), end="")
    print("\n", end="")

for i in range(0, n - 1):
    print(" " * (i + 1), end="")
    print("*" * (-2 * i + 2 * n - 3), end="")
    print("\n", end="")
