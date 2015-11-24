import re

#s='ABC\\-001'       #对应正则表达式字符串变为：'ABC\-001'
s=r'ABC\-001'        #对应正则表达式字符串不变
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
str1='010-12345'
str2='010 12345'

def check(str,regex):
    if re.match(regex,str):
        print('succeed')
    else:
        print('failed')

check(str1,r'^\d{3}\-\d{3,8}$')
check(str2,r'^\d{3}\-\d{3,8}$')
#切分
print('a b   c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
#分组，提取子串

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m2 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m2.groups())

#贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())
#加个?就可以让\d+采用非贪婪匹配
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())
