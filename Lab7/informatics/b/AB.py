N = int(input())
M = N % 100

if M <= 10 or M >= 20:
    if (N % 10) == 0 or ((N % 10) >= 5 and (N % 10) <= 9):
        print(str(N) + " bochek")
    elif (N % 10) == 1:
        print(str(N) + " bochka")
    else:
        print(str(N) + " bochki")
else:
    print(str(N) + " bochek")