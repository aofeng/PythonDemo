#coding:utf-8

# Python的函数以关键字def来标识，语法如下：
# def 函数名(参数1, 参数2=defaultValue, ..., 参数N):
#     statement

def add(a, b=1):
    return a+b

def testChangeLocalVar(x):
    x = 2
    print "in function testChange, local var x=", x

def display(a, b, c):
    print "a=", a
    print "b=", b
    print "c=", c

# Python中的pass表示一个空的语句块
def returnNothing():
    pass

# 没有传入参数b，将使用默认值１
print(add(1))

# 传入了参数b，使用传入的值
print(add(1,2))

#局部变量与全局变量同名，但相互不影响
x = 5
print "global var x=", x
testChangeLocalVar(5)
print "global var x=", x

# 调用函数时，指定参数名称，就和函数中参数定义的顺序无关
display(11, 30, 10)
display(c=10, a=11, b=30)

# 没有return语句的函数，默认返回None（表示没有任何东西的特殊类型）
print returnNothing()
