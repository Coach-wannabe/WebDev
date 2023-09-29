n = int(input())
ans = ""

while n != 0:
    if(n % 2 == 0): ans += '0'
    else: ans += '1'

    n //= 2

print(ans)