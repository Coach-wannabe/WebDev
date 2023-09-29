n = int(input())
arr = [int(part) for part in input().split()]

max1 = -101
max2 = -101
for i in range(n):
    if(arr[i] > max1): max1 = arr[i]

    if(arr[i] < max1 and arr[i] > max2): max2 = arr[i]

print(max2)