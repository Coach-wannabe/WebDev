from tokenize import Double


a, b = input().split()
a = int(a)
b = int(b)

def power(a, b):
    return a ** b

print(power(a, b))