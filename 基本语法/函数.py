# 同一目录
import function # 引用模块
print(function.func())

# 同一目录
import function as newModule # 对模块重命名
print(newModule.func())

# 同一目录
from function import func # 引入function模块中的函数func
print(func())

# 同一目录
from function import func as newFunc # 引入function模块中的函数func，并且重命名为newFunc
print("%s: 引入function模块中的函数func，并且重命名为newFunc"%newFunc())


