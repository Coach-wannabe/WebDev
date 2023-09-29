a = int(input())
n = int(input())

ans = 1

for i in range(1, n + 1):
    ans += a ** i

print(ans)