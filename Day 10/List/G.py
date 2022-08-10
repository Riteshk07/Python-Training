x = [10,12,45]

print(x, id(x))

x[0] = 50     # list object is mutable
# x[3] = 32   # IndexError: list assignment index out of range

print(len(x))
print(x, id(x))