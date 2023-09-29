n = int(input())
cnt = 0

while n != 0:
    if(n % 10 == 0): cnt += 1
    n //= 10

print(cnt)