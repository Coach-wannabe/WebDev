n = int(input())

arr_input = input().split(' ')
arr = [int(num) for num in arr_input]

cnt = 0
for i in range(n):
    if(arr[i] > 0): cnt += 1

print(cnt)