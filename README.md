#Python Demo
用于存放博客中文章的Python示例代码和学习过程中实践编写的Python代码片段。
##流程控制
### if else
* [Guess.py](src/cn/aofeng/demo/controlflow/Guess.py)
*  [IfStatement.py](src/cn/aofeng/demo/controlflow/IfStatement.py)

###while
* [WhileStatement.py](src/cn/aofeng/demo/controlflow/WhileStatement.py)

###for
* [ForLoop.py](src/cn/aofeng/demo/controlflow/ForLoop.py)

##函数
* [Function.py](src/cn/aofeng/demo/function/Function.py)
* [DocStrings.py](src/cn/aofeng/demo/function/DocStrings.py)

##数据类型
###字符串
* (StringDemo.py)[src/cn/aofeng/demo/datatye/StringDemo.py]

##数据结构
###列表（List）
* [List.py](src/cn/aofeng/demo/datastructure/List.py)

###集合（Sets）
* [Sets.py](src/cn/aofeng/demo/datastructure/Sets.py)

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

##输入输出
* [StdInput.py](src/cn/aofeng/demo/io/StdInput.py)
* [FileIo.py](src/cn/aofeng/demo/io/FileIo.py)

##操作系统相关
* [DirAndFileAccess.py.py](src/cn/aofeng/demo/os/DirAndFileAccess.py)

##HTTP相关
* [UrllibDemo.py](src/cn/aofeng/demo/http/UrllibDemo.py)
* [SGMLParserDemo.py](src/cn/aofeng/demo/http/SGMLParserDemo.py)
* [BaiduSingerInfo.py](src/cn/aofeng/demo/http/BaiduSingerInfo.py)

##多线程
* [ThreadFunction.py](src/cn/aofeng/demo/thread/ThreadFunction.py)
* [ThreadClass.py](src/cn/aofeng/demo/thread/ThreadClass.py)

##队列
* [生产者消费者](src/cn/aofeng/demo/queue)

##JSON
* [使用Python标准库操作JSON](src/cn/aofeng/demo/json/StandardLibrary.py)

##数据库
###MySQL
* [使用Connector/Python操作MySQL](src/cn/aofeng/demo/mysql)

##NoSQL
###Memcached
* [使用python-memcache操作Memcached](src/cn/aofeng/demo/memcached)

##编程实践
###日志分析
* [AccessLogExecTimeAnalyze.py](src/cn/aofeng/prod/log/AccessLogExecTimeAnalyze.py)
* [AccessLogLoginPvAnalyze.py](src/cn/aofeng/prod/log/AccessLogLoginPvAnalyze.py)
* [MonitorLogAnalyze.py](src/cn/aofeng/prod/log/MonitorLogAnalyze.py)
* [ACServerAppAnalyze.py](src/cn/aofeng/prod/log/ACServerAppAnalyze.py)

###模板
* [CreateNginxHostConfig.py)](src/cn/aofeng/prod/template/CreateNginxHostConfig.py)

# 注意点
* `方法与变量不能使用相同的名称`，否则执行时会报错：`TypeError: 'str' object is not callable`。
* 在子类的__init__方法执行时，并不会自动执行父类的__init__方法，需在子类的代码中显式调用，这与Java不同。
* 支持多重继承，这与Java不同。
* 2.2和之前的版本只能通过经典的方式来实现继承，2.3开始支持通过super的方式实现继承，在可维护性和多重继承上做了改进。
* 不支持自增（++）和自减（--）操作符。
