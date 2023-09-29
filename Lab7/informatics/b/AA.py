M, N, x, y = int(input()), int(input()), int(input()), int(input())

if N > 1:
    if y == 1:
        print(x, y + 1)
    elif y == N:
        print(x, y - 1)
    else:
        print(x, y - 1)
        print(x, y + 1)
if M > 1:
    if x == 1:
        print(x + 1, y)
    elif x == M:
        print(x - 1, y)
    else:
        print(x - 1, y)
        print(x + 1, y)