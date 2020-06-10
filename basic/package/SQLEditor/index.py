import pymysql
class SQLEditor:

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

    def __ConnectDB(self):
        db = pymysql.connect(host="47.101.30.46", port=4006, user="smartms", passwd="1", db="test_zhq", charset="utf8")
        cursor = db.cursor()
        return {'db': db, 'cursor': cursor}

    def __CloseDB(self, db):
        db.close()
