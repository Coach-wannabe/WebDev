a, b, c, d = input().split()
 
 
def min(a, b, c, d):
    if(a < b and a < c and a < d): return a
    if(b < a and b < c and a < d): return b
    if(c < a and c < b and c < d): return c
    return d
 
 
print(min(a, b, c, d))