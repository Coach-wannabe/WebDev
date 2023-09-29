from re import T


n = int(input())

flag = False
for i in range(n):
    x = int(input())
    if(x == 0): 
        flag = True
        break

if(flag == True): print("YES")
else: print("NO")