print("Second Day of Python")
"""
# Strings in Python
s = "Avishkar"
s2 = "Gaware"


# Concatenation
print(s + " " + s2) # Avishkar Gaware


# length of string
print(len(s)) # 8


# indexing
print(s[0]) # A
print(s[-1]) # r


# reversing a string
print(s[::-1]) # rakhsivA


# we cannot change a string (immutable)
# s[0] = "a" -> TypeError: 'str' object does not support item assignment
# by using index we can access the string but cannot change it


# slicing
#str[starting_index : ending_index : step] # ending_index is not included

print(s[2:]) # ishkar
print(s[:5]) # Avish

 # Negative indexing
 # A   P  P  L  E
 # -5 -4 -3 -2 -1 
fruit = "APPLE"
print(fruit[-3 : -1]) # PL
print(fruit[-2:-4:-1]) # LP


# functions
# enswith("") -> return true if string ends with substring
str = "i am a coder"
print(str.endswith("der"))# True

#capitalize() -> capitalize 1st char
print(str.capitalize())#I am a coder

# replace(old,new) -> replace all occurences of old with new
print(str.replace(" ", ""))# iamacoder
print(str.replace("coder", "engineer"))# i am a engineer /if word not found return original str

# find(word) -> return 1st index of 1st occurer else -1
print(str.find("am")) #2
print(str.find("ami")) #-1

# count(word) -> count occurence of substring
print(str.count("am")) # 1
print(str.count('a')) # 2

# practice Questions

# 1. WAP to input user's name & print its length

#name = input("Enter your name:")
#print("Length of your name is", len(name))

# 2. WAp to find the occurence of '$' in a string.(count)
str2 = 'Hi, $ i am the $ symbol in your string as a $'
print("Count of $ in string is", str2.count('$'))


# conditional statements
# if-elif-else
age = 21
if(age >= 18):
    print("You are eligible")
    print("You can vote, you can drive")
elif(age == 17):
    print("After 1 year you are eligible")
else:
    print("you are minor")


marks = float(input("Enter marks of student:"))

if(marks >= 90):
    grade = 'A'
elif(marks >= 80):
    grade = 'B'
elif(marks >= 70):
    grade = 'C'
else:
    grade = 'D'

print(f"Grade of the student is '{grade}' ")
print("graded of student is '{}'".format(grade)) 

# Nesting
age = 17
if(age >= 18):
    if(age >= 80):
        print("you canot drive above 80")
    else:
        print("can drive")
else:
    print("cannot drive minor")


# Practice Question
# 1.WAP to check if a number entered by the user is odd or even
number = int(input("Enter a number:"))
if number % 2 == 0:
    print(number,"is even")
else: print(number, "is odd")

# 2.WAP to find the gratest no of 3 numbers entered by user
numbers = [int(x) for x in input("Enter num sep by ',':").split(',')]
print(numbers)
#print(max(numbers))
maxnum = -1
for num in numbers:
    if num > maxnum:
        maxnum = num
print("Max num is:", maxnum)
######## OR ################################################################################################################
a = int(input("Enter 1st num:"))
b = int(input("Enter 2nd num:"))
c = int(input("Enter 3rd num:"))

if (a >= b and a >= c):
    print(a, "is large")
elif(b >= c):
    print(b, "is large") 
else:
    print(c,"is large")


# 3.WAP to check if num entered is multiple of 7 or not
numm = int(input("Enter a num:"))
if (numm % 7 == 0):
    print(numm,"is multiple of 7")
else: print(numm, "is not multiple of 7")


# LIST -> built in data-type that stores set of values, it can store element of different types

marks = [78,95,76,33,64]

# mutable
student = ["avishkar", 60.17, "Hingoli"]
student[0] = "Aviraj"
print(student[0])#Aviraj

#length of list
print(len(marks))

# List Slicing -> list_name[starting_idx:ending_idx] -> ending index not included
marks2 = [76,87,98,96,97,93,81]
print(marks2[2:5]) # [98, 96, 97]
print(marks2[-1:]) # [81]
print(marks2[-1::-1]) # [81, 93, 97, 96, 98, 87, 76]
print(marks2[-4:-2]) # [96,97]



# List Methods -> methods are specific for list, for string not like a function (len())
list = [2,1,7]


# append
# print(list.append(6)) -> it adds 6 in list but append doesnot return anything -> None
list.append(6)
# list.append([4,6]) -> not allowed only one value accepted
# list.append("Hello") -> it will append but sort method gives TypeError
print(list) # [2, 1, 7, 6]


# sort()
# list = list.sort() -> sort() does not return sorted list, it returns the none
# print(list.sort()) -> so it gives none, first sort list.sort() then print(list)
list.sort() # sort in ascending order default
print(list) # [1, 2, 6, 7]

list.sort(reverse = True) # sort in descending order
print(list) # [7, 6, 2, 1]


# reverse()
# print(list.reverse()) -> none reverse() dont return anything it reverse list in original list itself
list.reverse()
print(list) #[1, 2, 6, 7]


# insert insert(idx,el) -> require 2 arguments
list.insert(0,87)
print(list) # [87, 1, 2, 6, 7]

list.insert(-1,16) #This inserts the element at last index but last item in the list shifted to right, to insert at last use append
print(list) # [87, 1, 2, 6, 16, 7]

list.insert(1,[67,89,16,70]) # [87, [67, 89, 16, 70], 1, 2, 6, 16, 7] -> we can insert list into list
print(list) # [87, [67, 89, 16, 70], 1, 2, 6, 16, 7]


# remove() method -> removes first occurence of element, only one argument
list.remove(1)


# pop(idx) method -> removes element at idx, we can access that element
print("pop",list.pop(1)) # pop [67, 89, 16, 70] whole element at idx return and remove(sub-list)
print(list.pop()) # if index not given pop return last element and remove
list.pop(2) # removes element at index 2





# Tuples in Python -> built-in data type that lets us create IMMUTABLE sequence of values
# we can access tuple by index, ',' at the end of tuple ele is completely fine
tup = (87,64,33,95,33,) 
print(tup[0])
# tup[0] = 96 -> TypeError: 'tuple' object does not support item assignment like string


# if you want to create tuple with 1 element then must use ',' after element else python consider it as int
tupl = (1,) 
print(type(tupl)) # <class 'tuple'>

tupl2 = (1)
print(type(tupl2)) # <class 'int'>

# slicing in tuple -> same as string and list
print(tup[1:3]) # (64, 33)


# Methods in tuple
# tup.index(el) -> return index of first occurence
print(tup.index(33)) # 2

# tup.count(el) -> counts total occurences
print(tup.count(34)) # 0



# practice Question

# 1.WAP  to ask the user to enter name of their 3 fav. movies & store them in a list

# movies = input("Enter your 3 fav movies:").split()
# print(movies)

# movies.append(input("Enter 1st movie")) \n movies.append(input("Enter 2nd movie")) movies.append(input("Enter 3rd movie")) \n print(movies)

movies = []
movie1 = input("Enter 1st fav. movie:")
movie2 = input("Enter 2nd fav. movie:")
movie3 = input("Enter 3rd fav. movie:")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)


# 2.WAP to check if a lsit contains a palindrome of elements.
givenlist = [1,2,3,2,1]
cpy_list = givenlist.copy()
cpy_list.reverse()

if givenlist == cpy_list:
    print("Given list is palindrome")
else:
    print("not a palindrome")
"""

"""
def is_palindrome(list):
    n = len(list)

    for i in range(n):
        if list[i] != list[n-i-1]:
            return 0
    return 1

# list = [1,"abc","abc",1]
list = [1,2,3,2,1]
if is_palindrome(list):
    print("list is palindrome")
else: 
    print("List is not a palindrome")
    
"""

# 3.WAP to count the no. of student with the "A" grade in the following tuple
grade = ("c","D","A","A","B","a","A")

print(grade.count("A")) # 3 case sensitive

# 4. store the above values in a list and sort them from "A" to "D".
grade = ["C","D","A","A","B","a","A"]
grade.sort()
print(grade)