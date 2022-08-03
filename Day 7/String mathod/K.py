a = "mohan is a good boy, mohan play cricket, mohan also sing a song"

b = a.find("a")
print(b)

while(b != -1):
    b = a.find("a", b+1)
    print(b)
