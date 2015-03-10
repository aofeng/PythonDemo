#coding:utf8
# 字典，对应Java中的Map。
# Key只能是字符串、数值等不可变类型；Value可以是可变类型和不可变类型；Key与Value之间用英文冒号隔开。
# 每个Key-Value对之间用英文逗号隔开，所有的内容位于一对大括号之间。

people = {"name":"NieYong", "age":32, "sex":"M"}

# 获取字典中Key-Value的数量
print "一共有%d个Key-Value" % (len(people))

# 获取指定Key的Value
print "Key'%s'的值为'%s'" % ("name", people.get("name"))

# 历遍所有的Key
keyList = people.keys()
for key in keyList:
    print key

# 历遍所有的Value
valList = people.values()
for val in valList:
    print val

# 同时历遍所有的Key及对应的Value
keyValList = people.items()
for k,v in keyValList:
    print "'%s':'%s'" % (k, v)

# 增加一个Key-Value
people["address"]="广州"
print people.get("address")

# 删除一个Key及其对应的Value
del people["age"]
print people.get("age")
