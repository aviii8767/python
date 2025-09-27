print("Day 3")
"""
# Dictionary in Python {key : value,}
# they are unordered, mutable(changeable)& don't allow duplicate keys
# it accept any type of data in one dict
dict = {
    "name" : "SAi",
    "subject" : ["phy", "chem", "bio"],
    "marks" : (91,87,98),
    "is_adult" : True
}

# values are access using key
print(dict["name"]) # SAi
#print(dict["age"]) # KeyError: 'age' -> for non existing key

# to assign or add new
dict["key"] = "value"

dict["name"] = "Ram" # overwrite


# Nested Dictionaries
student = {
    "name" : "Avishkar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "bio" : 99

    },
    "age" : 21
}
# accessing nested  dictionary
#print(student["subjects"]) # {'phy': 97, 'chem': 98, 'bio': 99}
#print(student["subjects"]["bio"]) # 99

# Dictionary Methods

# 1.keys()
print(student.keys()) # returns all keys in <class 'dict_keys'> format -> dict_keys(['name', 'subjects', 'age'])
print(student["subjects"].keys()) # dict_keys(['phy', 'chem', 'bio'])

# type casting into list
print(list(student.keys())) # ['name', 'subjects', 'age'] 

print(len(student)) # 3 


# 2.values() also used with len 
print(student.values()) # returns all values -> dict_values(['Avishkar', {'phy': 97, 'chem': 98, 'bio': 99}, 21])
print(student["subjects"].values()) # dict_values([97, 98, 99])
print(list(student.values())) # ['Avishkar', {'phy': 97, 'chem': 98, 'bio': 99}, 21]


# 3.items()
print(student.items()) # returns all (key,val) pairs as tuple -> dict_items([('name', 'Avishkar'), ('subjects', {'phy': 97, 'chem': 98, 'bio': 99}), ('age', 21)])
print(student["subjects"].items()) # dict_items([('phy', 97), ('chem', 98), ('bio', 99)])
pairs = list(student.items()) # [('name', 'Avishkar'), ('subjects', {'phy': 97, 'chem': 98, 'bio': 99}), ('age', 21)]
print(pairs[0]) # ('name', 'Avishkar')
print(pairs[0][1]) # Avishkar
print(pairs[1][0]) # subjects
print(pairs[1][1]) # {'phy': 97, 'chem': 98, 'bio': 99}
print(pairs[1][1]["phy"]) # 97


# 4.get("key") -> returns the key according to value same as dict["key"] but 
# if key is not present in dict then normal method gives KeyError while get method erturns None
# print(student["name2"]) # KeyError: 'name2'
print(student.get("name2")) # None -> following code work finely


# 5.update({key:val}) -> insert the specified items to the dictionary
student.update({"city" : "Hingoli",})

# we can pass newDict also
newDict = {"village" : "Pimprala", "home" : "krushna Niwas"}
student.update(newDict)

# we can update existing value
student.update({"name":"Aviraj"})
"""

# Set{} in Python 
# set is a collection of unordered items
# each element in the set must be unique & immutable (set -> mutable, set-elements -> immutable)
# in set we cannot store list and dict as they are mutable other than this we can store(like tuple, str, float, int, bool)

collection = {1,2,3,4,4,"Hello", "Mom","mom"}
print(collection) # {1, 2, 3, 4, 'Mom', 'mom', 'Hello'} -> ignores duplicate values
print(len(collection)) # 7 total number of items

# empty set syntax
collection = {} # this is empty dictionary syntax
print(type(collection)) # <class 'dict'>
emty_set = set() 
print(emty_set) # set()
print(type(emty_set)) # <class 'set'>


# Set Methods

# 1.add(el) -> adds an element, we can pass tuple but not list, dict
emty_set.add(4)
print(emty_set) # {4}

emty_set.add((1,2,3)) # we can add tuple
print(emty_set) # {(1, 2, 3), 4}

# emty_set.add([7,8,9]) # TypeError: unhashable type: 'list' -> immutable values are hashable



# 2.remove(el) -> removes the element from set
emty_set.remove(4)
# emty_set.remove(87) # KeyError: 87 if we try to remove non-existing element 



# 3.clear() -> empties the set
emty_set = {23,45,11,23,545}
print(emty_set) # {545, 11, 45, 23} 
emty_set.clear()
print(len(emty_set)) # 0


# 4.pop() -. removes a random value
emty_set = {45,5,7,6,8,}
print(emty_set) # stored as {5, 6, 7, 8, 45}
print(emty_set.pop()) # 5 -> mostly pop first element after store
print(emty_set) # {6, 7, 8, 45} -> 5 removed


# 5.union(set2) -> combines both set values & return new
set1 = {1,3,2}
set2 = {4,5,3,2}
print(set1.union(set2)) # {1, 2, 3, 4, 5}


# 6.intersection(set2) -> combines common values & return new
print(set1.intersection(set2)) # {2, 3}


#practice Q

# 1. store word meaning in dictionary

word_dict = {"table" : ("a piece of furniture", "list of facts & figures"), "cat" : "a small animal which sonds meow-meoww"}

# 2. you are given a list of subjects for students. assume one classroom is required for 1 subject.
# how many classrooms are needed by all students.
"python","java","C++","python","javascript","java","python","java","C++","C"

subjects = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print("Total classrooms needed:",len(subjects))


# 3. WAP to enter marks of 3 sub from user and store them in a dictionary. start with an empty dictionary &
# add one by one. use subject name as key & marks as value

# result = {}
# result.update({input("Enter Subject name:") : int(input("Enter marks:"))})
# result.update({input("Enter Subject name:") : int(input("Enter marks:"))})
# result.update({input("Enter Subject name:") : int(input("Enter marks:"))})
# print(result)


# 4.figure out way to store 9 & 9.0 as seperate values in the set

# a. without using built-in data type -> one value as a string &  one as a int
values = {"9", 9.0}

# b. using built-in data types (list or tuple)
values = {
    ("float", 9.0),
    ("int", 9)
}
