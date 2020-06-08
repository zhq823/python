print(bin(int(60)))
tem = int(input("十进制转化二进制:"))
arr = []
while True:
    s = tem // 2 # 商
    y = tem % 2 # 余数
    arr.append(y)
    if s == 0:
        arr.reverse()
        arr = [str(i) for i in arr]
        arr = ["ob"] + arr
        res = ''.join(arr)
        print(arr, res)
        break
    tem = s
