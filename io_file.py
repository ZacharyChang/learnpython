with open('\pytest.txt','w') as f1:
    f1.write('Hello,Zachary!')
'''
try:
    f=open('c:/pytest.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
'''
#same as
#with open('\pytest.txt','r',encoding='gbk',errors='ingore')
with open('\pytest.txt','r') as f2: #'rb'读二进制 
    for line in f2.readlines():
        print(line.strip())     #去掉默认'\n'


