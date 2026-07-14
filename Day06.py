# oops - obect oriented programming ...... it helps to organize the programm using object and class
# class - it is a blueprint or template of the object
#object - it is the real instances of the class
#constructor - __init__ - it construct the function automatically when object is created ... it is a special memeber function of a class....it is used to initilizes the data members of an object...
#inheritance - the class derived from the base class and inherits the properities of base class in derived class
#abstraction - it hides the implementation of the program and show only the essential information
#polymorphism - it is ability to use same name for different tasks
#encapsulation- it hides the data from unauthorised access and convert into a single unit of class
# attribute are the variables used in the class
#  methods are the functions used inside the class

#class Student :
#   pass
#Student1 = Student()
#Student2= Student()

#print(Student1)
#print(Student2)

# constructor
# class Student :
    # def __init__(self):
    #   print("Student Created")
# s1=Student() 

# class Student :
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
# s1 = Student("Navjot", 20)
# print("Name :",s1.name)
# print("Age :", s1.age)

#  Method
# class Student : 
#     def __init__(self,name ,age):
#         self.name=name
#         self.age=age

#     def introduce(self):
#         print("My name is: ",self.name)
    
#     def suraj(self):
#         print("My age is: ",self.age)

# s1=Student("Navjot", 20)
# s1.introduce()        
# s1.suraj()
       
# encapsulation- binding the data and method to restrict the direct access and hides the data
        
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance= balance
#     def show_balance(self):
#         print("Balance : ",self.__balance)

# account = BankAccount(10000)
# account.show_balance()
# print(account.__balance)

# inheritance -- it aloows us to inherit  he properities from one class to another class

# class Animal():  #parent class
#     def eat(self):
#       print("Animal is eating")
# class Dog(Animal):    #child class
#    def bark(self):
#       print("Dog is barking")
# d = Dog()
# d.eat()
# d.bark()

# types of inheritance
 
# 1. single inheritance
 
# class Car():
#     def start(self):
#       print("Enigine is starting")
# class Key(Car):
#    def push(self):
#       print("key is rotating")
# d = Key()
# d.push()
# d.start()

# 2. multilevel

# class GrandFather():
#     def House(self):
#         print("house")
# class Father(GrandFather):
#     pass 
# class Son(Father):
#     pass
# s = Son()    
# s.House()
       
# 3. multiple 

class Father():
    def Driving(self):
        print("Driving")
class Mother():
    def Cooking(self):
        print("Cooking")
class Son(Father, Mother):
    pass
s = Son()
s.Driving()
s.Cooking()