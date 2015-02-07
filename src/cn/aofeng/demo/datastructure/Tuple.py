#coding:utf8
# 元组：
# 1) 用圆括号圈住所有元素，元素之间用英文逗号分隔。
# 2) 空元组用一对圆括号表示。
# 3) 如果元组只有单个元素，必须在该元素后加一个英文逗号。
# 4) 元组不可变。

numTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 9)
emputTuple = ()
oneElemTuple = ("A", )

# 统计指定元素的个数
count = numTuple.count(1)
print "元组%s中有%d个数字%d" % ("numTuple", count, 1)

# 
nineIndex = numTuple.index(9)
print "数字%d的首个索引位置是:%d" % (9, nineIndex)

help(tuple)
