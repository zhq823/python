import pymysql

# 连接数据库
db = pymysql.connect(host="47.101.30.46", port=4006, user="smartms", passwd="1", db="test_zhq", charset="utf8")

# 创建一个游标对象
cursor = db.cursor()

# 执行sql: 如果animal表存在就删除
cursor.execute("DROP TABLE IF EXISTS ANIMAL")

# 执行sql：创建animal表
createTableSQL = """CREATE TABLE ANIMAL(NAME CHAR(50), AGE INT, HEIGHT INT)"""

cursor.execute(createTableSQL)

# 执行sql：查询name="哈士奇"的所有数据
cursor.execute("SELECT * FROM ANIMAL as A WHERE A.NAME='哈士奇'")

# 输出所有符合条件的数据
dataList = cursor.fetchall()

print("查询结果：{}".format(dataList))

for x in dataList:
    print(x)

db.close()
