tem = "我是不落幕的爱恋" 
if isinstance(tem, str) == True:
    print("这个比真帅")
else:
    print("这个比6啊")

a, b = 0, 1
while b < 10:
    print(b)
    print(b, end=',')
    a, b = b, a+b

c, d = 1, '1'
print(c == d)