N = int(input())

sum = 1
f = 1
for g in range(1, N + 1):
    f = f / g
    sum += f

print(sum)