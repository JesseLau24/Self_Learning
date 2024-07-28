# Create a base class Engine with attributes horsepower and type. 
# Create a base class Car with attributes make, model, 
# and an Engine object. 
# Ensure that the Car class can display its information along with 
# engine details.
# Define the base class Engine
class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type

    def display_info(self):
        print(f"Engine: {self.horsepower} HP, Type: {self.engine_type}")

# Define the base class Car
class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def display_info(self):
        print(f"Car: {self.make} {self.model}")
        self.engine.display_info()

# Create an instance and call the method
engine = Engine(300, "V6")
car = Car("Ford", "Mustang", engine)
car.display_info()