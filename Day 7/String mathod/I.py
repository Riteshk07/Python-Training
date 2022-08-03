a = "mohan is a good boy, mohan play cricket, mohan also sing a song"

b = a.find("mohan")
print(b)

c = a.find("mohan", b+1)
print(c)

d = a.find("mohan", c+1)
print(d)

e = a.find("mohan", d+1)
print(e)

