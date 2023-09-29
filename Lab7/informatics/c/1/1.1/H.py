n = int(input())

ans = 0
for i in range(n + 1):
    ans += 2 ** i

print(ans) 