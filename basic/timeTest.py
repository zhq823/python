import time, sys
# import calendar

# 当前时间
# print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
# 日历
# print(calendar.month(2020, 2))

t0 = time.time()
# # # 延时
time.sleep(1)
# # # 测试运行耗时
print(t0, time.time() - t0)

