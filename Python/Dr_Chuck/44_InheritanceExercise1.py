# Create a base class Animal with attributes name and color, 
# and a method make_sound() that prints a generic sound. 
# Then create two derived classes, Dog and Cat, which adds age, 
# override the make_sound() method to print "Woof" and "Meow", 
# respectively. 
# Create instances of Dog and Cat and call their make_sound() 
# methods.
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def makesound(self):
        print(f'{self.color} {self.name} makes a sound.')

class Dog(Animal):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.age = age

    def woof(self):
        super().makesound()
        print(f'woof, woof. i am {self.age} years old')

class Cat(Animal):
    def __init__(self, name, color, age):
        super().__init__(name, color)
        self.age = age

    def meow(self):
        super().makesound()
        print(f'meow, meow. i am {self.age} years old.')

lucky = Cat('lucky', 'orange', 3)
huahua = Dog('huahua', 'white and brown', 16)

lucky.meow()
huahua.woof()
