#coding:utf8
import sys
import json

'''统计XX助手登陆的UV和PV：
1、每行的数据内容如下：
{"reqTime":"2015-10-21T23:58:37.363CST","service":"account.login","request":{"id":16839563,"client":{"caller":"pphelper","ex":{"ip":"175.42.246.2","os"      :"iOS"}},"data":"{\"name\":\"49*****51\",\"password\":\"*****************************************************************************************\",\"l      oginFrom\":1}","encrypt":"md5","sign":"127b54047*****92abebc*****b5a50c","ip":"121.201.97.6","service":"account.login"},"response":{"id":16839563,"stat      e":{"code":1,"msg":"操作成功"},"data":"{\"ucid\":49*****51,\"st\":\"st5e629db*****5cb90*****0c020473\"}"},"execTime":56}
2、统计结果类似如下：
 PV: 36000036
UV: 1800019 '''

def analyzeLine(line, onlyLoginSuccess=False):
    ''' 从行中解析出登陆的账号，如果账号不符合条件，返回空字符串（""） 
    参数说明：
    line - 一行数据
    onlyLoginSuccess - 只统计登陆成功的数据，默认为统计所有（成功＋失败）的登陆数据'''
    obj = json.loads(line, "utf-8")
    loginInfoStr = obj.get("request").get("data")
    if onlyLoginSuccess:
        responseCode = obj.get("response").get("state").get("code")
        if 1 == int(responseCode):
            loginInfoObj = json.loads(loginInfoStr, "utf-8")
            account = loginInfoObj.get("name")
        else:
            account = ""
    else:
        loginInfoObj = json.loads(loginInfoStr, "utf-8")
        account = loginInfoObj.get("name")
    
    return account;

def analyzeFile(logPath):
    ''' 逐行解析文件内容 '''
    accountSet = set() # 不重复的账号列表
    accountCount = 0;
    fo = open(logPath, "rb")
    try:
        while True:
            line = fo.readline()
            if not line:
                break
            if 0 == len(line):
                continue
            account = analyzeLine(line, False)
            if "" != account:
                accountSet.add(account)
                accountCount += 1
    finally:
        fo.close()
    print "PV:",accountCount
    print "UV:",len(accountSet)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '''错误的参数！
        使用方法：python SDKPPServerStat.py 文件完整路径
        例：python SDKPPServerStat.py /home/nieyong/temp/pp_login_20151021.log'''
        sys.exit(1)
    logPath = sys.argv[1]
    analyzeFile(logPath)
