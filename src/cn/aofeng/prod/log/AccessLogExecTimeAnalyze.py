#coding:utf8
import sys

''' access日志文件按小时切分，1天生成24个文件，文件名格式：access.log.yyyy-mm-dd-hh，如：access.log.2015-05-13-19
access日志每行是一个方法的访问明细数据，包含请求和响应数据，采用JSON格式，但请求和响应的data字段值从JSON对象转义成了字符串。示例：
{"reqTime":"2015-05-14T04:00:00.381CST","service":"account.login","request":{"service":"account.login","id":1431547200528,"client":{"si":"20150409191108990683","os":"android","fr":"API Level-18 - Bird-","ve":"4.0.1","ex":"imei:864131020519888|imsi:460027739286277|model:Bird LT01|net:wifi|mobi:|resX:960|resY:540|mac:00:0a:f5:0b:74:30|orient:L|uuid:900513dd-99b6-4b79-acda-32bf54eff27e","caller":"","pi":"","sve":"","mve":""},"data":"{\"loginFrom\":2,\"password\":\"******************************************************************************************\",\"encrypt\":1,\"name\":\"799872391\"}","encrypt":"md5","sign":"","ip":"118.248.33.200"},"response":{"id":1431547200528,"state":{"code":13,"msg":"验证码为空","updateFreq":12},"data":"{\"isCheckCaptcha\":1}"},"execTime":3} 

当前程序是分析单个access文件，获取execTime的值分布数据，执行后获得结果类似如下：
{'76': 1, '3': 1, '67': 2}
'''

def analyzeLine(line):
    if (0 == len(line.strip())):
        return -1;
#     obj = json.loads(line, "utf-8")
#     return obj.get("execTime")
    findStr = "execTime"
    startPoint = line.find(findStr)
    return line[(startPoint+len(findStr)+2):-2]

def analyzeFile(filePath):
    execTimeMap = {}
    
    fo = open(filePath, "rb")
    count=0
    try:
        while True:
            line = fo.readline()
            count+=1
            if (count % 1000 == 0) :
                print "已经处理%s行" % (count)
            if (0 == len(line)):
                break;
            execTime = analyzeLine(line)
            if(-1 == execTime):
                continue
            num = execTimeMap.get(execTime)
            if (num):
                num += 1
            else:
                num = 1
            execTimeMap[execTime] = num
    finally:
        fo.close()
    
    return execTimeMap

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '''错误的参数！
        使用方法：python AccessLogExecTimeAnalyze.py 文件完整路径
        例：python AccessLogExecTimeAnalyze.py /home/jws/logs/account_server/access/access.log.2015-07-09-00'''
        sys.exit(1)
    filePath = sys.argv[1]   # "/home/jws/logs/account_server/access/access.log.2015-07-09-00"
    execTimeMap = analyzeFile(filePath)
    print execTimeMap
