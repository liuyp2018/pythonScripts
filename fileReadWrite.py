
#打开一个指定目录下的文件，并指定打开方式为r
f=open('E:/aaa.txt','r')
#读取文件中的内容
print(f.read())
#关闭文件
f.close()


#使用with，可在结束时自动调用close()方法
with open('E:/aaa.txt','r') as f:
   print(f.read())


with open('E:/aaa.txt','r') as f:
    #读取文件中的所有内容，适用于文件比较小的情况
    print(f.read())

with open('E:/aaa.txt', 'r') as f:
    #按设定字节读取文件内容,调用多次，可连续读取文件内容
    print(f.read(3))
    print(f.read(3))

with open('E:/aaa.txt', 'r') as f:
    #每次读取一行内容，若要读取多行，则需要多次调用
    print(f.readline())
    print(f.readline())

with open('E:/aaa.txt', 'r') as f:
    #readlines()将文件中所有内容一次读出，并返回一个list
  for line in f.readlines():
        print(line.strip())



with open('E:/aaa.txt','w') as f:
    f.write('hello11')

with open('E:/aaa.txt','r') as f:
    print(f.read())

with open('E:/aaa.txt', 'a') as f:
    f.writelines(['aaa\n','bbb\n'])

with open('E:/aaa.txt', 'r') as f:
    print(f.read())



with open('C:/Users/EDZ/Desktop/微信图片_20180621101455.jpg', 'rb') as f:
    print(f.read())