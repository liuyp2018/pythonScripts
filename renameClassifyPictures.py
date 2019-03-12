import exifread
import os
import time
import shutil
#获取文件的时间
def getdate(filename):
    #以二进制方式，打开指定的文件
    f=open(filename,'rb')
    #调用exifread来获取图片文件的exif信息
    data=exifread.process_file(f)
    if data:
        #如果获取到data值，则进行下述相关操作
        try:
            #获取EXIF DateTimeOriginal值，即为图片的创建时间
            t=data['EXIF DateTimeOriginal']
            print(t)
            #将获取到的时间进行格式转换，并仅保留年份和月份，然后返回
            return str(t).replace(":",".")[:7]
        except:
            pass
    #如果，未获取到图片的exif信息，则调用os.stat获取文件的系统信息
    state=os.stat(filename)
    #将文件的修改时间格式化，并返回
    return time.strftime("%Y.%m",time.localtime(state[-2]))

#照片分类整理函数
def classifyPictures(path):
    #利用os.walk获取目录下的文件夹和文件的名称及其目录路径
    for root,dirs,files in os.walk(path,True):
        for filename in files:
            #获取文件的完整路径
            file=os.path.join(root,filename)
            #获取文件的后缀名f
            p,f=os.path.splitext(file)
            if f.lower() not in ('.jpg','.png','.mp4'):
                continue
            try:
                t=getdate(file)
            except Exception as e:
                print(e)
                continue
            moveDir=root+'/'+t
            mf=moveDir+'/'+filename
            if not os.path.exists(moveDir):
                os.mkdir(moveDir)
            #复制文件
            shutil.copy2(file,mf)
            #文件复制后，删除文件
            os.remove(file)

#将路径下的图片，重命名为带日期的文件
def getExif(path):
    for root,dirs,files in os.walk(path,True):
        for file in files:
            old_full_file_name = os.path.join(path, file)
            FIELD = 'EXIF DateTimeOriginal'
            fd = open(old_full_file_name, 'rb')
            tags = exifread.process_file(fd)
            fd.close()
            if FIELD in tags:
                new_name = str(tags[FIELD]).replace(':', '')[:8]+ '_' + file
                new_full_file_name = os.path.join(path, new_name)
                tot = 1
                while os.path.exists(new_full_file_name):
                    new_full_file_name = os.path.splitext(new_full_file_name)[0] +'_' + str(tot) +os.path.splitext(file)[1]
                    tot += 1
                print(old_full_file_name, " ---> ", new_full_file_name)
                os.rename(old_full_file_name, new_full_file_name)
            else:
                print('No {} found'.format(FIELD), ' in: ', old_full_file_name)


getExif('E:/test')

classifyPictures('E:/movePictures')