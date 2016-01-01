__author__ = 'ZacharyChang'

import re
# from re import findall,search,sub,S

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

# search
s2 = 'asdfxxIxx123xxlovexxdfd'
g1 = re.search('xx(.*?)xx123xx(.*?)xx', s2).group(1)
g2 = re.search('xx(.*?)xx123xx(.*?)xx', s2).group(2)
g3 = re.findall('xx(.*?)xx123xx(.*?)xx', s2)
print(g1)
print(g2)
print(g3[0][1])

# sub
h = re.sub('xx(.*?)xx', '123%s456' % 'new', s2)
print(h)

s3 = 'afdasfg2332daadgdfs32423ad'
i = re.findall('(\d+)', s3)
print(i)
