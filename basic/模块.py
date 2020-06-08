import sys, os
from package import matrix

# print(sys.path)
# print(dir(sys))

# if __name__ == "__main__":
#     print("模块自身被执行")
# else:
#     print("模块被其他模块引入执行")

# print(dir())
list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix.get(list))
