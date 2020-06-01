temp=input("我最喜欢的数字:") 
guess = int(temp)
num =1
while guess !=7:
    print(123)
    if num<5:
        guess = int(temp)
        if guess==7:
            print("对了")
            break
        else:
            num =num+1
            if guess >7:
                print("大了")
            else:
                print("小了")
        temp=input("重新猜吧:")
    else:
        print("5次机会用完了")
        break
print("game over")


