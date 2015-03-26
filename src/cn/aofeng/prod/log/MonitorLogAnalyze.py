#coding:utf8
import sys
import os

# monitor日志存储目录。
# monitor日志的文件格式名：monitor.log.yyyy-mm-dd-hh，如：monitor.log.2015-03-19-10
# monitor日志每行一个方法的访问汇总：
# log_time=2015-03-21 00:08:00`service=acconfig.getSecurityKey`req=2006`time=585`failedReq=0`failedTime=0`timePerReq=0.0

def analyzeLine(line):
    ''' 对monitor.log文件中一行数据进行服务的请求数据分析 '''
    
    if line == "":
        return "", {}
    service = ""
    serviceData = {"reqTotalNum":0, "reqTotalTime":0, "reqFailNum":0}
    for kvStr in line.split("`"):
        kvList = kvStr.split("=")
        if kvList[0] == "service":
            service = kvList[1]
        elif kvList[0] == "req":
            serviceData["reqTotalNum"] += int(kvList[1])
        elif kvList[0] == "time":
            serviceData["reqTotalTime"] += int(kvList[1])
        elif kvList[0] == "failedReq":
            serviceData["reqFailNum"] += int(kvList[1])
    
    return service, serviceData

def analyzeFile(data, filePath):
    ''' 对单个monitor.log文件进行服务的请求数据分析 '''
    
    if not os.path.exists(filePath):
        print "文件%s不存在" % (filePath)
        return data
    fo = open(filePath, "r")
    try:
        while True:
            line = fo.readline()
            if not line:
                break
            if len(line) == 0:
                continue
            service, serviceData = analyzeLine(line)
            if service != "":
                if None == data.get(service):
                    data[service] = serviceData
                else:
                    data[service]["reqTotalNum"] += serviceData["reqTotalNum"]
                    data[service]["reqTotalTime"] += serviceData["reqTotalTime"]
                    data[service]["reqFailNum"] += serviceData["reqFailNum"]
    finally:
        fo.close()
    
    return data

def analyzeFiles(fileDir, date):
    ''' 从指定的目录下历遍24小时的monitor.log文件进行服务的请求数据分析 '''
    
    data = {}
    for hour in range(0,24):
        monitorLogFilePath = "".join( (fileDir, "monitor.log.", date, "-", str(hour).zfill(2)) )
        print "开始分析文件：%s" % (monitorLogFilePath)
        analyzeFile(data, monitorLogFilePath)
    print "%30s, %10s, %10s, %10s" % ("service", "reqTotalNum","reqTotalTime", "reqFailNum")
    for service,value in data.items():
        print "%30s, %10d, %10d, %10d" % (service, value["reqTotalNum"], value["reqTotalTime"], value["reqFailNum"])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print '''错误的参数！
        使用方法：python MonitorLogAnalyze.py 目录完整路径 yyyy-mm-dd
        例：python MonitorLogAnalyze.py /home/jws/logs/account_server/statlog/monitor/ 2015-03-10'''
        sys.exit(1)
    monitorLogDir = sys.argv[1]   # "/home/jws/logs/account_server/statlog/monitor/"
    date = sys.argv[2]   # 2015-03-10
    analyzeFiles(monitorLogDir, date)
