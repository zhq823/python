# 矩阵变换
from module import matrix
list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
list2 = matrix.get(list)
print(list2)
# 集合
a = set("adjajakjdajkajd")
print(a)
b = [x for x in a]
print(b)
# 字典
# 字典可以使用items
dic = {'a': 1, 'b': 2}
dic = dict(a=1, b=2)
print(dic)


def te(data):
    print("这也行,{}={}".format(data, dic[data]))
    return data


print([te(x) for x in dic])

print(dic.values())
print(dic.keys())
newDic = {x: dic[x] for x in dic if x != 'a'}
print(newDic)

# items()将键值对变成元组, 所以就可以有了 (k, v) = tuple()
for (k ,v) in dic.items():
    print(k, v)
print(dic.items())
