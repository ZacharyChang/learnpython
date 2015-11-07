class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Dog eatss meat')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Cat eats fish')

dog=Dog()
cat=Cat()
dog.run()
dog.eat()
cat.run()
cat.eat()
print('dog is a Dog? %s' %isinstance(dog,Dog))
print('dog is a Anmial? %s' %isinstance(dog,Animal))
print('cat is a Dog? %s' %isinstance(cat,Dog))

