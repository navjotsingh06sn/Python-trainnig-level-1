# functions- in fuction hamme teen chiijje chahiye. ik usko define krna hai dusra uski body bnani hai and then fir usse call krma hai
# function is a reusable block of code 

# def Std_name():
#     print("Navjot")
# Std_name()

# function with parameter - jab bhi hamme issme function define krte hai tab function bhi call hota hai..tab function main parameters likhte hai.

# def Student_name(a,b):
#     c=a+b
#     print(c)
# Student_name(5,6)

# def St_name(name):
#     print(name)
# St_name("NAVJOT")
# St_name("ARMAAN")
# St_name("SATNAM")
# St_name("MANNAT")
# St_name("ANJALI")

# def Lenght_scale(q,l):
#     area=q*l
#     return area
# a=Lenght_scale(9,7)
# print(a)


# a=int(input("Enter the first Number : "))
# b=int(input("Enter the second Number : "))
# def all_t(a,b):
#     c=a*b
#     # print(c)
#     return c
# print(all_t(a,b))

# def Add_no(f,d,ab,):
#     f=int(input("Enter the no : "))
#     d=int(input("Enter the no : "))
#     e=f+d
#     return e
# print(Add_no(f,d))

# lambda function

# ab=lambda x: x*x
# print(ab(6))

# file handling - it has three types of files 1. .txt, 2. .CSV, 3. JSON.  we can modify files using commands.... with the terminal without using mannualy we use touch (name of file).txt to make file and to make folder we use mkdir (folder ka nam)
# we can read the data in files which is located at other place on terminal by using commands 
# file=open("data.txt" ,"r")
# s=file.read()
# print(s)
# file.close()

# file=open("data.txt" ,"w")
# v=file.write()
# print(v)
# file.close()

# file=open("data.txt" ,"a")
# v=file.append()
# print(v)
# file.close()
import os 
os.remove("data.txt")


