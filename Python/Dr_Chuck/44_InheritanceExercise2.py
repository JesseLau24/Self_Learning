# Create a base class Person with attributes name and age, and a 
# method display_info() that prints the person's information. 
# Create a derived class Student that adds an attribute grade and 
# overrides the display_info() method to include the grade. 
# Use super() to reuse the code from the parent class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'name: {self.name}, age: {self.age}')


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_info(self):
        super().display_info()
        print(f'occupation: student grade:{self.grade}')


xiaohong = Student('xiaohong', 8, '100')
xiaohong.display_info()
    
