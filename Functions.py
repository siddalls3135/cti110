# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:00:03 2019

@author: sidda
"""

# In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function") 
 
# To call a function, use the function name followed by parenthesis:    
def my_function():
  print("Hello from a function")

my_function()

# The following example has a function with one parameter (fname). When the 
# function is called, we pass along a first name, which is 
# used inside the function to print the full name: 
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

# If we call the function without parameter, 
# it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# E.g. if you send a List as a parameter, 
# it will still be a List when it reaches the function:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# If the number of arguments are unknown, 
# add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")