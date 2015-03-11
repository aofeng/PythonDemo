#coding:utf8

# 标准输入：raw_input。从标准输入读取一行并返回一个字符串(去掉结尾的换行)。
name = raw_input("请输入你的名字:")
print name, ", 欢迎你使用Python!"

# 标准输入：input。从标准输入读了一行，但是它假设输入的是一个有效的Python表达式，并返回计算结果。
expression = input("请输入一个Python表达式：")
print "表达式的计算结果是：",expression
