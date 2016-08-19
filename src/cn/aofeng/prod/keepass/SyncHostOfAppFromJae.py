#coding:utf8
import requests
import os
from prettytable import PrettyTable
import time
from cn.aofeng.prod.keepass.AppAndHost import Host, App

# 账号登陆JAE后生成的Cookie项"_uae_web_session"
__uaeWebSession = ""

# KeePass数据库文件及打开的密码
__keepassDbFilePath = "Test.kdbx"
__keepassDbFilePasswd = "aofeng"

# SSH的账号和密码
__sshUsername = ""
__sshPasswd = ""

# 获取用户拥有权限的应用列表地址
__appListUrl = ""
# 获取指定应用的主机列表地址
__hostListUrl = ""

#KiTTY中定义的主机连接信息名称
__kittyGW = "SSHGateWay"
#XShell连接的主机和端口信息
__xshellGW = "ssh://fortressgate.aofeng.cn:3000"

class KeePass:
    
    def __init__(self, uaeWebSession, keepassDbFilePath, keepassDbFilePasswd, sshUsername, sshPasswd):
        self.uaeWebSession = uaeWebSession
        self.keepassDbFilePath = keepassDbFilePath
        self.keepassDbFilePasswd = keepassDbFilePasswd
        self.sshUsername = sshUsername
        self.sshPasswd = sshPasswd
    
    def addEntryToKeePass(self, appId, appName, hostObj, entryUrl, entryTitlePrefix=""):
        '''向KeePass中添加记录'''
        print("add host  entry %s" % hostObj[0])
        addCmdTemplate = 'KPScript -c:AddEntry %s -pw:"%s" -Title:"%s%s" -UserName:"%s@reader@%s@%d" -Password:"%s" -URL:"%s" -GroupPath:PROD/%s_%s'
        param = (self.keepassDbFilePath, 
                 self.keepassDbFilePasswd, 
                 entryTitlePrefix, 
                 hostObj[0], 
                 self.sshUsername, 
                 hostObj[1], 
                 9922, 
                 self.sshPasswd, 
                 entryUrl, 
                 appName, 
                 appId)
        addCmd = addCmdTemplate % param
        os.system(addCmd)

    def delAllEntriesOfGroup(self, groupPath):
        '''从KeePass中删除指定Group下的所有记录'''
        print("delete all entries from group %s"%groupPath)
        delCmdTemplate = 'KPScript -c:DeleteEntry %s -pw:"%s" -refx-GroupPath:%s'
        param = (self.keepassDbFilePath, 
                 self.keepassDbFilePasswd, 
                 groupPath)
        delCmd = delCmdTemplate % param
        os.system(delCmd)

    def addEntryOfAppToKeePass(self, appId, appList, hostListUrl, kittyGW, xshellGW):
        app = App(self.uaeWebSession)
        host = Host(self.uaeWebSession)
        hostList = host.getHostListOfApp(appId, hostListUrl, True)
        appName = app.findAppName(appList, appId)
        
        # 清除旧的主机列表
        groupPath = "PROD/%s_%s" % (appName, appId)
        self.delAllEntriesOfGroup(groupPath)
        time.sleep(2)
        
        # 增加新的主机列表
        for host in hostList:
            self.addEntryToKeePass(appId, appName, host, "cmd://kitty -load "+kittyGW+" -l {username} -pw {password}")   # 增加一条使用Kitty打开SSH的记录
            self.addEntryToKeePass(appId, appName, host, xshellGW, "XShell-")   # 增加一条使用XShell打开SSH的记录

if __name__ == '__main__':
    if(len(__uaeWebSession)==0):
        __uaeWebSession = raw_input("Please Enter uae_web_session:")
    if(len(__keepassDbFilePath)==0):
        __keepassDbFilePath = raw_input("Please Enter KeePass Database File:")
    if(len(__keepassDbFilePasswd)==0):
        __keepassDbFilePasswd = raw_input("Please Enter Open %s Password':"%__keepassDbFilePath)
    if(len(__sshUsername)==0):
        __sshUsername = raw_input("Please Enter SSH Account:")
    if(len(__sshPasswd)==0):
        __sshPasswd = raw_input("Please Enter SSH Password:")
    if(len(__appListUrl)==0):
        __appListUrl = raw_input("Please Enter appListUrl:")
    if(len(__hostListUrl)==0):
        __hostListUrl = raw_input("Please Enter hostListUrl:")
    
    app = App(__uaeWebSession)
    kp = KeePass(__uaeWebSession, __keepassDbFilePath, __keepassDbFilePasswd, __sshUsername, __sshPasswd)
    appList = app.getAppList(__appListUrl, True)
    app.showAppList(appList, True)
    appId = raw_input("Please Enter 'App Id' or 'ALL':")
    if("ALL"==appId):
        # 所有应用
        for app in appList:
            kp.addEntryOfAppToKeePass(str(app["appId"]), appList, __hostListUrl, __kittyGW, __xshellGW)
    else:
        # 单个应用
        kp.addEntryOfAppToKeePass(appId, appList, __hostListUrl, __kittyGW, __xshellGW)
