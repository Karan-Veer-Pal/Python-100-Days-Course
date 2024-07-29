# Day : 31 Sets

# Sets is a collection of well defined objects. Sets are unordered collection. Sets does not contain repeated values or items or elements. Interpreter not maintaining the order of the set when we run print command.

# Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

info = {"Carla", 19, False, 5.9, 19} # Not maintaining the order.
print(info)

print("\n")

s = {2, 4, 2, 6}
print(s) # It will return {2, 4, 6}

print("\n")

# Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set

s1 = {}
print(type(s1)) # It will return <class 'dict'> because by default it is a dictionary when we create an empty set.

print("\n")

s2 = set()
print(type(s2)) # It will return <class 'set'>.

print("\n")

# Accessing set items:
# Using a For loop
# You can access items of set using a for loop.
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
