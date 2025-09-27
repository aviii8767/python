print("Welcome to day 4 in python")
# loops in python

# 1.while loop
"""
iterator
while (condition):
    statement to perform
    iterator increment/decrement
"""

"""
# practice Q using while loop
# 1. print num 1-100
num = 1
while num <= 100:
    print(num)
    num += 1

# 2. print num from 100-1
num = 100
while num >= 1:
    print(num)
    num -= 1

# 3. print multiplication table of a number n
n = 22
i = 1
while i<= 10:
    print(n, "x", i, "=", n*i )
    i +=1

# 4. print the elements of the following list using a loop
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(list):
    print(list[i], end = ",")
    i += 1
print("\n")

# 5.search for a num x in this tuple using loop
tupl = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 50
i = 0
found = False
while i < len(tupl):
    if tupl[i] == x:
        found = True
        print("x found at index:",i)
        break
    i += 1
if not found:
    print("x not present in given tuple")


# break -> used to terminate  the loop when encountered
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

# continue -> terminates execution in the current iteration & continues execution of the loop with the next iteration
i = 0
while i <= 20:
    if(i % 2 == 0):
        i += 1
        continue # skip the even num
    print(i)
    i += 1

    
# for loop
# used for sequential traversal. for traversing list, string, tuples etc.

# for el in list:
     # some work

# for loop with else -> useful with break statement, else wala part break wale case main execute nahi hoga
# here if we dont use else then that statement always executes after for loop
list = [4,7,12]
for el in list:
    if el == 7:
        print("Found")
        break
else:
    print("element not found")


# for loop to calculate char in string without space
str = "Avishkar Purushottam Gaware"
count = 0
for char in str:
    if char == " ":
        continue
    count += 1
    print(char)
print(count)

# range() -> range fn returns seq. of numbers, starting from 0 by default, and increments by 1 (default), and stops before a specified number.
# range(start?,stop,step?)

print(range(5)) # o/p:range(0, 5)

seq = range(4)
print(seq[0]) # 0
print(seq[3]) # 3

for i in seq:
    print(i, end = ",") # 0,1,2,3,
print()

for i in range(4):
    print(i, end = ",") # 0,1,2,3,
print()

for i in range(0,10,2):
    print(i, end =",") # 0,2,4,6,8,
print()

for i in range(10,0,-2):
    print(i, end = ",") # 10,8,6,4,2,
print()

# practice Q using for loop and range() fn

# 1.print num from 1 to 100
for i in range(1,101):
    print(i)

# 2.print num from 100 to 1 
for i in range(100,0,-1):
    print(i)

# 3. print a multiplication table of a num n
n = 87
for i in range(1,11):
    print(n, "x", i, "=", n*i)

# pass Statement -> pass is a null statement that does nothing. It is used as a placeholder for future code.
# generally used in exceptions or try catch
for el in range(10):
    pass


# practicce Q.

# 1. WAP to find the sum of first n natural numbers. (using while)
n= 6
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Total Sum =",sum)

# 2. WAP to find the factorial of first n numbers(using for)
n = 7
factorial = 1
for i in range(1,n+1):
    factorial *= i
print("Factorial =",factorial)
"""

# functions & Recursion / fn -> Block of statements that perform a specific task
"""
def fun_name(param1,param2..):
    # some work
    return val
func_name(arg1,arg2..) -> function call
"""
"""
# the function which dont return anything in return that results in to None
def print_hello():
    print("Hello")
output = print_hello()
print(output) # none -> print(print_hello())


# avg of 3 num
def cal_avg(a,b,c):
    return (a + b + c)/3

print("Avg:",cal_avg(95,97,98))

# Types -> 1.Built-in func (print(), len(), type(), range())  2.User defined fun


# Default parsmeters -> assign a def value to para, which is used when no argument is passed
# ek baar default parameter set kiya ki uske baad wale sare para default wale hee hone chahiye, non-default not acceptable -> 
# def my_fun(c,a=4,b=2) allowed -> def my_fun(a=4,b,c) not allowed

# practice Q.
# 1. WAF to print the length of a list.(list is the parameter)

def calculate_length(list):
    return len(list)

cities = ["hingoli", "nanded", "parbhani", "latur", "beed"]
length = calculate_length(cities)
print("Length =", length)


# 2.WAF to print the elements of a list in a single line.

def print_el(list):
    for el in list:
        print(el, end = " ")
print_el(cities)
print()

# 3.WAF to find the factorial of n.(n is the parameter)

def cal_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print("Factorial = ",fact)

cal_factorial(7)


# 4. WAF to convert USD to INR

def usd_to_inr_converter(usd_val):
    inr_val = usd_val * 88.77
    print(usd_val, "USD in INR =", inr_val) 

usd_to_inr_converter(15000)

# 5. WAF that takes num and return "ODD" if num is odd else "EVEN"
def check_odd_even(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"

print(check_odd_even(88))

# Recursion -> when a fn calls itself repeatedly
def show(n):
    if (n == 0): # base case
        return
    print(n)
    show(n-1)
show(4)

# call stack -> fn call stack #############################################watch again from lect 6-40:00 min###########


# find factorial using recursion
def fact(n):
    if (n == 0 or n == 1):
        return 1
    return n * fact(n-1)
    
print("Factorial =",fact(7))

# practice Q
# 1. Write a recursion fun to calculate the sum of first n natural numbers

def calc_sum(n):
    if n == 0:
        return 0
    return calc_sum(n-1) + n

print(calc_sum(100))
"""

# 2. Write a recursive fun to print all el in a list.

def print_list(list,idx = 0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)

fruits = ["Citafhal", "Aamba", "Jambhul", "Borr", "Ramfhal", "Jaamb", "Keli"]
print_list(fruits)
