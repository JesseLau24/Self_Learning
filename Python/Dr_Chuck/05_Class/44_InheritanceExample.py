# Define a Parent class named Animal
class Animal:
    # Initialize the Animal class with a name attribute
    def __init__(self, name):
        self.name = name

    # Define a method speak for the Animal class
    def speak(self):
        print(f"{self.name} makes a sound")

# Define a Child class named Dog that inherits from Animal
class Dog(Animal):
    # Override the speak method for the Dog class
    def speak(self):
        print(f"{self.name} barks")

# Define a Child class named Cat that inherits from Animal
class Cat(Animal):
    # Override the speak method for the Cat class
    def speak(self):
        super().speak() # here, it didn't override the speak from parent.
        # it adds the following line
        print(f"{self.name} meows")

# Create an instance of Dog with the name "Buddy"
dog = Dog("Buddy")
# Create an instance of Cat with the name "Whiskers"
cat = Cat("Whiskers")

# Call the speak method on the Dog instance
dog.speak()  # Output: Buddy barks
# Call the speak method on the Cat instance
cat.speak()  # Output: Whiskers meows

# Define a Child class named Bird that inherits from Animal
class Bird(Animal):
    # Override the speak method for the Bird class
    def speak(self):
        print(f"{self.name} chirps")

    # Define an additional method fly for the Bird class
    def fly(self):
        print(f"{self.name} is flying")

# Create an instance of Bird with the name "Tweety"
bird = Bird("Tweety")
# Call the speak method on the Bird instance
bird.speak()  # Output: Tweety chirps
# Call the fly method on the Bird instance
bird.fly()    # Output: Tweety is flying

# Define a Parent class named Vehicle
class Vehicle:
    # Initialize the Vehicle class with brand and model attributes
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Define a method info for the Vehicle class
    def info(self):
        print(f"Vehicle: {self.brand} {self.model}")

# Define a Child class named Car that inherits from Vehicle
class Car(Vehicle):
    # Initialize the Car class with brand, model, and year attributes
    def __init__(self, brand, model, year):
        # Call the parent class's __init__ method using super()
        super().__init__(brand, model)
        self.year = year

    # Override the info method for the Car class
    def info(self):
        # Call the parent class's info method using super()
        super().info()
        print(f"Year: {self.year}")

# Create an instance of Car with the brand "Toyota", model "Camry", and year 2020
car = Car("Toyota", "Camry", 2020)
# Call the info method on the Car instance
car.info()
# Output:
# Vehicle: Toyota Camry
# Year: 2020
