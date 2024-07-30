# Class - a template - Dog
# Method or Message - a defined capability of a class - bark()
# Field 0r Attribute - a bit of data in a class -length
# Object or Instance - a particular instance of a class - Huahua
# Class - a template - Dog
class Dog:
    # Constructor to initialize the attributes of the Dog class
    def __init__(self, name, breed, length):
        # Field or Attribute - a bit of data in a class - length
        self.name = name
        self.breed = breed
        self.length = length
        print(f'__init__ constructs {self.name}')

    # Method or Message - a defined capability of a class - bark()
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    # Method to display information about the dog
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Length: {self.length} inches")

    def __del__(self):
        print(f'__del__ (destructor, which is seldom used) destructs {self.name}')

# Object or Instance - a particular instance of a class - Huahua
# Creating an instance of the Dog class
huahua = Dog("Huahua", "Chihuahua", 12)

# Calling methods on the instance
huahua.bark()  # Output: Huahua says: Woof! Woof!
huahua.display_info()  

# Creating another instance of the Dog class
buster = Dog("Buster", "Bulldog", 24)

# Calling methods on the new instance
buster.bark()  # Output: Buster says: Woof! Woof!
buster.display_info()

# Type of object 'buster'
print('Type of "huahua":', type(huahua))

# will display a list of all the attributes and methods associated
# with the 'huahua' object. 
print('What are in "huahua":',dir(huahua)) 

huahua = 15 # huahua gets destructed
buster.bark()
buster.bark()

print('huahua gets destructedbecause the variable name is reasigned wtih other values')
print('now buster gets destructed because it is the last line of this python file:')
print('but you can also call __del__ like "del huahua".')
