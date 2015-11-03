std1={'name':'Stark','score':99}
std2={'name':'Tom','score':81}

def print_score1(std):
        print('%s: %s' %(std['name'],std['score']))

print_score1(std1)
print_score1(std2)

class Student(object):
    
    def __init__(self,name,score):
        self.name=name
        self.score=score
        
    def print_score(self):
        print('%s: %s' %(self.name,self.score))

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Stark',87)
bart.print_score()
lisa.print_score()
