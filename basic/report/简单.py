import sys
import os
import xlwt

rootPath = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
sys.path.append(rootPath)

from package.SQLEditor.index import SQLEditor

instance = SQLEditor()
resouceData = instance.Query("SELECT * FROM ANIMAL")
columns = resouceData['columns']
dataList = resouceData['dataList']
print(dataList)

wb = xlwt.Workbook()
# 设置
style = xlwt.XFStyle()
# 边框
borders = xlwt.Borders()
borders.top = xlwt.Borders.MEDIUM
borders.right = xlwt.Borders.MEDIUM
borders.bottom = xlwt.Borders.MEDIUM
borders.left = xlwt.Borders.MEDIUM
style.borders = borders
# 背景颜色
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5
style.pattern = pattern
# 设置字体
font = xlwt.Font()
font.colour_index = 0x7FFF
style.font = font

# 添加一个表
ws = wb.add_sheet("report")
# 添加表头
ws.write(0, 0, "姓名", style)
ws.write(0, 1, "年龄", style)
ws.write(0, 2, "身高", style)
# 添加body
[[ws.write(x+1, y, value, style) for y, value in enumerate(row)] for x, row in enumerate(dataList)]
ws.col(0).width = 6666
ws.col(1).width = 6666
ws.col(2).width = 6666

wb.save('{}/test.xls'.format(os.path.dirname(__file__)))