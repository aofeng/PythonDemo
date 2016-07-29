#coding:utf8

from prettytable import PrettyTable

class ConsolePrettyTable:
    '''将应用的主机列表显示在控制台'''
    
    def __init__(self, filePath):
        self.name = "Console"
    
    def out(self, appId, appName, hostList):
        print("AppId:%s, has %d host"%(appId, len(hostList)))
        table = PrettyTable(["App Name", "Host Name", "Host IP", "Host Port", "Cluster",  "Env", "State"])
        for host in hostList:
            table.align["App Name"] = "l"
            table.align["Host Name"] = "l"
            table.align["Cluster"] = "l"
            host.insert(0, appName)
            table.add_row(host)
        print(table)

class FileCsv:
    '''将应用的主机列表输出到CSV文件'''
     
    def __init__(self, filePath):
        self.name = "CSV"
        self.filePath = filePath
        self.separator = ","
        self.endLine = "\n"
        
    def out(self, appId, appName, hostList):
        fo = open(self. filePath, "ab");
        for host in hostList:
            line = appName+self.separator+host[0]+self.separator+host[1]+self.separator+str(host[2])+self.separator+host[3]+self.separator+host[4]+self.separator+host[5]+self.endLine
            fo.write(line)
        fo.close()
        
    