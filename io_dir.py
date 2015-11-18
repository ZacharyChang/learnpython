import os
#获取系统信息
print(os.name)  
#print(os.uname())  not work on windows
#获取系统变量
print(os.environ)
print(os.environ.get('PATh'))
print(os.path.abspath('.'))

#合并路径
print(os.path.join('c:\Git','test'))    #正确处理不同操作系统下路径分隔符，win下'\',linux下'/'
#创建目录
if not os.path.exists('c:\\testdir'):
    os.mkdir('c:\\testdir')
#删除目录
os.rmdir('c:\\testdir')

#获取文件扩展名
print(os.path.splitext('c:\\Git\\readme.txt'))  #('c:\\Git\\readme', '.txt')
if os.path.isfile('test1.txt'):
    #重命名文件
    os.rename('test1.txt','test2.txt')
    #删除文件（无复制！）
    os.remove('test2.txt')

#列出当前目录下的所有目录
for x in os.listdir('.'):
    if os.path.isdir(x):
        print(x)

#列出所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
