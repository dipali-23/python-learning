# class Book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year

#     def display_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Publication Year: {self.publication_year}")

# book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
# book2 = Book("1984", "George Orwell", 1949)

# book1.display_info()
# book2.display_info()





# class Student:
#     school_name = "Tech Academy"  # Class variable

#     def __init__(self, name, roll):
#         self.name = name          # Instance variable
#         self.roll = roll

#     def show(self):
#         print(f"{self.name} (Roll: {self.roll}) - School: {Student.school_name}")

# student1 = Student("Alice", 101)
# student2 = Student("Bob", 102)

# student1.show()
# student2.show()






# encapsulation
# private variables
# class StudentGrade:
#     def __init__(self,grade):
#         self.__grade=grade
#     def get_grade(self):
#         return self.__grade
#     def set_grade(self,grade):
#         if grade>100 or grade<0:    
#             print("Invalid Grade")
#         else:
#             self.__grade=grade
#     def show(self):
#         print(f"Grade: {self.__grade}")

# student1=StudentGrade(90)
# student1.show()
# student1.set_grade(110)
# student1.show()
# student1.set_grade(85)
# student1.show()
# print(student1.get_grade())
        





# Inheritance
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         print(f"Name: {self.name}")

# class Employee(Person):
#     def __init__(self, name, emp_id):
#         super().__init__(name)  # call parent constructor
#         self.emp_id = emp_id

# e = Employee("Dipali", 101)
# print(e.name, e.emp_id)
# e.display()






# run-time polymorphism

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# animals=[Dog(), Cat()]
# for animal in animals:
#     animal.sound()  # Calls the overridden method in the respective subclass


# function polymorphism

# class Laptop:
#     def code(self):
#         print("Coding in Python")
# class Mobile:
#     def code(self):
#         print("Coding in Java")
# def start_coding(device):
#     device.code()  # Calls the overridden method in the respective subclass
# laptop = Laptop()
# mobile = Mobile()
# start_coding(laptop)  # Output: Coding in Python
# start_coding(mobile)  # Output: Coding in Java


# Abstract class
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Bark")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")
# class camel():
#     def make_sound(self):
#         print("grrr")

# def animal_sound(animal: Animal):
#     animal.make_sound()

# animal_sound(Dog())  # Bark
# animal_sound(Cat())  # Meow
# animal_sound(camel())  # grrr

# # a = Animal()  ❌ Will raise an error
# d = Dog()
# d.make_sound()  # Bark


# class method,instance method, static method

# class Employee:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role

#     def get_details(self):  # instance method
#         return f"{self.name} works as {self.role}"

# emp= Employee("John Doe", "Software Engineer")
# print(emp.get_details())  # Output: John Doe works as Software Engineer


# class Employee:
#     company = "TechCorp"  # class variable

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def get_company(cls):  # class method
#         return cls.company
# emp= Employee("John Doe")
# print(emp.get_company())  # Output: TechCorp
# print(Employee.get_company())  # Output: TechCorp

class MathUtils:
    @staticmethod
    def add(a, b):  # static method
        return a + b

print(MathUtils.add(5, 3))  # Output: 8
