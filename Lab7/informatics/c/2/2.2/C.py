sum = 0
cnt = 0
element = int(input())
while element != 0:
    sum += element
    cnt += 1
    element = int(input())

print(sum / cnt)