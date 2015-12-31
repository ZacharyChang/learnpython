__author__ = 'ZacharyChang'

import re

# example of .
a = 'aba123'
b = re.findall('a..', a)
print(b)

# example of *
c = re.findall('a*', a)
print(c)

# example of ?
d = re.findall('a?', a)
print(d)

secret = 'agasdfxxIxxyetafda2452xxlovexxoperw232xxyouxx2fdsarojf3'
e = re.findall('xx.*xx', secret)
print(e)
d = re.findall('xx.*?xx', secret)
print(d)
e = re.findall('xx(.*?)xx', secret)
print(e)
for each in e:
    print(each)

secret2 = '''adfasfxxhello
xx34awfaftjlkjaxxworldxxafda2342'''
# re.S makes . match new line
f = re.findall('xx(.*?)xx', secret2, re.S)
print(f)
