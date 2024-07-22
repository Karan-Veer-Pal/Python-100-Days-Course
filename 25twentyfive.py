# Day : 25 Operation on Tuples

# We cannot manipulate tuple not in a direct way, if you want to change, add or remove a value from a 'Tuple', Do there's no direct method to do that, You have to copy it and make a list then you have to do changes in that list and then you have to change it again in 'Tuple'.

# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

print("\n")

# However, we can directly concatenate two tuples without converting them to list.

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

print("\n")

# Tuple methods
# As tuple is immutable type of collection of elements it have limited built in methods.They are explained below

# count() Method
# The count() method of Tuple returns the number of times the given element appears in the tuple.
# index() method
# The Index() method returns the first occurrence of the given element from the tuple.

tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
res = tuple1.index(3)
res = tuple1.index(3, 4, 8)
print('Count of 3 in Tuple1 is:', res)