# Day : 34 Dictionary Methods

# Dictionary uses several built-in methods for manipulation.They are listed below

# Update Method

# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

print("Update a Dictionary by using update() method:")
employee1 = {122 : 45, 123 : 89, 567 : 89, 670 : 69}
employee2 = {222 : 67, 566 : 90}
print(employee1)
employee1.update(employee2)
print(employee1, "\n")

print("Update a Dictionary by using update() method:")
info1 = {'name':'Karan', 'age':19, 'eligible':True}
print(info1)
info1.update({'age':20})
info1.update({'DOB':2001})
print(info1)

# In python, 'Dictionary' are ordered collection of data items in python 3 onwards.

print("\n")

# Removing items from dictionary:
# There are a few methods that we can use to remove items from dictionary.

# Clear Method

# The clear() method removes all the items from the list.

print("Clear a Dictionary by using clear() method:")
employee3 = {122 : 45, 123 : 89, 567 : 89, 670 : 69}
print(employee3)
employee3.clear()
print(employee3, "\n")

print("Clear a Dictionary by using clear() method:")
info2 = {'name':'Karan', 'age':19, 'eligible':True}
print(info2)
info2.clear()
print(info2)

print("\n")

# empty dictionary

print("Empty Dictionary")
empty = {}
print(empty)

print("\n")

# Pop Method

# The pop() method removes the key-value pair whose key is passed as a parameter.

print("Pop a item from a Dictionary by using pop() method:")
employee4 = {122 : 45, 123 : 89, 567 : 89, 670 : 69}
print(employee4)
employee4.pop(122)
print(employee4, "\n")

print("Pop a item from a Dictionary by using pop() method:")
info3 = {'name':'Karan', 'age':19, 'eligible':True}
print(info3)
info3.pop('eligible')
print(info3)

print("\n")

# Popitem Method

# The popitem() method removes the last key-value pair from the dictionary.

print("Pop a item from a Dictionary by using popitem() method:")
employee5 = {122 : 45, 123 : 89, 567 : 89, 670 : 69}
print(employee5)
employee5.popitem() # Automatically popitem() remove last item from dictionary
print(employee5, "\n")

print("Pop a item from a Dictionary by using pop() method:")
info4 = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info4)
info4.popitem()
print(info4)

print("\n")

# Delete Method

# we can also use the del keyword to remove a dictionary item.

# If key is not provided, then the del keyword will delete the dictionary entirely.

print("Delete a Dictionary by using del() method:")
employee6 = {122 : 45, 123 : 89, 567 : 89, 670 : 69}
print(employee6)
del employee6 # Delete entire dictionary
#print(employee6, "\n") # It will generate the error b/c employee5 is delete entirely

print("Delete a Dictionary by using del() method:")
info5 = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info5)
del info5
# print(info5) # It will generate the error b/c employee5 is delete entirely

print("\n")

# Delete Method

print("Delete a item from a Dictionary by using del() method:")
employee7 = {122 : 45, 123 : 89, 567 : 89, 670 : 69}
print(employee7)
del employee7[122] # Delete entire dictionary
print(employee7, "\n") # Delete only one key-value

print("Delete a item from a Dictionary by using del() method:")
info6 = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
print(info6)
del info6['age']
print(info6)

print("\n")