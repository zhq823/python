### hello world
print("hello world")

### 求平方和
sumPlugin = sum(x * x for x in range(10))
print("平方和:", sumPlugin)

### 判断数据类型
tem = input("is Number:")
isInt = isinstance(tem, int)
isString = isinstance(tem, str)
print("是否为正整数", isInt)
print("是否为字符串", isString)

### 中文编码
print("你好，世界")
print("python")
