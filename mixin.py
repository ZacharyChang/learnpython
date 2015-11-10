class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running')

class Flyable(object):
    def fly(self):
        print('Flyging')

class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Flyable):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird,Runnable):
    pass

dog=Dog()
print(type(dog))
print(isinstance(dog,Animal))
print(isinstance(dog,Mammal))
print(isinstance(dog,Runnable))
print(isinstance(dog,Flyable))
