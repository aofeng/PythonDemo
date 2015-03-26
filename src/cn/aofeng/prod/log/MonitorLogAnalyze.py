#coding:utf8
import sys
import os
import re

# monitor日志存储目录。
# monitor日志的文件格式名：monitor.log.yyyy-mm-dd-hh，如：monitor.log.2015-03-19-10
# monitor日志每行一个方法的访问汇总：
# log_time=2015-03-21 00:08:00`service=acconfig.getSecurityKey`req=2006`time=585`failedReq=0`failedTime=0`timePerReq=0.0

def analyzeLine(line):
    ''' 对monitor.log文件中一行数据进行服务的请求数据分析 '''
    
    if line == "":
        return "", {}
    kvList = re.split("`|=", line)
    service = kvList[3]
    serviceData = {"reqTotalNum":int(kvList[5]), "reqTotalTime":int(kvList[7]), "reqFailNum":int(kvList[9])}
    
    return service, serviceData

def addDictData(first, second):
    ''' 对两个Dictionary数据进行累加：将second中的数据累加到first中 '''
    
    if None == first or None == second:
        return
    for service, value in second.items():
        if None == first.get(service):
            first[service] = value
        else:
            first[service]["reqTotalNum"] += value["reqTotalNum"]
            first[service]["reqTotalTime"] += value["reqTotalTime"]
            first[service]["reqFailNum"] += value["reqFailNum"]

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
                addDictData(data, {service:serviceData})
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
