import pymysql

# 创建连接数据库
db = pymysql.connect(host="47.101.30.46", port=4006, user="smartms", passwd="1", db="test_zhq", charset="utf8")

# 创建游标
cursor = db.cursor()

# 查询已有的数据，为insert设置新数据的索引
cursor.execute("SELECT * FROM ANIMAL as a WHERE a.NAME LIKE '%哈士奇%'")
dataList = cursor.fetchall()

# 执行sql
insertSQL = """INSERT INTO ANIMAL(NAME, AGE, HEIGHT) VALUES('哈士奇{}', 520, 250)""".format(len(dataList))

try:
    # 执行sql
    cursor.execute(insertSQL)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
