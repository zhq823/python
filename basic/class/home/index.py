
import sys
import os
import pathlib

currentPath = pathlib.Path(__file__).parent.parent # os.path.abspath(os.path.dirname(__file__)) 
rootPath = os.path.split(currentPath)[0]
sys.path.append(rootPath)

print(currentPath)
print(rootPath)
print(sys.path)



from function import func

print(func())
