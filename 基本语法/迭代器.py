'''
    【迭代器优点】
    使用迭代器不要求事先准备好整个迭代过程中的所有元素。
    迭代器仅仅在迭代到某个元素时才计算该元素，而在这之前或之后元素可以不存在或者被销毁。
    因此迭代器适合遍历一些数量巨大甚至无限的序列
    【next函数特点】
    当生成一个迭代器对象后，使用next一次，迭代步骤就前进一次，也就是只能前进不能后退
'''
import sys
list = [1, 2, 3, 4]

# 使用iter函数
it = iter(list)
res = ""
for x in it:
    res += "%d,"%(x)
res = res[:-1]
print(res)

# 使用next函数
dataSources = ["Jon Snow", "Divid", "Jack"]
newIt = iter(dataSources)
print(next(newIt))
while True:
    try:
        print("我叫{}".format(next(newIt)))
    except StopIteration:
        sys.exit()