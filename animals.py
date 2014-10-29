class Animal:
    def say(self):
        print('Hi!')

    def die(self):
        print('Oh!')


class Bird(Animal):
    pass


class Dog(Animal):
    def say(self):
        print('Bow!')


a = Animal()
a.say()
a.die()

b = Bird()
b.say()
b.die()

d = Dog()
d.say()
d.die()
