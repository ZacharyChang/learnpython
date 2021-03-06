from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))


q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

dd=defaultdict(lambda:'N/A')
dd['key1']=1
print(dd['key1'])
print(dd['key2'])   #返回默认值

d=dict([('a',1),('b',2),('c',3)])
print(d)    #dict的key无序
od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)   #OrderDict的Key有序

#FIFO的dict
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

c=Counter()
for ch in 'pythonlanguage':
    c[ch]=c[ch]+1

print(c)
