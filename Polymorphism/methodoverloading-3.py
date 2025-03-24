from multipledispatch import dispatch

@dispatch(int, int)
def product(a, b):
    return a * b

@dispatch(int, int, int)
def product(a, b, c):
    return a * b * c

@dispatch(float, float, float)
def product(a, b, c):
    return a * b * c

print(product(2, 3))        # 6
print(product(2, 3, 4))     # 24
print(product(2.0, 3.4, 5.4))  # 36.72
