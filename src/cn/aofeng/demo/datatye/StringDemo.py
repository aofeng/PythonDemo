#coding:utf-8

def format():
    '''格式符说明：
    %s   字符串（采用str()的显示）
    %r   字符串（采用repr()的显示）
    %c   单个字符
    %b   二进制整数
    %d   十进制整数
    %i   十进制整数
    %o   八进制整数
    ％x   十六进制整数
    %e   指数（基底写为e）
    %E   指数（基底写为E）
    %f   浮点数
    ％F   浮点数
    %g   指数（e）或浮点数（根据显示长度）
    %G   指数（E）或浮点数（根据显示长度）
    %%   字符"%"
    '''
    # 单个占位符替换
    template = "my name is %s"
    print(template % "小明")
    
    # 多个占位符替换 - 使用元组传值给模板
    template = "this file's author is %s, it has %d line, and create time is %s"
    print( template % ("NieYong", 100, "2016年2月22日") )

    # 多个占位符替换 - 使用字典传值给模板
    # 字符串占位符格式：%(name)s
    # 数值型占位符格式：%(name)d
    template = "this file's author is %(authorName)s, it has %(lineNum)d line, and create time is %(cTime)s"
    print( template % {"authorName":"NieYong", "lineNum":100, "cTime":"2016年2月22日"} )

def join():
    '''字符串拼接'''
    a = "Hello"
    b = "中国"
    c = a+b
    print(c)   # Hello中国
    
    d=""
    d+=a
    d+=b
    print(d)   # Hello中国

def find():
    '''在字符串内查找字符或字符串。在Python 2.7.x下测试，一个汉字的空间按3个英文字符计算'''
    src = "hello,26个字母，汉字,天地之间"
    print(src.find("26"))   #6
    print(src.find("字"))   #11
    print(src.find("不存在"))   #-1

def iterator():
    '''历遍字符串'''
    src = "hello,26个字母,汉字"
    for c in src:
        print(c)

def reverse():
    '''逆序(翻转)字符串'''
    src = "abcdergh0123456789"
    dest = src[::-1]
    print(dest)   # 9876543210hgredcba

def sub():
    '''截取部分字符串；分割字符串'''
    src = "abcdergh0123456789"
    subStr = src[1:3]
    print(subStr)   # bc
    print(src.split('0'))   # ['abcdergh', '123456789']

def replace():
    '''部分字符串替换'''
    src = "abcdergh0123456789"
    dest = src.replace("h01", "-")
    print(dest)   # abcderg-23456789

def length():
    src = "abcdergh0123456789"
    print( len(src) )   # 18

format()
join()
find()
iterator()
reverse()
sub()
replace()
length()
