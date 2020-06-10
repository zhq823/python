import pymysql

db = pymysql.connect(host="47.101.30.46", port=4006, user="smartms", passwd="1", db="test_zhq", charset="utf8")

cursor = db.cursor()

try:
    cursor.execute("DELETE FROM ANIMAL WHERE AGE='522'")
    db.commit()
except:
    db.rollback()

db.close()