import os
from shutil import copy
from shutil import rmtree

#jenkins项目目录
JENKINS_PATH='C:/Users/EDZ/.jenkins/workspace/ove2.0_admin_incremDeploy/'
projectPath=JENKINS_PATH+'ove_admin'
#待增量复制的文件所在目录
copyFileCommonPath=JENKINS_PATH+'copyFiles'
#存放git中修改文件的文件路径
changedFile=JENKINS_PATH+'changedfiles.txt'
#存放删除文件的文件路径
deleteFilesPath=JENKINS_PATH+'ove2.0_admin_deleteFiles.txt'

#在操作前，将上一次生成的待复制文件删除
if os.path.exists(copyFileCommonPath):
    rmtree(copyFileCommonPath)
#再次创建放置需要更新文件的文件夹
if not os.path.exists(copyFileCommonPath):
    os.makedirs(copyFileCommonPath)
#删除上一次生成的删除文件列表
if os.path.exists(deleteFilesPath):
    os.remove(deleteFilesPath)
if not os.path.exists(deleteFilesPath):
    with open(deleteFilesPath,'a') as f:
        pass

f=open(changedFile,'r')
for line in f.readlines():
    str=line.strip()
    if str[0]=='D':
        # 分离得到要复制文件的相对路径
        dFile=str.split("ove_admin")[1]
        with open(deleteFilesPath, 'a') as f:
            f.writelines(dFile+'\n')
    elif str[0]=='R':
        deleteFile=str.split('ove_admin')[1]
        with open(deleteFilesPath, 'a') as f:
            f.writelines(deleteFile+'\n')
        copyFile=str.split('ove_admin')[2]
        filePath = projectPath  + copyFile
        # 得到要复制文件的上一级目录p
        p, f1 = os.path.split(copyFile)
        # 得到要将文件复制到的目标文件夹
        copyFilePath = copyFileCommonPath + p
        # 创建目标文件夹
        if not os.path.exists(copyFilePath):
            os.makedirs(copyFilePath)
        # 判断得到的对象是文件还是文件夹，若是文件夹则不进行复制操作
        if os.path.isdir(filePath):
            continue
        # 将Jenkins中对应的文件复制到目标文件夹下
        copy(filePath, copyFilePath)
    else:
        # 分离得到要复制文件的相对路径
        file=str.split("ove_admin")[1]
        #得到要复制的文件在Jenkins项目中的绝对路径
        filePath = projectPath + file
        #得到要复制文件的上一级目录p
        p,f1=os.path.split(file)
        #得到要将文件复制到的目标文件夹
        copyFilePath=copyFileCommonPath+p
        #创建目标文件夹
        if not os.path.exists(copyFilePath):
            os.makedirs(copyFilePath)
        #判断得到的对象是文件还是文件夹，若是文件夹则不进行复制操作
        if os.path.isdir(filePath):
            continue
        #将Jenkins中对应的文件复制到目标文件夹下
        copy(filePath,copyFilePath)
#关闭文件
f.close()




