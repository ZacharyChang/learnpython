#使用type()判断对象类型
print('type(123): %s' %type(123))
print("type('str'):%s" %type('str'))
print('type(None):%s' %type(None))
print('type(abs):%s' %type(abs))

print('type(123)==type(456)? ',end='')
print(type(123)==type(456))
print('type(123)==int? ',end='')
print(type(123)==int)
print("type('123')==type('abc')? ",end='')
print(type('123')==type('abc'))
print('type(abc)==str? ',end='')
print(type(123)==int)
print("type('abc')==type(123)? ",end='')
print(type('abc')==type(123))

print('**********************')
#使用isinstance()判断继承关系
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))

print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

print('**********************')
#使用dir()获得对象所有属性和方法
print(dir('ABC'))

class Dog(object):
    def __len__(self):
        return 100

dog=Dog()
print(len(dog))

class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=MyObject()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',45)
print(getattr(obj,'y'))
print(getattr(obj,'z',404))
func=getattr(obj,'power')
print(func)
print(func())
