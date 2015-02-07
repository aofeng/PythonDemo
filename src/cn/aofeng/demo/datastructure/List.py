#coding:utf8
#数据结构：列表

fruitList = ["Apple", "Orange", "Watermelon"]

print "fruit count:", len(fruitList)

# 使用for...in历遍
def inLoop():
    print "fruit list:"
    for fruit in fruitList:
        print "   ",fruit
print "\n========== 使用for...in历遍 =========="
inLoop()

# 使用"range+索引"历遍
def rangeLoop():
    print "fruit list:"
    fruitCount = len(fruitList)
    for index in range(fruitCount):
        print "   ",fruitList[index]
print '\n========== 使用"range+索引"历遍 =========='
rangeLoop()

# 反转List
fruitList.reverse();
print "\n========== 反转List中的数据 =========="
rangeLoop()

# 在尾部追加数据
fruitList.append("Banana")
print "\n========== 尾部追加一个数据 =========="
rangeLoop()

# 弹出尾部的数据
print "\n========== 弹出尾部的数据 =========="
item1 = fruitList.pop()
item2 = fruitList.pop()
print "弹出的数据:",item1,", ",item2
rangeLoop()

# List提供的所有方法及说明
help(list)