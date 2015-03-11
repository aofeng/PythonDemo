# coding:utf8
# 在子类的__init__方法执行时，并不会自动执行父类的__init__方法，需在子类的代码中显式调用，这与Java不同
# 使用super实现继承从Pytho2.3版本开始支持，比经典的继承方式更加容易使用，且可维护性更好

class Human(object):
    def __init__(self, name):
        self.name = name
        self.sex = "unkown"

    def printName(self):
        print "name:", self.name

    def printSex(self):
        print "sex:", self.sex

    def sayHi(self):
        print "风一样的人"

class Male(Human):   # 指定继承自Human
    def __init__(self, name):
        super(Male, self).__init__(name)   # 通过super调用父类Human的初始化方法
        self.sex = "Male"

    def sayHi(self):
        print "风一样的男人"

class Female(Human):   # 指定继承自Human
    def __init__(self, name):
        super(Female, self).__init__(name)   # 通过super调用父类Human的初始化方法
        self.sex = "Female";
    
    def sayHi(self):
        super(Female, self).sayHi()   # 通过super方式调用父类的方法
        print "风一样的女人"

male = Male("XiaoMing")
female = Female("Mary")

male.printName()
male.printSex()
male.sayHi()

female.printName()
female.printSex()
female.sayHi()
