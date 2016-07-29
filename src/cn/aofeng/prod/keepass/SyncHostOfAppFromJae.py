#coding:utf8
import requests
import os
from prettytable import PrettyTable
import time
from cn.aofeng.prod.keepass.AppAndHost import Host, App

# 账号登陆JAE后生成的Cookie项"_uae_web_session"
uaeWebSession = ""

# KeePass数据库文件及打开的密码
keepassDbFilePath = "Test.kdbx"
keepassDbFilePasswd = "aofeng"

# SSH的账号和密码
sshUsername = "aofeng"
sshPasswd = ""

# 获取用户拥有权限的应用列表地址
appListUrl = ""
# 获取指定应用的主机列表地址
hostListUrl = ""

class KeePass:
    def addEntryToKeePass(self, appId, appName, hostObj, entryUrl, entryTitlePrefix=""):
        '''向KeePass中添加记录'''
        print("add host  entry %s" % hostObj[0])
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

    def delAllEntriesOfGroup(self, groupPath):
        '''从KeePass中删除指定Group下的所有记录'''
        print("delete all entries from group %s"%groupPath)
        delCmdTemplate = 'KPScript -c:DeleteEntry %s -pw:"%s" -refx-GroupPath:%s'
        param = (keepassDbFilePath, 
                 keepassDbFilePasswd, 
                 groupPath)
        delCmd = delCmdTemplate % param
        os.system(delCmd)

    def addEntryOfAppToKeePass(self, appId, appList, hostListUrl):
        app = App()
        host = Host()
        hostList = host.getHostListOfApp(appId, hostListUrl, True)
        appName = app.findAppName(appList, appId)
        
        # 清除旧的主机列表
        groupPath = "PROD/%s_%s" % (appName, appId)
        kp = KeePass()
        kp.delAllEntriesOfGroup(groupPath)
        time.sleep(2)
        
        # 增加新的主机列表
        for host in hostList:
            kp.addEntryToKeePass(appId, appName, host, "cmd://kitty -load SSHGateWay -l {username} -pw {password}")   # 增加一条使用Kitty打开SSH的记录
            kp.addEntryToKeePass(appId, appName, host, "ssh://fortressgate.aofeng:3000", "XShell-")   # 增加一条使用XShell打开SSH的记录

if __name__ == '__main__':
    if(len(uaeWebSession)==0):
        uaeWebSession = raw_input("Please Enter uae_web_session:")
    if(len(keepassDbFilePath)==0):
        keepassDbFilePath = raw_input("Please Enter KeePass Database File:")
    if(len(keepassDbFilePasswd)==0):
        keepassDbFilePasswd = raw_input("Please Enter Open %s Password':"%keepassDbFilePath)
    if(len(sshUsername)==0):
        sshUsername = raw_input("Please Enter SSH Account:")
    if(len(sshPasswd)==0):
        sshPasswd = raw_input("Please Enter SSH Password:")
    if(len(appListUrl)==0):
        appListUrl = raw_input("Please Enter appListUrl:")
    if(len(hostListUrl)==0):
        hostListUrl = raw_input("Please Enter hostListUrl:")
    
    app = App()
    kp = KeePass()
    appList = app.getAppList(appListUrl, True)
    app.showAppList(appList, True)
    appId = raw_input("Please Enter 'App Id' or 'ALL':")
    if("ALL"==appId):
        # 所有应用
        for app in appList:
            kp.addEntryOfAppToKeePass(str(app["appId"]), appList, hostListUrl)
    else:
        # 单个应用
        kp.addEntryOfAppToKeePass(appId, appList, hostListUrl)
    
