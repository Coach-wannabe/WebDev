n = int(input())

arr_input = input().split(' ')
arr = [int(num) for num in arr_input]

cnt = 0
for i in range(1, n):
    if(arr[i] > arr[i-1]): cnt += 1

print(cnt)