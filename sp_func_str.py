class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'str: a object of Student [name=%s]' %self.name
    #__repr__=__str__
    def __repr__(self):
        return 'repr: a object of Student [name=%s]' %self.name

stu=Student('Jack')
print(stu)  #__str__
stu         #__repr__ in console window
