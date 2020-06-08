# 第几次摸奖
num = int(1)
# 摸奖机会数
total = int(5)
# 中奖数字
guessList = [x for x in range(5)]
# print(guessList)
# 用户输入
tem = int(input("摸奖数字："))
while num <= total:
    res = tem in guessList
    if res:
        print("第" + str(num) + "次摸奖结果：good luck")
        break
    else:
        print("第" + str(num) + "次摸奖结果：sorry")
        num += 1
        if num == total + 1:
            print(str(total) + "次机会结束")
            break
        tem = int(input("please try again:"))
        
    