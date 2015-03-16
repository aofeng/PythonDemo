#coding:utf8
# SGMLParser是Python标准库加解析HTML的工具类。
# SGMLParser将HTML分解成8种不同类型的数据，然后调用相应的方法：
# 1）开始标签（Start Tag）。调用start_tagname方法，并传入该标签所有属性列表。如果没有对应的方法，将调用unknown_starttag方法，将传入该标签的名称和属性列表。
# 2）结束标签（End Tag）。调用end_tagname方法。如果没有对应的方法，将调用unknown_endtag方法并传入名称。
# 3）字符引用（Character Reference）。调用handle_charref方法并传入数据。
# 4）实体引用（Entiry Reference）。调用handler_entityref方法并传入数据。
# 5）注释 （Comment）。调用handler_comment方法并传入数据。
# 6）处理指令 （Processing Instruction)。调用handler_pi方法并传数据。
# 7）声明 （Declaration）。调用handler_decl方法并传入数据。
# 8）文本数据 （Text Data)。调用handler_data方法并传入数据。
# 在使用SGMLParser处理HTML数据时，需要继承SGMPParser并覆盖这些方法。

from sgmllib import SGMLParser

class HtmlParser(SGMLParser):

    def reset(self):
        SGMLParser.reset(self)
        self.data = []   # 存储标签的文本内容
        self.findTag = False   # 标志是否找到指定的标签

    def start_a(self, atts):
        ''' 找到A标签 '''
        self.findTag = True

    def end_a(self):
        ''' A标签结束 '''
        self.findTag = False

    def handle_data(self, data):
        ''' 找到文本内容 '''
        if self.findTag:   # 只处理A标签的内容
            self.data.append(data.strip())

# 找开HTML样本文件并读取所有内容
fo = open("HtmlSampler.html", "r")
data = fo.read()

# 使用SGMLParser解析
htmlParser = HtmlParser()
htmlParser.feed(data)
htmlParser.close()

# 输出解析结果
for aVal in htmlParser.data:
    print aVal
