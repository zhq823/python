import pymysql
class SQLEditor:

    # 查询列表，输出字典
    def Query(self, sql):
        # 创建连接数据库
        dbkw = self.__ConnectDB()
        # 查询数据
        dbkw["cursor"].execute(sql)
        columns = dbkw["cursor"].description
        dataList = dbkw["cursor"].fetchall()
        columns = [column[0] for column in columns]
        response = [{str(key): item[index] for index, key in enumerate(columns)} for item in dataList]
        return {"dataList": dataList, "columns": columns, "response": response}

    # 仅查询数据list
    def Select(self, sql):
        # 创建连接数据库
        dbkw = self.__ConnectDB()
        # 查询数据
        dbkw["cursor"].execute(sql)
        dataList = dbkw["cursor"].fetchall()
        # 输出
        # print([[y for y in x] for x in dataList])
        self.__CloseDB(dbkw["db"])
        return dataList

    # 增删改等操作。支持组合查询
    def Render(self, *agrs):
        # print(agrs)
        # 创建连接数据库
        dbkw = self.__ConnectDB()
        try:
            [dbkw["cursor"].execute(sql) for sql in agrs]
            dbkw["db"].commit()
        except:
            dbkw["db"].rollback()
        self.__CloseDB(dbkw["db"])

    # 连接数据库
    def __ConnectDB(self):
        db = pymysql.connect(host="47.101.30.46", port=4006, user="smartms", passwd="1", db="test_zhq", charset="utf8")
        cursor = db.cursor()
        return {'db': db, 'cursor': cursor}

    # 关闭数据库
    def __CloseDB(self, db):
        db.close()
