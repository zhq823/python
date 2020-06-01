# a, b = 0, 2
# if a and b:
#     print("a、b都是True")
# else:
#     print("a、b至少有一个为False")

# print(a and b)

# if a:
#     print("0是True")
# else:
#     print("0是False")

# 成员运算符
num = 0
guessList = [1, 2, 3, 4, 5]
tem = int(input("摸奖数字："))
res = tem in guessList
while num < 5:
    if num == 4:
        print("5次机会结束")
        break
    print("第" + str(num+1) + "次摸奖")
    if res:
        print("good luck")
        break
    else:
        tem = input("sorry， please try again:")
    num += 1
