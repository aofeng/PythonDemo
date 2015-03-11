#Python Demo
##流程控制
### if else
* [Guess.py](src/cn/aofeng/demo/controlflow/Guess.py)
* [IfStatement.py](src/cn/aofeng/demo/controlflow/IfStatement.py)

###while
* [WhileStatement.py](src/cn/aofeng/demo/controlflow/WhileStatement.py)

###for
* [ForLoop.py](src/cn/aofeng/demo/controlflow/ForLoop.py)

##函数
* [Function.py](src/cn/aofeng/demo/function/Function.py)
* [DocStrings.py](src/cn/aofeng/demo/function/DocStrings.py)

##数据结构
###列表（List）
* [List.py](src/cn/aofeng/demo/datastructure/List.py)

###元组（Tuple）
* [Tuple.py](src/cn/aofeng/demo/datastructure/Tuple.py)

###字典（Dictionary）
* [Dictionary.py](src/cn/aofeng/demo/datastructure/Dictionary.py)

###序列（Sequence）
* [Sequence.py](src/cn/aofeng/demo/datastructure/Sequence.py)

##面向对象
* [HelloObject.py](src/cn/aofeng/demo/oop/HelloObject.py)
* [ClassAndObjectVariables.py](src/cn/aofeng/demo/oop/ClassAndObjectVariables.py)
* [Inheritance.py](src/cn/aofeng/demo/oop/Inheritance.py)

# 注意点
* `方法与变量不能使用相同的名称`，否则执行时会报错：`TypeError: 'str' object is not callable`。
* 在子类的__init__方法执行时，并不会自动执行父类的__init__方法，需在子类的代码中显式调用，这与Java不同。
* 支持多重继承，这与Java不同。
* 2.2和之前的版本只能通过经典的方式来实现继承，2.3开始支持通过super的方式实现继承，在可维护性和多重继承上做了改进。
