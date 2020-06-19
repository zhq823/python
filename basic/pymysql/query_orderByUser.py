import sys
import os
import json

rootPath = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(rootPath)

# 引入SQL ExportExcel
from package.SQLEditor.index import SQLEditor
from package.SQL.index import MySQL
from package.ExportExcel.index import ExportExcel


# 生成SQLEditor实例
SQLInstance = SQLEditor(host="47.111.36.56", port=3306, user="tom.jin", passwd="15850798154")
dataList = SQLInstance.Query(MySQL('MSD_User_car').get())
response = dataList['response']
print(response)

# 生成exportExcel实例
exportExcelInstance = ExportExcel()
excelDataList = [
    ["叫车人姓名", "使用次数", "用车花费", "服务公里数", "均单价"]
]
excelDataList.extend([[item['DspName'], item['Qty'], item['SettleAmount'], item['Kilometre'], item['Price']] for item in response])
exportExcelInstance.exportSheetByUser(dataList=excelDataList)