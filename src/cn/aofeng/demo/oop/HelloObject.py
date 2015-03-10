# coding:utf8

class HelloObject:

    def __init__(self):
        ''' 在对类的实例初始化时会调用__init__方法 ,等现于Java类的构造方法'''
        print "类HelloObject的实例初始化完成"

    def sayHello(self):
        ''' 类的方法与普通的函数有一个区别：类的方法的第一个参数必须是self，没有参数的方法也必须携带self '''
        print "Hello, Python!"

    def gather(self):
        ''' 类的方法调用类内部的方法与调用普通的函数有一个区别：调用类内部的方法需通过self对象来调用 '''
        self.sayHello()

ho = HelloObject();
ho.sayHello()
ho.gather()
