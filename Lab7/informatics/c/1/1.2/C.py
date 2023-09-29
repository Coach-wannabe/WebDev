import math

a = int(input())
b = int(input())

for i in range(a, b + 1):
    root = math.sqrt(i)
    if int(root + 0.5) ** 2 == i:  
        print(i)