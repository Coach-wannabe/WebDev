from tkinter.tix import InputOnly


a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(1001):
    print(i)
    if(a * i * i * i + b * i * i + c * i + d == 0):
        print(i, end=' ')