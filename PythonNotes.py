# This is a comment

print("Hello World")

x = 1
if x > 0:
    print("x is greater than 0")

else:
    print("x is less than 0")

# Variables
# use lower case because upper case is typically used with class objects

age = 'two'
print(type(age))

# string() int() float()
number = float(1)
print(type(number))

number_and_age = (number, age)
print(number_and_age)

# Data Types
# Mutable = can edit variable after creation
# Immutable = cannot edit variable after creation
# list, tuple, dictionary, frozenset, sheet

our_list = ["a","b","c",1.5]
print(our_list)

our_tuple = ("a","b","c")
print(our_tuple)

our_dictionary = {"name":"Jason", "age":"34"}
print(our_dictionary)

our_set = {"one","two","three","two"}
print(our_set)

our_frozenset = frozenset(our_set)
print(our_frozenset)

# Numbers

import math

x = 1 # integer
y = 1.4 # float
z = 2+3j # complex numbers

print(type(z))

result = x + y
print(result)

print(math.ceil(y))

# Lists

our_list = ["a","b","c",1,1.5]
print(our_list)

our_list.append("d")
print(our_list)

print(our_list[0]) # index our List
our_list.insert(0,"First element")
print(our_list)

our_list.remove("First element")
print(our_list)

our_list.pop(5) # remove item from list by order
print(our_list)

nested_list = [[1,2,3],3,4,5] # nest a list within a List
print(nested_list)

# Strings

string_a = "Jason" # this string in Python is an array
print(len(string_a)) # calculate the length of a string

print(string_a[0]) # pull out a letter from a string based on position

print(string_a.upper()) # upper case letters in string
print(string_a.lower()) # lower case letters in string

string_b = "Jason, Carleigh, Jayson, Hope"
print(string_b.split(",")) # split string

# tuple - immutable object

tuple_a = ("Cat", "Dog","Mouse")

print(tuple_a[1])

# Sets and Frozensets

set_a = {"one", "two","three"}
set_a.add("four") # add an element to a set
print(set_a)

set_a.update(["five","six","seven"]) # add multiple elements to a set
print(set_a)

# If Loops

x = 1
y = 2
z = 3

if x < y and y < z: # can use and/or here
    print("yes")

else:
    print("no")

# While Loops

i = 1

while 1 < 10: # continues the loop as long as this is true
    i = i + 1 # condition that continues the while loop
    print(i)
    if i == 6: # nested while loop
        break # stops the loop action

# For Loops

name = "Jason"

for element in name:  # each string value in name
    print(element)

list_a = ["jason","Carleigh","Jayson","Hope"]

for name in list_a:
    print(name)

list_b = [1,2,3,4,5]

for number in list_b:
    print(number+5)

# Functions - always starts lower case and declared using def

def add_two_six(x):
    result = x + 2.6
    print(result)

amount = add_two_six(7) # can calculate results off those functions quickly

# Class objects - a class is an object that we can use to create other objects made up of functions and attributes
# classes typically start with Upper cased letters

class Report: # when somones uses this class "Report" to create their own object, it has the title and author attributes
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def write_report(self, text):
        return "{} By: {} \n {}".format(self.title, self.author, text)


my_report = Report("I should have studied", "Jason")

print(my_report.write_report("This is OOP"))
