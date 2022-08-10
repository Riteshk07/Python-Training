x = [10,12,45]

print(x, id(x))
print(x[0],x[1],x[2])
print(len(x))

x.remove(12)


print(x, id(x))
print(x[0],x[1])
print(len(x))

# list can shrink