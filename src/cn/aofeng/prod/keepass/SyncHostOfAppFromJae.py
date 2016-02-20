#coding:utf8
import requests
import json
import os
from prettytable import PrettyTable
import time

# 账号登陆JAE后生成的Cookie项"_uae_web_session"
uaeWebSession = ""

# KeePass数据库文件及打开的密码
keepassDbFilePath = "Test.kdbx"
keepassDbFilePasswd = "aofeng"

# SSH的账号和密码
sshUsername = "nieyong"
sshPasswd = ""

# 获取用户拥有权限的应用列表地址
appListUrl = ""
# 获取指定应用的主机列表地址
hostListUrl = ""

def request(url, uaeWebSession):
    cookies = {"_uae_web_session":uaeWebSession}
    response = requests.get(url, cookies=cookies)
    return response

def getAppList(onlyProd=False):
    '''从JAE获取应用列表'''
    result = []
    response = request(appListUrl, uaeWebSession)
    jsonObj = json.loads(response.content.decode())
    for appGroup in jsonObj:
#         print(appGroup["id"], appGroup["name"])
        appList = appGroup["apps"]
        for app in appList:
            if(onlyProd):
                if("生产"==app["env_mode"]):
                    result.append({"appId":app["id"], "appName":app["index"], "appDesc":app["name"], "envMode":app["env_mode"]})
            else:
                result.append({"appId":app["id"], "appName":app["index"], "appDesc":app["name"], "envMode":app["env_mode"]})
    return result

def showAppList(appList, onlyProd=False):
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

def findAppName(appList, appId):
    ''''根据指定的应用ID查询对应的应用名称。如果找不到，返回空字符串("")'''
    for app in appList:
        if(appId==str(app["appId"])):
            return app["appName"]
    return ""

def getHostOfApp(appId, onlyProd=False):
    '''从JAE获取指定应用的主机列表'''
    getHostUrl = hostListUrl%appId
    response = request(getHostUrl, uaeWebSession)
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

def showHostOfApp(appId, hostList):
    '''将应用的主机列表显示在控制台'''
    print("AppId:%s, has %d host"%(appId, len(hostList)))
    table = PrettyTable(["Host Name", "Host IP", "Host Port", "Cluster",  "Env", "State"])
    for host in hostList:
        table.align["Host Name"] = "l"
        table.align["Cluster"] = "l"
        table.add_row(host)
    print(table)

def addEntryToKeePass(appId, appName, hostObj, entryUrl, entryTitlePrefix=""):
    '''向KeePass中添加记录'''
    print("add entry to host %s" % hostObj[0])
    addCmdTemplate = 'KPScript -c:AddEntry %s -pw:"%s" -Title:"%s%s" -UserName:"%s@reader@%s@%d" -Password:"%s" -URL:"%s" -GroupPath:PROD/%s_%s'
    param = (keepassDbFilePath, 
             keepassDbFilePasswd, 
             entryTitlePrefix, 
             hostObj[0], 
             sshUsername, 
             hostObj[1], 
             9922, 
             sshPasswd, 
             entryUrl, 
             appName, 
             appId)
    addCmd = addCmdTemplate % param
    os.system(addCmd)

def delAllEntriesOfGroup(groupPath):
    '''从KeePass中删除指定Group下的所有记录'''
    print("delete all entries from group %s"%groupPath)
    delCmdTemplate = 'KPScript -c:DeleteAllEntries %s -pw:"%s" -refx-GroupPath:%s'
    param = (keepassDbFilePath, 
             keepassDbFilePasswd, 
             groupPath)
    delCmd = delCmdTemplate % param
    os.system(delCmd)

def addEntryOfAppToKeePass(appId, appList):
    hostList = getHostOfApp(appId, True)
    showHostOfApp(appId, hostList)
    appName = findAppName(appList, appId)
    # 清除旧的主机列表
    groupPath = "PROD/%s_%s" % (appName, appId)
    delAllEntriesOfGroup(groupPath)
    time.sleep(2)
    # 增加新的主机列表
    for host in hostList:
        addEntryToKeePass(appId, appName, host, "cmd://kitty -load SSHGateWay -l {username} -pw {password}")   # 增加一条使用Kitty打开SSH的记录
        addEntryToKeePass(appId, appName, host, "ssh://fortressgate.uc.cn:2000", "XShell-")   # 增加一条使用XShell打开SSH的记录

if(len(uaeWebSession)==0):
    uaeWebSession = input("Please Enter uae_web_session:")
if(len(keepassDbFilePath)==0):
    keepassDbFilePath = input("Please Enter KeePass Database File:")
if(len(keepassDbFilePasswd)==0):
    keepassDbFilePasswd = input("Please Enter Open %s Password':"%keepassDbFilePath)
if(len(sshUsername)==0):
    sshUsername = input("Please Enter SSH Account:")
if(len(sshPasswd)==0):
    sshPasswd = input("Please Enter SSH Password:")
appList = getAppList(True)
showAppList(appList, True)
appId = input("Please Enter 'App Id' or 'ALL':")
if("ALL"==appId):
    # 所有应用
    for app in appList:
        addEntryOfAppToKeePass(str(app["appId"]), appList)
else:
    # 指定的单个应用
    addEntryOfAppToKeePass(appId, appList)
    
