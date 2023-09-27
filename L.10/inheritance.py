class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print('{} is {} years old.'.format(self.name, self.age))
    
    def speak(self, sound):
        print('{} says {}!'.format(self.name, sound))
    
class RussellTErrier(Dog):
    def run(self, speed):
        print('{} runs {}'.format(self.name, speed))

class Bulldog(Dog):
    def run(self, speed):
        print('{} runs {}'.format(self.name, speed))

Jim = Bulldog('Jim', 12)
print(Jim.description())

print(Jim.run('slowly'))

print(isinstance(Jim, Dog))

julie = Dog('Julie', 100)
print(isinstance(julie, Dog))

john = RussellTErrier('John', 5)
print(isinstance(john, Bulldog))

print(isinstance(julie, Dog))