list = [1, 2, 3, 4]

it = iter(list)
res = ""
for x in it:
    res += "%d,"%(x)
res = res[:-1]
print(res)