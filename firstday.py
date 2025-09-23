print("Hello World")
# Variables and Data types in Python
# Operators in Python
# Type conversion and Type casting in Python
"""
# variable
var = "Avishkar"
var2 = False
var3 = None


# data type of var
print(type(var)) # <class 'str'>
print(type(var2)) # <class 'bool'>
print(type(var3)) # <class 'NoneType'>


# address of var
print(id(var)) # 1752349772208
print(id(var2)) # 140722490372560
print(id(var3)) # 140722490372592



#OPERATORS IN PYTHON
# 1.arithmetic operators(+,-,*,/,//,%,**) -> when we divide with / it gives float value

# 2.relational / Comparison operators(>,<,>=,<=,==,!=)

# 3.Assignment operators(=,+=,-=,*=,/=,//=,%=,**=)

# 4.logical operators(and,or,not) 



# Type CONVERSION(done by intarpritor automatically) and type CASTING(manually done by us)
# 1.Type conversion
a,b = 5,2.2
sum = a + b
print(sum) # 7.2 int -> float


# 2.Type Casting 
a = "2"
b = 4.25
# print(a+b) -> TypeError: can only concatenate str (not "float") to str
# so we will do type casting
print(float(a) + b)

# Examples of type casting (int(),float(),str(),bool(),list(),tuple(),set(),dict(),ord(),chr(),hex(),oct(),bin(),complex())
name = "Avishkar "
#print(float(name)) -> ValueError: could not convert string to float: 'Avishkar'

#print(int(name)) # -> ValueError: invalid literal for int() with base 10: 'Avishkar'

print(str(name)) # Avishkar  it is ordered and allows duplicates, we can access by index

print(bool(name)) # True it is either True or False, empty string is False, non-empty string is True

print(list(name)) # ['A', 'v', 'i', 's', 'h', 'k', 'a', 'r', ' '] it is ordered and allows duplicates, we can access by index

print(set(name)) # {'A', 'r', 'i', 'v', 'a', 's', 'h', ' ', 'k'} it is unordered and unique, we cant access by index, we can operations like union, intersection, difference

print(tuple(name)) # ('A', 'v', 'i', 's', 'h', 'k', 'a', 'r', ' ') it is ordered and allows duplicates, we can access by index

#print (dict(name)) # ValueError: dictionary update sequence element #0 has length 1; 2 is required, it is unordered and unique, we access by key, key-value pair
print(dict.fromkeys(name)) # {'A': None, 'v': None, 'i': None, 's': None, 'h': None, 'k': None, 'a': None, 'r': None, ' ': None} creates dictionary with keys from the iterable and values as None

print(ord("A")) # 65 gives ascii value of character, and doesnt work for string of length > 1

print(chr(65)) # A gives character of ascii value, and works for value from 0 to 1114111

print(hex(65)) # 0x41 gives hexadecimal value of integer, and works for negative values too 

print(oct(65)) # 0o101 gives octal value of integer

print(bin(65)) # 0b1000001 gives binary value of integer

print(complex(2)) # (2+0j) gives complex number (o,2) -> 2j, (2,3) -> (2+3j), (2.5,3.5) -> (2.5+3.5j), (2+3j) -> (2+3j), (2,0) -> (2+0j)


#simple Questions and Answers
# Q1. write a program to input two numbers and print their sum, difference, product, quotient, floor division, modulus and power.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum: ", a+b)
print("Difference: ", a-b)
print("Product: ", a*b)
print("Quotient: ", a/b)
print("Floor Division: ", a//b)
print("Modulus: ", a%b)
print("Power: ", a**b)

# Q2. write a program to input a side of a square and print its area and perimeter.
side = int(input("Enter side of square: "))
print("Area: ", side*side)
print("Area: ", side**2)
print("Perimeter: ", 4*side)

# Q3. write a program to input 2 floating numbers and print their average.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Average: ", (a+b)/2)

# Q4. write a program to input 2 numbers and print True if a is greater than or equal to b, if not print False.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(a >= b)
"""
