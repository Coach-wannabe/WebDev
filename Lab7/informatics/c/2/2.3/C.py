from tkinter.tix import MAX


n = int(input())
min = 10
max = -1

while n != 0:
    if(n % 10 > max): max = n % 10
    elif(n % 10 < min): min = n % 10
    n //= 10

print(min, max)