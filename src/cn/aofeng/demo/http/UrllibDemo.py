#coding:utf8
# 标准库urllib的DEMO
import urllib

# 对请求参数进行urlencode处理
params = {"name":"聂勇", "sex":"M", "nationality":"China"}
encodeParams = urllib.urlencode(params)
print params

# 打开指定的URL
dstUrl = "http://aofengblog.blog.163.com"
try:
    response = urllib.urlopen(dstUrl)
    print "Response Code：", response.getcode()
    print "Response Header：", response.info()   # 如果是打开HTTP URL，info()方法返回的内容是header中的内容。
    print "Response URL：", response.geturl()   # 返回实际的响应地址，如果geturl()方法返回的地址与请求地址不一致，说明发生了跳转
    print "Response Content："
    while True:   # 逐行输出响应内容
        line = response.readline()
        if not line:
            break
        print line.strip()
        
    response.close()
except IOError, ex:
    print "打开URL：%s出错" % (dstUrl)
