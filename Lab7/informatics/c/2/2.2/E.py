max = 0

element = int(input())
while element != 0:
    if(element > max): max = element
    element = int(input())

print(max)