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

print('a b   c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,]+', 'a,b, c  d'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
