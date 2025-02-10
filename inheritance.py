#Parent class/super class/base class
class Animal:
    def speak(self):
        print("Animal is speaking")

#child class/sub class/derived class

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

a = Animal()


c =Cat()
c.speak()


d =Dog()
d.bark()