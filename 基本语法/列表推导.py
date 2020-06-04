# 矩阵变换
from matrix import get
list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
list2 = get(list)
print(list2)
# 集合
a = set("adjajakjdajkajd")
print(a)
b = [x for x in a]
print(b)
# 字典
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
