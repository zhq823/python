import pymysql

db = pymysql.connect(host='47.101.30.46', port=4006, user='smartms', passwd='1', db='test_zhq', charset='utf8')

cursor = db.cursor()

cursor.execute("SELECT FROM ANIMAL")

columns = cursor.description
dataList = cursor.fetchall()
columns = [column[0] for column in columns]

response = [{str(key): item[index] for index, key in enumerate(columns)} for item in dataList]

print(response)

db.close()
