class Student(object):
    def __init__(self,name):
        self.name=name

    def __call__(self):
        print('My Name is %s' %self.name)

stu=Student('Mike')
stu()  #self不要传参数
print(callable(stu))
print(callable([1,2,3]))
