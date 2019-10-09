c = [-45, 6, 0, 72, 1543]
print (c[0])
print (len(c))
print ("how long is c?:", len(c), ("numbers long"))
print (c[-1])


# accessing numbers in a list
# c = [-45, 6, 0, 72, 1543]
#        c[0]    c[1]     c[2]     c[3]     c[4]
# c =    -45       6        0       72      1543
#       c[-5]   c[-4]    c[-3]    c[-2]    c[-1]


print (c[0] - 5)

print (c[-1] - 1500 / 2)

s = "hello"

# s = "hello"
#     s[0]     s[1]     s[2]     s[3]     s[4]
#       h        e        l        l        o
#    s[-5]    s[-4]    s[-3]    s[-2]    s[-1]
print (s[0])

test = [1, 2, 3, 4]
print (test[0])
# when accessing items in a list the [0], [1] etc is called by
# name you give it. I.E "c", "s", "test"

print (c[0] + test[0])

# add items in a tuple
for number in range (1,6):
    c += [number]

print (c)

# added pyton test to the "s" tuple
s += " python test"
print (s)

# prints verticle list with index value
for i in range (len(s)):
    print (f"{i}: {s[i]}")
    print (s[15])
    # prints single place with index value
    print (f" {i}: {s[14]}")
    
    
student_tuple = "steven", "siddall", 3.3 , 3.5
print (student_tuple)
print (len(student_tuple))

#trailing , indicates its a tuple
a_single_tuple = ("red",)
print (a_single_tuple)



time_tuple = (9, 16, 1)
print (time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2])

# print tuple1 and tuple 2. They are differnt. 
# tuple2 references tuple 1 and is the same until
# you add more to tuple1 with the following
tuple1 = (10, 20, 30)
tuple2 = tuple1
tuple1 += (40, 50)
    
numbers = [1, 2, 3, 4, 5]
# adds items to tuple
numbers += (6, 7)
# first list is amanda thru numbers
# list within the list are the nubmers
# calling the a list within a list is done by frist 
#referencing the 1st list with c[2] then referecing 
# the list inside the list with c[1]
# i.e student_tuple [2] [1] = 85
# you are telling the program to replace 75 with 85 when you 
# use that code
                 #c[0]      c[1]       c[2]
                               #    [c0]c[1]c[2]
student_tuple = ("amanda", "Blue" , [98, 75, 87])
# replaces value [1] with 85 instead of 75
student_tuple [2][1] = 85
print (student_tuple)

# replace duplicate numbers with concatinated numbers
test1 = "steven", "bishop", "Siddall", [1, 2, 2, 4]
#changed duplicate 2 to a 3
test1 [3][2] = 3
# adds numbers to test1
test1 += (5, 6, 7, 8)
print (test1)

test2 = ["steven", "siddall"]
test2 [1] = "bishop"
print (test2)

# in order to make a change to a tuple ( name or number)
# the group must be inside []
# if the following code was 
# test3 = ["steven", "bishop", "bishop"], 1, 2, 3, 3
# you can only change the names, not the numbers
test3 = ["steven", "bishop", "bishop"], 1, 2, 3, 3
# change duplicate name
test3 [0] [2] = "siddall"
# change duplicate number
test3 [1] [3] = 4
print (test3)

# This example returns the items from index -4 (included) to index -1 (excluded)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
# thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 

# To add an item to the end of the list, use the append() method:  
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) 

# The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) 

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

J# oin two list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)