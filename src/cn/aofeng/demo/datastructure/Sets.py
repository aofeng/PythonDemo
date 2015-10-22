#coding:utf8

# 初始化
a = set()
print a

# 添加一个元素
a.add(1)
print a

# 添加一个已经存在的元素
a.add(1)
print a

# 添加一个不存在的元素
a.add(9)
print a

# 删除一个元素
a.remove(1)
print a

# 添加4个元素，再弹出一个元素
a.add(6)
a.add(8)
a.add(7)
a.add(2)
print a
p = a.pop()
print "p=",p
print a