class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self,name):
        self.__name=name

    def set_score(self,score):
        if 0<= score <= 100:
            self.__score=score
        else:
            raise ValueError('wrong value of score')

    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))

    def get_grade(self):
        if self.__score>= 90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

bart=Student('Bart Smith',80)
bart.print_score()
print(bart.get_grade())
bart.set_name('Jon Snow')
bart.set_score(92)
print(bart.get_name())
print(bart.get_score())
bart.print_score()
