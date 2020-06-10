# 开爬
import requests
import json
import os

r = requests.get("https://cn.bing.com/")
with open("{}/我的第1个爬虫文件.html".format(os.path.dirname(__file__)), 'a', encoding="utf-8") as f:
    f.write(r.text)
f.close()