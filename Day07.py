# polymorphism - same method name , but different behaviour.....concept that allows one interface to be used for different data types or objects...

# class Dog:
#     def sound(self):
#         print("Bark")

# class Cat:
#     def sound(self):
#         print("Meow")

# animal= [Dog(), Cat()]
# c1 = Cat()
# c1.sound() // is se hamme bar bar har ik ka object bnana padegga
# d1= Dog()
# d1.sound()
# for animal in animal:
#    animal.sound()        

# Abstraction - hidding implementation details and show only essential features

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("car is started")

# c= Car()
# c.start()

# super() keyword - it is used to call the parent class conctructor from child class

# class Person:
#     def __init__(self, name):
#         self.name=name
# class Student(Person):
#     def __init__(self, name, roll):
#         super().__init__(name)
#         self.roll = roll

# s=Student("Navjot",3006)
# print(s.name)
# print(s.roll)

#class variable vs instance variable
#  class variable
# class School():
#    Student="navjot"
# s1=School()
# print(s1.Student)

# instance variable
# class Student:
#    def __init__(self,name):
#     self.name=name

# s1=Student("Navjot")
# s2=Student("Sheetal")
# print(s1.name)
# print(s2.name)

# class Employee:
#     company="CORPTUBE"

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def display(self):
#         print(f"Name : {self.name}")
#         print(f"Salary : {self.salary}")

# class Developer(Employee):
#     def __init__(self, name, salary,tech):
#         super().__init__(name, salary)
#         self.tech=tech

#     def display(self):
#         super().display()
#         print(f"Technology: {self.tech}")

# dev=Developer("Navjot",50000,"Cyber")
# dev.display()
# print(dev.company)
