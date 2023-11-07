string = input()
for ascii_index in range(ord("a"), ord("z") + 1):
    try:
        print(string.index(chr(ascii_index)), end=" ")
    except ValueError:
        print(-1, end=" ")
