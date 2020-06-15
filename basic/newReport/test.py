from openpyxl import Workbook
from openpyxl.worksheet.pagebreak import Break

wb = Workbook()
ws = wb.active
row_number = 10
page_break = Break(id=row_number)
ws.page_breaks.append(page_break)