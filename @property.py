class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        elif value <0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self._score=value     #_score rather tan score

s=Student()
s.score=80
print(s.score)
s.score=999     #raise error
s.score='abc'   #not execute
