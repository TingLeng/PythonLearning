def hi(name="Leng Ting"):
    return('Hello, ' + name)

print(hi())
greet = hi

del hi
#print(hi())
print(greet())
