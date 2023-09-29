n = int(input())

arr_input = input().split(' ')
arr = [int(num) for num in arr_input]


for i in range(n):
    if(arr[i] % 2 == 0): print(arr[i], end=' ')