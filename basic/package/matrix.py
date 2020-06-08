import sys
import os

# 只会在自身运行是被执行，else：则是被其他模块引入使用
if __name__ == "__main__":
    curpath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curpath)[0]
    sys.path.append(rootPath)
    print(curpath)
    print(rootPath)
    print(sys.path)


def get(data=[]):
    if 'list' in str(type(data)):
        return [[row[index] for row in data] for index in range(len(data[0]))]
    else:
        return data
