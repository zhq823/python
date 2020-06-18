import os
import json
import math
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.pagebreak import Break, RowBreak, ColBreak

from openpyxl.chart import (
    LineChart,
    BarChart,
    Reference,
    Series,
    series_factory
)


class ExportExcel:

    # 构造函数
    def __init__(self):
        pass
    
    # 初始化
    def install(self, *agrs):
        print(agrs)

    # 导出用车明细-叫车人
    def exportSheetByUser(self, dataList = []):
        # 记录当前工作簿有多少的sheet
        self.sheetnames = []
        try:
            # 尝试读取本地文件《销售用车次数、花费.xlsx》
            wb = load_workbook(filename="销售用车次数、花费.xlsx")
            # 每次运行给新sheet添加索引《sheet{index}》
            sheetnames = wb.sheetnames
            ws = wb.create_sheet("sheet{}".format(len(sheetnames)))
        except:
            # 读取本地文件《销售用车次数、花费.xlsx》失败，就新建一个工作簿
            wb = Workbook()
            sheetnames = []
            ws = wb.active
        
        total = len(dataList) # x轴类别长度
        multiple = total/5 # 标准类别长度是5，所以total/5是标准宽度的倍数
        for row in dataList:
            ws.append(row) # 遍历list，向sheet添加数据

        # 用车花费
        c1 = BarChart()
        print(c1.width)
        c1.width = multiple*10
        # x轴类别category，min_col=1,max_col=1 == 取自第一列（这种情况max_col可以省略不写）；min_row=2,max_row=6 意思是从前固定好的第一列，从第2行到第6行取数据作为category
        cats = Reference(ws, min_col=1, max_col=1, min_row=2, max_row=total)
        # 同理第一个图表取自第三列，第2行到第6行的数据作为该图表的数据
        v1 = Reference(ws, min_col=3, min_row=2, max_row=total)
        c1.add_data(v1, titles_from_data=False, from_rows=False)
        c1.set_categories(cats)
        c1.x_axis.title = '叫车人姓名'
        c1.y_axis.title = '用车花费'
        c1.y_axis.majorGridlines = None
        c1.title = '销售用车次数、花费'
        # 自定义系列
        # c1.series = [Series(v1, title="用车花费")]


        # 使用次数
        c2 = LineChart()
        v2 = Reference(ws, min_col=2, min_row=2, max_row=total)
        c2.add_data(v2, titles_from_data=False, from_rows=False) #
        c2.y_axis.axId = 200 # 可能多个公用一个x轴的y轴，所以为了区别不同的y轴，需要设置id，当然你也可以将不同的y轴的id设置一样，那么它们将公用一个y轴
        c2.y_axis.title = "使用次数" # 该轴线的title
        c2.y_axis.crosses = "max" # 设置为max，那么该条轴线将位于系列右侧，默认左侧
        # c2.series = [Series(v2, title="使用次数")] # 自定义系列
        c1 += c2

        ws.add_chart(c1, "G8")

        # 排序
        ws.auto_filter.ref = "A1:E6"
        # ws.auto_filter.add_filter_column(0, ["Kiwi", "Apple", "Mango"])
        ws.auto_filter.add_sort_condition("B2:B6")


        wb.save("销售用车次数、花费.xlsx")
        wb.close()
        print("文件生成成功")
        
