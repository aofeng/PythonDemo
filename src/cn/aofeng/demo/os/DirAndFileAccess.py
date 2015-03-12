#coding:utf8
import os
import shutil
import sys

# 显示当前系统平台，Windows为"nt"。Unix/Linux显示为"posix"
print "系统平台：", os.name

# 显示当前工作目录
print "当前工作目录：", os.getcwd()

# 切换工作目录
def changeWorkDir(workDir):
    try:
        os.chdir(workDir)
        print "切换至新的工作目录：", workDir
    except OSError, ex:
        print "切换至新的工作目录%s发生错误：%s" % (workDir, ex)

newWorkDir = "/tmp"
changeWorkDir(newWorkDir)

# 与工作目录相关的公共方法
def genFullPath(dirName="", fileName=""):
    ''' 将传入的目录、文件与当前工作目录的路径拼接，生成一个绝对路径 '''
    elements = [newWorkDir]
    if 0 != len(dirName):
        elements.append(dirName)
    if 0!= len(fileName):
        elements.append(fileName)
    fullPath = os.sep.join(elements)
    return fullPath

# 新建目录
def createDir(dirName):
    fullPath = genFullPath(dirName)
    if not os.path.exists(fullPath):
        os.mkdir(fullPath)
        print "新建目录：", fullPath
    else:
        print "目录%s已经存在" % (fullPath)

dirName = "python_os_study"
createDir(dirName)

# 新建文件
def createFile(dirName, fileName):
    fullPath = genFullPath(dirName, fileName)
    if os.path.exists(fullPath):
        print "文件%s已经存在" % (fullPath)
        return
    
    fo = open(fullPath, "wb+")
    try:
        fo.writelines(["第一行：1", os.sep, "第二行：2", os.sep, "第三行：3", os.sep, "第四行：4"])
        print "新建文件：", fullPath
    finally:
        fo.close()

fileName = "python_new_file.txt"
createFile(dirName, fileName)

# 复制文件
def copyFile(srcFileName, dstFileName):
    srcFullPath = genFullPath(dirName, srcFileName)
    dstFullPath = genFullPath(dirName, dstFileName)
    try:
        shutil.copy(srcFullPath, dstFullPath)
        print "复制文件%s至%s成功" % (srcFullPath, dstFullPath)
    except:
        print "复制文件%s至%s出错" % (srcFullPath, dstFullPath)

bakFileName = ".".join([fileName, "bak"])
copyFile(fileName, bakFileName)

# 重命名文件
renameFileName = ".".join([fileName, "rename"])
renSrc = genFullPath(dirName, fileName);
renDst = genFullPath(dirName, renameFileName)
try:
    os.rename(renSrc, renDst)
    print "将文件%s重命名为%s成功" % (renSrc, renDst)
except:
    print "将文件%s重命名为%s出错" % (renSrc, renDst)

# 删除目录
def delDir(dirName):
    delPath = genFullPath(dirName)
    delFileList = os.listdir(delPath)
    for delFile in delFileList:   # 循环删除目录下的所有文件
        delFilePath = os.sep.join([delPath, delFile])
        os.remove(delFilePath)
        print "删除文件%s成功" % (delFilePath) 
    
    try:
        os.rmdir(delPath)   # 删除空目录
        print "删除目录%s成功" % (delPath)
    except:
        print "删除目录%s出错" % (delPath)

delDir(dirName)
