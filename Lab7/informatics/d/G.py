n = int(input())

arr_input = input().split(' ')
arr = [int(num) for num in arr_input]

arr = arr[::-1]
for i in range(n):
    print(arr[i], end=' ')