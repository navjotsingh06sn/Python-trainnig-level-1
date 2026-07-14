# type casting - it is used convert the data type into another data type according to its type
# ab= "48"
# print(int(ab))
# print(ab)
# print(type(ab))

# strings - modification , operation of string
# Ab="School"
# print(Ab[0:5] )
# for l in Ab:
#     print(l)

# list - when we store multiple items and assign to the single variables we called it a list.... it is written with[] ..... it allows duplicacy, ordered way, changeable(mutable)

# a=["Navjot","Satnam","Anjali","Mannat","Amarjot"]
# print(a)
# print(type(a))

# # printing duplicate value
# b=["Navjot","Satnam","Anjali","Mannat","Amarjot","Satnam"]
# print(b)

# print(len(b))

# changing item in list
# a[1]="BANSILAL"
# print(a)

# inserting item in list
# a.insert(0,"logo")
# print(a)

 # removing item from list
# a.remove("Navjot")
# print(a)

 # poping item from list
# a.pop()


# tupples - when we store multiple items and assign to single variable we called it a tupple..it is written with() .....it allows duplicacy, ordered way , and it is unchangeable(immutable)

# b=("Navjot","Satnam",4,5,6)
# print(b)
# print(type(b))


# set - it also stores multiple items in single variable it is use{} .. it doesnot allows duplicacy it is changeble and unordered

# c={"Navjot","Satnam",4,4,6}
# print(c)

# c.remove(6)
# print(c)

# c.add("bansilal")
# print(c)

# ab=["navjot@gmail.com","satnam@gmail.com","armaan@yahoo.com","satnam@gmail.com","harsh@gmail.com"]
# d=set(ab)
# print(d)


# dictinory - collection of data in a key value pairs..
ab={"name":"navjot", "roll no":"3272", "course":"btech","semster":"6th"}
print(ab)
print(ab["roll no"])

ab["name"]="satnam"
print(ab)

del ab["semster"]
print(ab)


