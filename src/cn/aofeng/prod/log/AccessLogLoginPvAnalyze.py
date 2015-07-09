#coding:utf8
import sys
import commands
import datetime

''' access日志文件按小时切分，1天生成24个文件，文件名格式：access.log.yyyy-mm-dd-hh，如：access.log.2015-05-13-19
access日志每行是一个方法的访问明细数据，包含请求和响应数据，采用JSON格式，但请求和响应的data字段值从JSON对象转义成了字符串。示例：
{"reqTime":"2015-05-14T04:00:00.381CST","service":"account.login","request":{"service":"account.login","id":1431547200528,"client":{"si":"20150409191108990683","os":"android","fr":"API Level-18 - Bird-","ve":"4.0.1","ex":"imei:864131020519888|imsi:460027739286277|model:Bird LT01|net:wifi|mobi:|resX:960|resY:540|mac:00:0a:f5:0b:74:30|orient:L|uuid:900513dd-99b6-4b79-acda-32bf54eff27e","caller":"","pi":"","sve":"","mve":""},"data":"{\"loginFrom\":2,\"password\":\"******************************************************************************************\",\"encrypt\":1,\"name\":\"799872391\"}","encrypt":"md5","sign":"","ip":"118.248.33.200"},"response":{"id":1431547200528,"state":{"code":13,"msg":"验证码为空","updateFreq":12},"data":"{\"isCheckCaptcha\":1}"},"execTime":3} '''

def addData(first, second):
    if None == first or None == second:
        return
    
    for hour, value in second.items():
        if None == first.get(hour):
            first[hour] = value
        else:
            first[hour]["totalLoginPv"] += value["totalLoginPv"]
            first[hour]["autoLoginPv"] += value["autoLoginPv"]
            first[hour]["manLoginPv"] += value["manLoginPv"]

def execShell(cmd):
    print "执行指令：", cmd
    status, result = commands.getstatusoutput(cmd)
    if status == 0:
        return int(result)
    return 0

def analyzeFile(data, filePath, hour):
    totalLoginPv = 0
    autoLoginPv = 0
    manLoginPv = 0
    
    # 统计账号登陆PV总量
    cmd = "grep 'account.login' "+filePath+" | wc -l"
    totalLoginPv = execShell(cmd)
    
    # 统计系统自动登陆PV量
    cmd  = "grep 'account.login' "+filePath+" | grep '\\\\\"loginFrom\\\\\":2' | wc -l"
    autoLoginPv = execShell(cmd)
    cmd  = "grep 'account.login' "+filePath+" | grep '\\\\\"loginFrom\\\\\":\\\\\"2\\\\\"' | wc -l"
    autoLoginPv += execShell(cmd)
    
    # 统计用户手动登陆PV量
    manLoginPv = totalLoginPv - autoLoginPv
    
    return {hour: {"totalLoginPv":totalLoginPv, "autoLoginPv":autoLoginPv, "manLoginPv":manLoginPv} }

def analyzeFiles(fileDir, date):
    ''' 从指定的目录下历遍24小时的access.log文件进行服务的请求数据分析 '''
    
    data = {}
    for hour in range(0,24):
        logFilePath = "".join( (fileDir, "access.log.", date, "-", str(hour).zfill(2)) )
        print "[%s] 开始分析文件：%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), logFilePath)
        result = analyzeFile(data, logFilePath, str(hour).zfill(2))
        addData(data, result)
    
    print "%10s, %10s, %10s, %10s" % ("时间", "totalLoginPv","autoLoginPv", "manLoginPv")
    total = {"totalLoginPv":0, "autoLoginPv":0, "manLoginPv":0}
    items = sorted(data.items())
    for key, value in items:
        print "%10s, %10d, %10d, %10d" % (key, value["totalLoginPv"], value["autoLoginPv"], value["manLoginPv"])
        total["totalLoginPv"] += value["totalLoginPv"]
        total["autoLoginPv"] += value["autoLoginPv"]
        total["manLoginPv"] += value["manLoginPv"]
    print "%10s, %10d, %10d, %10d" % ("总计", total["totalLoginPv"], total["autoLoginPv"], total["manLoginPv"])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '''错误的参数！
        使用方法：python AccessLogAnalyze.py 目录完整路径 yyyy-mm-dd
        例：python AccessLogAnalyze.py  /home/jws/logs/account_server/access/ 2015-03-10 '''
        sys.exit(1)
    logDir = sys.argv[1]   # "/home/jws/logs/account_server/access/"
    date = sys.argv[2]   # 2015-03-10
    analyzeFiles(logDir, date)
