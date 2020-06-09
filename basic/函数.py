'''
    【position, keyword】
    一、定义函数遵循：定义的先是position argument，后是keyword  argument
    二、使用函数的默认值： 函数的默认值必须作为最后的参数来定义
    三、同理，因为函数定义要求带有默认值的参数在后，所以调用函数，keyword argument也应该放在后面
    否则会报错：例如 def plugin(a=1, b): 应该将a=1放后面，否则会报错
    【总结：不管是定义函数、调用函数，带有默认值的关键词入参必须放在后面】
    【不带=在前，带=的在后】
'''

# 函数的作用域
a, b = 520, 250



def plugin():
    print("a的值是：%d" % a)


def utils():
    b = 1314
    print("b的值是：{}".format(b))

# plugin()
# utils()


# 函数的入参
def customPlugin(a, b=2, c=3):
    pass

customPlugin(1, b=2, c=3)