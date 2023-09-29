K = int(input())
countNumber = 0
countFlip = 0
for countNumber in range(1, K+1):
    Number = countNumber
    flip = 0 # нужно инициализировать здесь
    while Number > 0:
        flip = flip * 10 + Number % 10
        Number = Number // 10
    if countNumber == flip:
       countFlip += 1
print(countFlip)