#coding:utf-8
# 文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开
# 始是详细的描述。

def add(a, b):
    '''数字相加.
    
    传入两个整数：a和b，返回它们相加的结果.'''
    return a+b

def minVal(a, b):
    '''获得最小数.
    
    传入两个整数：a和b，返回最小的数值.'''
    if a > b:
        return b
    else:
        return a

print add.__doc__

help(add)
help(minVal)
