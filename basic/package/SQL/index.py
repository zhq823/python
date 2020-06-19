import os

class MySQL:

    def __init__(self, name):
        self.name = name

    def get(self):
        sqlFile = open("{0}/{1}.sql".format(os.path.dirname(__file__), self.name), 'r', encoding="utf-8")
        sqlFileList = sqlFile.readlines()  # 读取sql文件，此时是list
        sqlFile.close()  # 读取sql后关闭文件
        sqlFileStr = "".join(sqlFileList)  # list 转化为 str
        return sqlFileStr
