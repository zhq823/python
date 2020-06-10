import pymysql

db = pymysql.connect(host="47.101.30.46", port=4006, user="smartms", passwd="1", db="test_zhq", charset="utf8")

cursor = db.cursor()

try:
    cursor.execute("UPDATE ANIMAL SET AGE = AGE + 1 WHERE NAME='哈士奇1'")
    db.commit()
except:
    db.rollback()

db.close()

