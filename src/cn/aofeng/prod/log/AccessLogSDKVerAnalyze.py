#coding:utf8
import json
import re
import sys

'''统计哪些游戏使用了服务端的SDK（包括版本号和语言类型）。文件中每一行的内容如下：
{"reqTime":"2015-10-08T00:00:37.468CST","service":"account.verifySession","request":{"service":"account.verifySession","id":1444233637434,"client":{"si":"","os":"","fr":"","ve":"","ex":"language:php|version:1.0.1","caller":"","pi":"","sve":"","mve":"","frForDb":""},"game":{"cpId":2***2,"gameId":5****1,"channelId":"","serverId":0,"serverName":"","roleId":"","roleName":"","roleLevel":"","zoneId":"","zoneName":"","apkChannelId":""},"data":"{\"sid\":\"ssh1gamee16b082661e74d2c9e07b78262b3d9cf198620\"}","encrypt":"md5","sign":"756053aa870b0ffaff5fdab3ce6f854c","ip":"101.251.212.178","from":""},"response":{"id":1444233637434,"state":{"code":1,"msg":"操作成功","updateFreq":12},"data":"{\"accountId\":\"69a244c8dcc**********a9aaa7051b3\",\"nickName\":\"玩家55*****89\",\"creator\":\"JY\"}"},"execTime":5}

统计结果类似如下：
gameId sdkVer
564320 java-1.0.0
575267 php-1.0.1
543451 php-1.0.1
559548 php-1.0.1
553780 java-1.0.0
'''

def stat(filePath):
    gameSDK = {}
    fo = open(filePath, "rb")
    try:
        line = fo.readline()
        while 0 != len(line):
            line = line[25:]
            obj = json.loads(line.strip())
            request = obj.get("request")
            gameId = request.get("game").get("gameId")
            langVerStr = request.get("client").get("ex")
            langVerArr = re.split("[|:]", langVerStr)
            gameSDK[gameId] = langVerArr[1] + "-" + langVerArr[3]
            
            line = fo.readline()
    finally:
        fo.close()
    
    return gameSDK

if __name__ == '__main__':
    if (2 != len(sys.argv)):
        print '''参数错误！
用法:
    python  AccessLogSDKVerAnalyze.py [filePath]
示例:
    python  AccessLogSDKVerAnalyze.py /home/nieyong/temp/sdkserver_access.log'''
        sys.exit(1)
    filePath = sys.argv[1]
    gameSDK = stat(filePath)
    print "gameId sdkVer"
    kvList = gameSDK.items()
    for k,v in kvList:
        print k, v