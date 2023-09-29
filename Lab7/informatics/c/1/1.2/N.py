n = int(input())

cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in range(n):
    x = int(input())
    if(x == 0): cnt1 += 1
    elif(x > 0): cnt2 += 1
    else: cnt3 += 1

print(cnt1, cnt2, cnt3)