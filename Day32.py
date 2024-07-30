# Day : 32 Set Methods

# Sets Theory:

# Joining Sets
# Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

# I. union() and update():
# The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

print("Union Method:")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.union(cities2)
print(cities3)

print("\n")

# Update Method use for add the items of first set into second set which are not present in the first sets. Like doing a update of cities4 set.

print("Update Method:")
cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities5 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities4.update(cities5)
print(cities4)

print("\n")

# II. intersection and intersection_update():
# The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

print("Intersection Method:")
cities6 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities7 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities8 = cities6.intersection(cities7)
print(cities8)

print("\n")

# Intersection_Update Method use for update one set on the basis of the Intersection means whose items are present in the Intersection, are only now present in the first set, eleminate the non-intersection items in a set.

print("Intersection_Update Method:")
cities9 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities10 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities9.intersection_update(cities10)
print(cities9)

print("\n")

# III. symmetric_difference and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

print("Symmetric_Difference Method:")
cities11 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities12 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities13 = cities11.symmetric_difference(cities12)
print(cities13)

print("\n")

# Symmetric_Difference_Update Method prints the items which are present in the symmetric_differrence and update the one set by the symmetric_difference.

print("Symmetric_Difference_Update Method:")
cities14 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities15 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities14.symmetric_difference_update(cities15)
print(cities14)

print("\n")

# IV. difference() and difference_update():
# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

print("Difference Method:")
cities16 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities17 = {"Seoul", "Kabul", "Delhi"}
cities18 = cities16.difference(cities17)
print(cities18)

print("\n")

# Difference_Update Method prints the items which are present in the differrence and update the one set by the difference.

print("Difference_Update Method:")
cities19 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities20 = {"Seoul", "Kabul", "Delhi"}
cities19.difference_update(cities20)
print(cities19)

print("\n")

# Set Methods
# There are several in-built methods used for the manipulation of set.They are explained below

# isdisjoint():
# The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

print("isdisjoint Method:")
cities21 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities22 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities21.isdisjoint(cities22))

print("\n")

# issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

print("issuperset Method:")
cities23 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities24 = {"Seoul", "Kabul"}
print(cities23.issuperset(cities24))
cities25 = {"Berlin", "Madrid","Delhi"}
print(cities23.issuperset(cities25))

print("\n")

# issubset():
# The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

print("issubset Method:")
cities26 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities27 = {"Delhi", "Madrid"}
print(cities27.issubset(cities26))

print("\n")

# add()
# If you want to add a single item to the set use the add() method.

print("add Method:")
cities28 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities28.add("Helsinki")
print(cities28)

print("\n")

# update()
# If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

print("update Method:")
cities29 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities30 = {"Helsinki", "Warsaw", "Seoul"}
cities29.update(cities30)
print(cities29)

print("\n")

# remove()/discard()
# We can use remove() and discard() methods to remove items form list.

print("remove()/discard() Method:")
cities31 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities31.remove("Tokyo")
print(cities31)

# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

# Example:
# cities32 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities32.remove("Seoul")
# print(cities32)

print("\n")

# pop()
# This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

print("pop Method:")
cities33 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities33.pop()
print(cities33)
print(item)

print("\n")

# del
# del is not a method, rather it is a keyword which deletes the set entirely.

# NameError: name 'cities34' is not defined We get an error because our entire set has been deleted and there is no variable called cities34 which contains a set.

# print("pop Method:")
# cities34 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities34
# print(cities34)

print("\n")

# What if we don’t want to delete the entire set, we just want to delete all items within that set?

# clear():
# This method clears all items in the set and prints an empty set.

print("clear Method:")
cities35 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities25.clear()
print(cities25)

print("\n")

# Check if item exists
# You can also check if an item exists in the set or not.

# Example
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
print("\n")
