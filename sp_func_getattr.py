class Student(object):
    def __getattr__(self,attr):
        if attr=='age':
            return lambda:25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' %attr)

stu=Student()
print(stu.age)
print(stu.age())
#print(stu.score())

#链式调用
class Chain(object):
    def __init__(self,path=''):
        self._path=path

    def __getattr__(self,path):
        return Chain('%s/%s' %(self._path,path))

    def __str__(self):
        return self._path

    __repr__=__str__

print(Chain().status.user.list.show)
