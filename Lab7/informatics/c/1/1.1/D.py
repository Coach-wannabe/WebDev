n = int(input())
k = int(input())

kk = 1
nn = n 
for i in range(1, k) :
    nn *= n - i 
    kk *= i + 1    
    
print(nn // kk)