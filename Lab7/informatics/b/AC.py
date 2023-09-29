a = int(input())
b = int(input())
c = int(input())

cnt = 0

if(a % 2 == 0): cnt += 1
if(b % 2 == 0): cnt += 1
if(c % 2 == 0): cnt += 1

if(cnt > 0): print("YES")
else: print("NO")