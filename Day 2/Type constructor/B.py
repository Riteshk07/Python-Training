# a = int("45")
# a = int("45.56")  # ValueError: invalid literal for int() with base 10: '45.56


# a = int("True") # ValueError:
# a = int("2+4j") # ValueError:


# a = int(20.55)
# a = int(True)
# a = int(False)
a = int(5+2j)

b = 45

print(type(a))

c = a+b

print(c)