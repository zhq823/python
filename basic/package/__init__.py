import sys, os, pathlib

# 跨文件夹引入模块需要添加被引入模块的路径环境变量
# 当import一个模块时，默认从当前目录查找，如果没有就去sys.path查找
if __name__ == "__main__":
    # 同一目录直接from xx import xx
    # 不同目录需要添加环境变量【特别注意的是，这些设置环境变量是在你的文件写的，而不是被引用的模块】
    # 方法一 推荐这种方法
    currentPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(currentPath)[0]
    sys.path.append(rootPath)
    # 方法二
    # pathlib.Path(__file__)是当前文件的完整路径，如果想获取上一级，直接.parent。。。这样比较灵活
    rootPath2 = os.path.split(pathlib.Path(__file__).parent)[0]
    sys.path.append(rootPath2) # sys.path.insert(len(sys.path), rootPath2)
    # 方法三 手动拼写添加也是可以的，不推荐
    # test
    print(sys.path)
    
    # print("自身运行")
else:
    pass
    # print("被调用")