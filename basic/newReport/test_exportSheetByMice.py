import sys
import os
import json

rootPath = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(rootPath)
from package.ExportExcel.index import ExportExcel
instance = ExportExcel()

with open("{}/orderByMice.json".format(os.path.dirname(__file__)), encoding="utf-8") as f:
    data = json.load(f)
    print(data)
    dataList = [
        ["会议编号", "订单量", "金额", "公里数"]
    ]
    dataList.extend([[item['PONum'], item['qty'], item['settleAmount'], item['kilometre']] for item in data])
    print(dataList)
    instance.exportSheetByMice(dataList=dataList)
f.close()