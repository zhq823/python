import sys
import os
import json

rootPath = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(rootPath)

from package.ExportExcel.index import ExportExcel
instance = ExportExcel()

with open("{}/orderByUser.json".format(os.path.dirname(__file__)), encoding='utf-8') as f:
    data = json.load(f)
    dataList = [
        ["叫车人姓名", "使用次数", "用车花费", "服务公里数", "均单价"]
    ]
    dataList.extend([[item['name'], item['qty'], item['settleAmount'], item['kilometre'], item['price']] for item in data])
    instance.exportSheetByUser(dataList=dataList)
f.close()

