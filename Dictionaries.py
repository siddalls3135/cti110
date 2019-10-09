# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:22:48 2019

@author: sidda
"""

# =============================================================================
# clear()
# Removes all the elements from the dictionary
# copy()
# Returns a copy of the dictionary
# fromkeys()
# Returns a dictionary with the specified keys and values
# get()
# Returns the value of the specified key
# items()
# Returns a list containing a tuple for each key value pair
# keys()
# Returns a list containing the dictionary's keys
# pop()
# Removes the element with the specified key
# popitem()
# Removes the last inserted key-value pair
# setdefault()
# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()
# Updates the dictionary with the specified key-value pairs
# values()
# Returns a list of all the values in the dictionary
# =============================================================================

#A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict)

#You can change the value of a specific item by referring to its key name:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict["year"] = 2018

# check if model is present in the dictionary:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 
  
# Adding an item to the dictionary is done by using a new index key 
# and assigning a value to it:  
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict["color"] = "red"
print(thisdict)  

# The pop() method removes the item with the specified key name:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict.pop("model")
print(thisdict) 

# The del keyword removes the item with the specified key name:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
del thisdict["model"]
print(thisdict) 

# The clear() keyword empties the dictionary:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict.clear()
print(thisdict) 

# Make a copy of a dictionary with the copy() method:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
mydict = thisdict.copy()
print(mydict)

# Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

# Create three dictionaries, than create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
} 

