import sys, os
import json

rootPath = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(rootPath)

# 引入SQL自定义增删改查类
from package.SQLEditor.index import SQLEditor
instance = SQLEditor()

# 执行删除SQL
# instance.Render("DELETE FROM ANIMAL WHERE NAME LIKE '%哈士奇%'")
# 执行查询所有数据
dataList = instance.Select("SELECT * FROM ANIMAL as a WHERE a.NAME LIKE '%哈士奇%'")
# 执行组合SQL操作，插入、更新
instance.Render("INSERT INTO ANIMAL(NAME, AGE, HEIGHT) VALUES('哈士奇{0}', 888{0}, 666{0})".format(len(dataList)), "UPDATE ANIMAL SET AGE = AGE + 1 WHERE NAME='哈士奇1'")
# 执行查询所有数据
dataList = instance.Select("SELECT * FROM ANIMAL as a WHERE a.NAME LIKE '%哈士奇%'")
# 将py数据类型转成JSON
# dataList = json.dumps(dataList)
print(dataList)