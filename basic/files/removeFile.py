import sys, os, pathlib

rootPath = os.path.split(pathlib.Path(__file__).parent)[0]
sys.path.append(rootPath)
print(os.path, type(os.path))
print(pathlib.Path(__file__), type(pathlib.Path(__file__)))
print(sys.path)

from package import matrix



list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(matrix.get(list))