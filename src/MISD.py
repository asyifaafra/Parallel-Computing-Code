# MISD - Multiple operations on same data

data = 5

print("MISD Process:")

def operasi1(x):
    return sum(range(1, x + 1))

def operasi2(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

print("Result from Operation 1 =", operasi1(data))
print("Result from Operation 2 =", operasi2(data))