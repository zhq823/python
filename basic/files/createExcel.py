import sys, os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

with open("{}/text.xlsx".format(curPath), 'a', encoding="utf-8") as f:
    text = "第一个python文件"
    f.write()
f.close()