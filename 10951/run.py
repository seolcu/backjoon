while True:
    try:
        string = input()
    except EOFError:
        break
    try:
        a, b = map(int, string.split())
    except ValueError:
        break
    print(a + b)
