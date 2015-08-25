#coding:utf8
import sys

'''
1、待解析文件中每行的内容如下：
2015-08-23 00:00:01 INFO controllers.Application ~ 服务器返回的json:{"id":1440259201159,"state":{"code":1,"msg":"操作已完成"},"data":{"ucid":100191750,"gameName":"新三国争霸","nickName":"九游玩家100191750","password":"","sid":"ash1bd8d394f-dac8-40ba-9a0d-996    40b5b9272128916","timeout":3600}},[gameId=22135,service=ucid.user.pageSid]
2、"按service归类统计调用的游戏ID列表"结果类似如下：
ucid.user.pageSid 2 4924,22135
3、"统计UV"结果类似如下：
8000
'''

import re

def set2String(gidSet):
    '''
    将Set转换成一个字符串，元素之间用英文逗号隔开
    '''
    result = ""
    for gid in gidSet:
        if 0 != len(result):
            result += ","
        result += gid
    
    return result

def statGameGroupByService(filePath):
    '''
    按service归类统计调用的游戏ID列表
    '''
    serviceMap = {}
    fo = open(filePath, "r")
    try:
        while True:
            line = fo.readline()
            if 0 == len(line):
                break
            index = line.find("[gameId=")
            if -1 != index:
                temp = line[index:].strip()
                arr = temp.split(",")
                service = arr[1][8:-1]
                gameId = arr[0][8:]
                gidSet = serviceMap.get(service)
                if None == gidSet:
                    serviceMap[service] = set([gameId])
                else:
                    gidSet.add(gameId)
        kvList = serviceMap.items();
        for k,v in kvList:
            print k, len(v), set2String(v)
    finally:
        fo.close()

def statUv(filePath):
    '''
    统计UV
    '''
    ucidSet = set([])
    fo = open(filePath, "r")
    try:
        while True:
            line = fo.readline()
            if 0 == len(line):
                break
            arr = re.findall(r"\"ucid\":[0-9]+", line)
            if None != arr and len(arr) > 0:
                ucid = arr[0].split(":")[1]
                ucidSet.add(ucid)
    finally:
        fo.close()
    print "用户数:",len(ucidSet)
    for ucid in ucidSet:
        print ucid

if __name__ == '__main__':
    errMsg = '''错误的参数！
使用方法：
    python ACServerAppAnalyze.py game|uv 文件完整路径
例：
    python ACServerAppAnalyze.py game /home/jws/logs/acserver/application.2015-08-23
    python ACServerAppAnalyze.py uv /home/jws/logs/acserver/application.2015-08-23'''
    if len(sys.argv) != 3:
        print errMsg
        sys.exit(1)
    action = sys.argv[1]
    logPath = sys.argv[2]
    if "game" == action:
        statGameGroupByService(logPath)
    elif "uv" == action:
        statUv(logPath)
    else:
        print errMsg
