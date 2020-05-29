### 判断数据类型
tem = input("is Number:")
isInt = isinstance(tem, int)
isString = isinstance(tem, str)
print("是否为正整数", isInt)
print("是否为字符串", isString)

# type() 查询变量所指的对象类型
a = 'hello world'
print(type(a))