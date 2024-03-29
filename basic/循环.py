data = [1, 2, 3, 4, 5]
# 一、遍历列表，x为元素，list.index(x) 使用index()查找当前元素在list中的索引
for x in data:
    print(x, data.index(x))

# 二、可以使用range()方法，循环数字序列。
# range(x) 0~x 区间内，增加1
# range(a, x) a~x 区间内，增加1
# range(a, x, c) a~x 区间内，增加C
for x in range(5):
    print(x)

# 三、可以结合使用range和len方法，访问一个有序列表的元素和它的索引
for x in range(len(data)):
    print("data[%d]: %d"%(x, data[x]))

# 四、使用内置方法enumerate，可以同时提供索引和元素
print([{str(index): value} for index, value in enumerate(data)])

# 五、遍历多个序列
questions = ['name', 'age']
answers = ['zhangsan', 18]
for q, a in zip(questions, answers):
    print("{} = {}".format(q, a))


# while循环，python只有前测试 while 循环(满足条件后才执行)，没有类似于JS的 do while 后测试循环语句(满足条件前至少循环一次)
count = 0
sum = 0
num = 100
while count <= num:
    sum += count
    count += 1
    print(sum)

for x in range(5):
    print("第{}次".format(x))
    if x == 2:
        print("xixi")
        pass
        print("hehe")
    else:
        print("haha")

for x in range(5):
    print("循环开始")
    if (x == 2):
        break
    print("循环结束")
