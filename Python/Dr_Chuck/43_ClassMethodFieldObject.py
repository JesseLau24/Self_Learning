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

    # Method or Message - a defined capability of a class - bark()
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    # Method to display information about the dog
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Length: {self.length} inches")

# Object or Instance - a particular instance of a class - Huahua
# Creating an instance of the Dog class
huahua = Dog("Huahua", "Chihuahua", 12)

# Calling methods on the instance
huahua.bark()  # Output: Huahua says: Woof! Woof!
huahua.display_info()  
# Output:
# Name: Huahua
# Breed: Chihuahua
# Length: 12 inches

# Creating another instance of the Dog class
buster = Dog("Buster", "Bulldog", 24)

# Calling methods on the new instance
buster.bark()  # Output: Buster says: Woof! Woof!
buster.display_info()
# Output:
# Name: Buster
# Breed: Bulldog
# Length: 24 inches
