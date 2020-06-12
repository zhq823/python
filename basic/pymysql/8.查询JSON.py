import sys
import os

rootPath = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(rootPath)
print(sys.path)

from package.SQLEditor.index import SQLEditor

instance = SQLEditor()

dataList1 = instance.Query("SELECT * FROM ANIMAL")
dataList2 = instance.Query("SELECT NAME, AGE FROM ANIMAL")

print("查询所有数据：", dataList1)
print("查询指定列：", dataList2)