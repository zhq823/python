import pymysql

# 打开数据库连接
'''
    host 数据库服务器存放的IP地址 str
    port 端口号，int
    user 账号 str
    passwd 密码 str
    db 库名 str
    charset 使用utf8 字符编码 str
'''
db = pymysql.connect(host="47.101.30.46", port=4006, user="smartms", passwd="1", db="smartx_temp", charset="utf8")

# 创建一个游标对象
cursor = db.cursor()

# 执行SQL查询
cursor.execute("SELECT * FROM temp_20200420_add as A WHERE A.Column1='上海市'")

# 获取单条数据
data = cursor.fetchone()

# 获取所有数据
dataList = cursor.fetchall()

# print("这是一条测试数据：{}".format(data))
for x in dataList:
    print(x)

db.close()
