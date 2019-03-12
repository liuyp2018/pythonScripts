#coding=utf-8
import xml.dom.minidom

#打开xml文件
dom=xml.dom.minidom.parse('C:/Users/EDZ/.jenkins/jobs/ove2.0_admin_incremDeploy/lastSuccessful/build.xml')

#得到文档元素对象
root=dom.documentElement
#print(root.nodeName)
v=root.getElementsByTagName('sha1')
version=v[0]
versionData=version.firstChild.data
print(versionData)

with open('version.txt','w') as f:    #设置文件对象
     f.write(versionData)
