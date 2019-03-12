import os
from shutil import copy
from shutil import rmtree

#jenkins项目目录
JENKINS_PATH='C:/Users/EDZ/.jenkins/workspace/wdove_42_incremDeploy'
#待增量复制的文件所在目录
copyFileCommonPath=JENKINS_PATH+'/copyFiles'
#存放svn中更改文件的文件路径
changedFile='D:/Apache-Subversion-1.10.0/bin/changedfiles.txt'

#在操作前，将上一次生成的待复制文件删除
if os.path.exists(copyFileCommonPath):
    rmtree(copyFileCommonPath)
#再次创建放置需要更新文件的文件夹
if not os.path.exists(copyFileCommonPath):
    os.makedirs(copyFileCommonPath)

if os.path.exists(JENKINS_PATH+'/ove1.0_deleteFiles.txt'):
    os.remove(JENKINS_PATH+'/ove1.0_deleteFiles.txt')
# if not os.path.exists(JENKINS_PATH+'/ove1.0_deleteFiles.txt'):
#     f=open(JENKINS_PATH+'/ove1.0_deleteFiles.txt','w')
#     f.close()

#将文件的路径和svn项目路径进行分离，得到更新文件的相对路径
def splitStr(str):
    file=str.split("whu")[1]
    return file

f=open(changedFile,'r')
for line in f.readlines():
    str=line.strip()
    #print(str[0])
    #判断得到的changefiles中，对文件的操作是否是删除；若是删除操作则忽略该文件，不对该文件进行后续的复制操作
    if str[0]=='D':
        # 分离得到要复制文件的相对路径
        file=splitStr(str)
        print(file)
        with open(JENKINS_PATH+'/ove1.0_deleteFiles.txt', 'a') as f1:
            f1.writelines(file+'\n')
    else :
        # 分离得到要复制文件的相对路径
        file=splitStr(str)
        #得到要复制的文件在Jenkins项目中的绝对路径
        filePath = JENKINS_PATH + file
        #print(file)
        #得到要复制文件的上一级目录p
        p,f1=os.path.split(file)
        #print(p)
        #print(f1)
        #得到要将文件复制到的目标文件夹
        copyFilePath=copyFileCommonPath+p
        #创建目标文件夹
        if not os.path.exists(copyFilePath):
            os.makedirs(copyFilePath)
        #print(filePath)
        #判断得到的对象是文件还是文件夹，若是文件夹则不进行复制操作
        if os.path.isdir(filePath):
            continue
        #将Jenkins中对应的文件复制到目标文件夹下
        copy(filePath,copyFilePath)
#关闭文件
f.close()




