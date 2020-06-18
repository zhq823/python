import sys
import os
import json

rootPath = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(rootPath)

from package.ExportExcel.index import ExportExcel
instance = ExportExcel()

with open("{}/orderBySupplier.json".format(os.path.dirname(__file__)), encoding="utf-8") as f:
    data = json.load(f)
    # print(data)
    dataList = [
        ["供应商名称", "供应商性质", "服务次数", "结算金额", "服务公里数", "单公里价格", "均单价"]
    ]
    dataList.extend([[item['supplierName'], item['platform'], item['qty'], item['settleAmount'], item['kilometre'], item['kPrice'], item['price']]for item in data])
    print(dataList)
    instance.exportSheetBySupplier(dataList=dataList)
f.close()