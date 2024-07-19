# Day : 22 Introduction to Lists

# Python Lists
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.
# List can be changable after creation but in Tuple not changed
l = [3, 5, 6]
print(l)
print(type(l))

print("\n")

# List Index
# Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

# Accessing list items
# We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...
marks = ["Avinash", 56, "Abhishek", 78, "Karan", 34, True, False]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[6])
print(marks[7])
print(type(l))

print("\n")

# Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.
print(marks[-3]) # Negative Index
print(marks[len(marks)-3]) # Positive Index
print(marks[8-3]) # Positive Index
print(marks[5]) # Positive Index

print("\n")

# Check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.
if "Abhishek" in marks:
  print("Yes")
else:
  print("No")

print("\n")

# Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.
# listName[start : end : jumpIndex]

# Same thing applies for string as well!
if "ran" in "Karan":
  print("Yes")
else:
  print("No")

print("\n")

#If we need to print all element in marks list then
print(marks)
print(marks[:]) # Automatically take print(marks[0:len(marks)])
print(marks[1:])
print(marks[1:-1])
print(marks[1:4:2]) # Jump Index print(marks[To:From:Jump]) in which jump means print the element in the gap of two like a jumping

print("\n")

# Example of Jumping Index
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])

print("\n")

# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
lst = [i for i in range(4)]
print(lst)
lst = [i*i for i in range(4) if i % 2 == 0]
print(lst)

# Syntax:
# Listt = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.

# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

# Condition: Condition checks if the item should be added to the new list or not.

# Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

print("\n")
