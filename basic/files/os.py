import sys
import os

curpath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curpath)[0]
sys.path.append(rootPath)

print("abspath", os.path.abspath("."))
print("dirname", os.path.dirname(__file__))
print("os.path", os.path.split(curpath)[0])
print("curpath", curpath)
print("rootPath", rootPath)
print("getcwd", os.getcwd())
