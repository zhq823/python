import pymysql

# 创建连接数据库
db = pymysql.connect(host="47.101.30.46", port=4006, user="smartms", passwd="1", db="test_zhq", charset="utf8")

# 创建游标
cursor = db.cursor()

# 查询数据
cursor.execute("SELECT * FROM ANIMAL as a WHERE a.NAME LIKE '%哈士奇%'")
dataList = cursor.fetchall()

# 输出原始数据
print("原始数据：{}".format(dataList))

# 将原始数据通过for循环，改成list形式输出
result = []
for x in dataList:
    item = []
    for y in x:
        item.append(y)
    result.append(item)
print("for循环实现:{}".format(result))

# 将原始数据通过列表推导，改成list形式输出
response = [[y for y in x] for x in dataList]
print("列表推导实现:{}".format(response))