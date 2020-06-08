a, b = 20, 20
print(a is b)
print(id(a) == id(b))

b = 30
print(a is not b)