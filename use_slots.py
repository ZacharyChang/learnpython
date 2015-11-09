class Student(object):
    __slots__=('name','age','score','set_age')  #使用__slots__定义限制属性

s=Student()
s.name='Arya'   #动态给实例绑定属性
print(s.name)

def set_age(self,age):  #定义实例方法
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)    #给实例绑定一个方法
s.set_age(25)   #调用实例方法
print(s.age)

s2=Student()    #创建新实例
#s2.set_age(33)  #调用方法，报错
def set_score(self,score):
    self.score=score

Student.set_score=MethodType(set_score,Student) #给class绑定方法
s.set_score(88)
print(s.score)
s2.set_score(92)
print(s.score)  #输出92！
print(s2.score)

