import sys
import os
import pathlib


currentPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(currentPath)[0]
sys.path.append(rootPath)

print(currentPath)
print(rootPath)

from package.matrix import get


print(sys.path)


list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(get(list))

# print(os.path.dirname(__file__))
# os.remove("{}/text.txt".format(os.path.dirname(__file__)))
