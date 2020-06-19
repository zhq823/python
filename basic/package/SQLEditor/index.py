import pymysql
class SQLEditor:

    def __init__(self, host="47.101.30.46", port=4006, user="smartms", passwd="1", charset="utf8"):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.__ConnectDB()
    def test():
        print(666)

    # 查询列表，输出字典
    def Query(self, sql):
        # 查询数据
        self.cursor.execute(sql)
        columns = self.cursor.description
        dataList = self.cursor.fetchall()
        columns = [column[0] for column in columns]
        response = [{str(key): item[index] for index, key in enumerate(columns)} for item in dataList]
        return {"dataList": dataList, "columns": columns, "response": response}

    # 仅查询数据list
    def Select(self, sql):
        # 查询数据
        self.cursor.execute(sql)
        dataList = self.cursor.fetchall()
        # 输出
        # print([[y for y in x] for x in dataList])
        return dataList

    # 增删改等操作。支持组合查询
    def Render(self, *agrs):
        # print(agrs)
        try:
            [self.cursor.execute(sql) for sql in agrs]
            self.db.commit()
        except:
            self.db.rollback()

    # 连接数据库
    def __ConnectDB(self):
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, charset=self.charset)
        self.cursor = self.db.cursor()

    # 关闭数据库
    def close(self):
        self.db.close()
