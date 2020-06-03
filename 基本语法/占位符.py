# %d int
# %s str
# %...还有其他数据类型的占位符

# 跟高级的用法 format
a, b, c = 1, "2", [3]
print("疯狂输出：%d"%(a))
print("疯狂输出：%s"%(b))
print("疯狂输出：{}".format(c))
print("疯狂输出：{}{}".format(c, a))
