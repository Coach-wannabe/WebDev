cnt = 0

element = int(input())
while element != 0:
    if(element % 2 == 0): cnt += 1
    element = int(input())

print(cnt)