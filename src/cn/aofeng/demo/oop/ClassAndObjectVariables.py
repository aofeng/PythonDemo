#coding:utf8

class ClassAndObjetVariables:
    ''' 类与对象的变量使用 '''
    
    classPublicVar = 9; # class中声明的变量默认为公共类型（Public），为类的所有实例持有同一份数据，任何一个实例修改后都会同步到其他的实例
    __classPrivateVar = "Private" # 以两个下划线开头的变量为私有类型（Private）
    
    def __del__(self):
        ''' __del__方法在对象（实例）被销毁时调用，但被调用的具体时间无法预知 '''
        print "对象已被销毁"
    
    def first(self):
        print "执行的上一个方法是", self.prevMethod
        self.prevMethod = "first"
        
    def second(self):
        print "执行的上一个方法是", self.prevMethod
        self.prevMethod = "second"

caov1 = ClassAndObjetVariables()
caov2 = ClassAndObjetVariables()

# 通过类来修改其成员变量，会影响到这个类的所有实例，包括在修改后创建的实例。caov1、caov2和caov3均输出1
ClassAndObjetVariables.classPublicVar = 1
caov3 = ClassAndObjetVariables()
print "caov1.classPublicVar=", caov1.classPublicVar
print "caov2.classPublicVar=", caov2.classPublicVar
print "caov3.classPublicVar=", caov3.classPublicVar,"\n"

# 通过实例来修改成员变量，只影响实例本身。caiv1输出6，caiv2输出1
caov1.classPublicVar = 6
print "caov1.classPublicVar=", caov1.classPublicVar
print "caov2.classPublicVar=", caov2.classPublicVar,"\n"

# 在Python中，私有变量也是可以被外部直接修改的
caov2.__classPrivateVar = "Change Private Variable Value"
print "caov2.__classPrivateVar=", caov2.__classPrivateVar
