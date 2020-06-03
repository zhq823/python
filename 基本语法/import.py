# 同一目录
import function # 引用模块function
print("%s: 引用模块"%function.func())

# 同一目录
import function as newModule # 引用模块function,并对模块重命名为newModule
print("%s: 对模块重命名"%newModule.func())

# 同一目录
from function import func # 引入function模块中的函数func
print("%s: 引入function模块中的函数func"%func())

# 同一目录
from function import func, func2 # 引入function模块中的函数func、func2
print("%s: 引入function模块中的函数func、func2 —— %s"%(func(), func2()))

# 同一目录
from function import * # 引入function模块中所有对象
print("%s: 引入function模块中所有对象 —— %s"%(func(), func2()))

# 同一目录
from function import func # 引入function模块中的函数func
print("%s: 引入function模块中的函数func"%func())

# 同一目录
from function import func as newFunc # 引入function模块中的函数func，并且重命名为newFunc
print("%s: 引入function模块中的函数func，并且重命名为newFunc"%newFunc())

# 不同目录
# import sys
# sys.path.append('/module/function')
# import function as a
# print(a.function())



