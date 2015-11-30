import itertools

#natuals=itertools.count(1)
# for n in natuals:
#    print(n)

#cs=itertools.cycle('ABC')
#for c in cs:
#    print(c)

ns =itertools.repeat('A',3)
for n in ns:
    print(n)

natuals=itertools.count(1)
ns=itertools.takewhile(lambda x: x <= 10,natuals)
print(list(ns))

#chain()
for c in itertools.chain('ABC','XYZ'):
    print(c)

#groupby()
for key,group in itertools.groupby('AAABBBCCCDDDAAA'):
    print(key,list(group))

#不区分大小写
for key,group in itertools.groupby('AaaBBbccCA',lambda c:c.upper()):
    print(key,list(group))


