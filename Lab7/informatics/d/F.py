n = int(input())

arr_input = input().split(' ')
arr = [int(num) for num in arr_input]

cnt = 0
for i in range(1, n - 1):
    if(arr[i] > arr[i-1] and arr[i] > arr[i+1]): cnt += 1

print(cnt)