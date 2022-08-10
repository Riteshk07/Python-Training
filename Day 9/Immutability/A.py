x = 15  # new object for int 15

print(x, id(x))

y = x+1 # new object for int 16 

print(y, id(y))

del x

z = 15

print(z, id(z))