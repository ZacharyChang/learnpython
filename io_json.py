import json

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
        
class Teacher(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s=Student('Scott',22,90)
#序列化
js=json.dumps(s,default=student2dict)
print(js)
#反序列化
print(json.loads(js,object_hook=dict2student))
t=Teacher('Mike',24,'m')
#实例的__dict__属性存储实例变量
print(json.dumps(t,default=lambda obj:obj.__dict__))
