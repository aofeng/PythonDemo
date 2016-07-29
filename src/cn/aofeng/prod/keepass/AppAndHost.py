#coding:utf8
import sys
import os
import requests
import json
from prettytable import PrettyTable
from cn.aofeng.prod.keepass.Printer import ConsolePrettyTable, FileCsv

# 账号登陆JAE后生成的Cookie项"_uae_web_session"
uaeWebSession = ""

# 获取用户拥有权限的应用列表地址
appListUrl = ""

# 获取指定应用的主机列表地址
hostListUrl = ""

# 输出类型（Console，CSV）
outType="Console"
outFilePath=""

class Common:
    ''' 公用方法 '''
    
    def get(self, url, uaeWebSession):
        cookies = {"_uae_web_session":uaeWebSession}
        response = requests.get(url, cookies=cookies)
        return response

class App:
    ''' 获取应用信息 '''
    
    def getAppList(self, reqUrl, onlyProd=False):
        '''从JAE获取应用列表'''
        result = []
        common = Common()
        response = common.get(reqUrl, uaeWebSession)
        jsonObj = json.loads(response.content.decode())
        for appGroup in jsonObj:
            appList = appGroup["apps"]
            for app in appList:
                if(onlyProd):
                    if("生产"==app["env_mode"]):
                        result.append({"appId":app["id"], "appName":app["index"], "appDesc":app["name"], "envMode":app["env_mode"]})
                else:
                    result.append({"appId":app["id"], "appName":app["index"], "appDesc":app["name"], "envMode":app["env_mode"]})
        return result

    def showAppList(self, appList, onlyProd=False):
        '''将应用列表显示在控制台'''
        table = PrettyTable(["App Id", "App Name", "App Desc", "Env"])
        for app in appList:
            table.align["App Name"] = "l"
            table.align["App Desc"] = "l"
            if(onlyProd):
                if("生产"==app["envMode"]):
                    table.add_row([app["appId"], app["appName"], app["appDesc"], app["envMode"]])
            else:
                table.add_row([app["appId"], app["appName"], app["appDesc"], app["envMode"]])
        print(table)
        print("")

    def findAppName(self, appList, appId):
        ''''根据指定的应用ID查询对应的应用名称。如果找不到，返回空字符串("")'''
        for app in appList:
            if(appId==str(app["appId"])):
                return app["appName"]
        return ""

class Host:
    ''' 获取主机信息 '''
    
    def getHostListOfApp(self, appId, reqUrl, onlyProd=False):
        '''从JAE获取指定应用的主机列表'''
        getHostUrl = reqUrl%appId
        common = Common()
        response = common.get(getHostUrl, uaeWebSession)
        jsonObj = json.loads(response.content.decode())
        hostList = jsonObj.get("instances")
        if not hostList:
            return []
        result = []
        for host in hostList:
            if not host.get("agent_ip"):   # 没有IP的主机说明已经下线
                continue
            if(onlyProd):
                if("prod"==host["env_mode"]):
                    result.append([ host["agent_name"], host["agent_ip"], host["port"], host["cluster"], host["env_mode"], host["state"] ])
            else:
                result.append([ host["agent_name"], host["agent_ip"], host["port"], host["cluster"], host["env_mode"], host["state"] ])
        return result

    def printAppAndHostList(self, appId, appName, hostList, outParam):
        ''' 输出应用和应用的主机列表信息 '''
        outType = outParam["outType"];
        outFilePath = outParam["outFilePath"]
        if ("Console" == outType):
            obj = ConsolePrettyTable(outFilePath)
            obj.out(appId, appName, hostList)
        elif("CSV" == outType):
            obj = FileCsv(outFilePath)
            obj.out(appId, appName, hostList)
        else:
            print("错误的输出类型\n")

if __name__ == '__main__':
    # 设置默认编码为utf8
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    # 将当前目录加入到python的环境目录
    sys.path.append(os.getcwd())
    
    # 参数判断
    if (len(uaeWebSession) == 0):
        uaeWebSession = input("Please Enter uae_web_session:")
    if (len(appListUrl) == 0):
        appListUrl = input("Please Enter appListUrl:")
    if (len(hostListUrl) == 0):
        hostListUrl = input("Please Enter hostListUrl:")
    if (len(outType) == 0):
        outType = input("Please Enter outType(Console, CSV):")
    if ("CSV" == outType and len(outFilePath) == 0):
        outFilePath = input("Please Enter outFilePath:")
        
    app = App()
    host = Host()
    appList = app.getAppList(appListUrl, True)
    app.showAppList(appList, True)
    appId = raw_input("Please Enter 'App Id' or 'ALL':")
    outParam = {"outType":outType, "outFilePath":outFilePath}
    if ("ALL"==appId):
        # 所有应用
        for app in appList:
            appName = app["appName"]
            hostList = host.getHostListOfApp(app["appId"], hostListUrl, True)
            host.printAppAndHostList(app["appId"], appName, hostList, outParam)
    else:
        # 单个应用
        appName = app.findAppName(appList, appId)
        hostList = host.getHostListOfApp(appId, hostListUrl, True)
        host.printAppAndHostList(appId, appName, hostList, outParam)
