def fn(self,name='world'):
    print('hello,%s.' %name)

Hello=type('hello',(object,),dict(hello=fn))    #创建class Hello
h=Hello()
h.hello()
h.hello('zachary')
print(type(Hello))
print(type(h))

print('============================')
#metaclass是类的模板，必须从type类派生
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass

L=MyList()
L.add(1)
L.add(2)
print(L)
