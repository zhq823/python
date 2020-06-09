import os

# r 只读 (mode 参数是可选的; 'r' 将是默认值。)
# w 只用于写 (如果存在同名文件则将被删除)
# 和 'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾
# 'r+' 同时用于读写
with open("{}/text.txt".format(os.path.dirname(__file__)), 'a', encoding="utf-8") as f:
    text = "第一个python文件\n"
    f.write(text)
f.close()
