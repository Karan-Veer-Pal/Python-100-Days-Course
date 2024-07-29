# Day : 24 Tuples

# Python Tuples
# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

tup1 = (1, 5, 6)
print(type(tup1), tup1)

print("\n")

tup2 = (1, 5)
print(type(tup2), tup2)

print("\n")

tup3 = (1)
print(type(tup3), tup3)

print("\n")

tup4 = (1,)
print(type(tup4), tup4)

print("\n")

#In tuple we cannot change the element value

# Tuple Indexes
# Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.
tup5 = (1, 2, 76, 342, 32, "green", True)
print(type(tup5), tup5)
print("Length of tuple", len(tup5))
print(tup5[0])
print(tup5[1])
print(tup5[2])
print(tup5[3])
print(tup5[4])
print(tup5[5])
print(tup5[6])
print(tup5[-3]) #Means tup5[4] -> 7(length of tuple) - 3 = 4 

print("\n")

# Check for item:
# We can check if a given item is present in the tuple. This is done using the in keyword.
if "green" in tup5:
  print("Yes, green is present in this tuple")
else:
  print("No, green is not present in this tuple")

print("\n")

#slicing tuple
#After 'Slicing' python returns a new 'Tuple', so the existing 'Tuple' doesnot change, But a new Tuple is created.
tup6 = tup5[1:4]
print(tup6)

#Note:
# 'Tuples' are immutable.
# 'Strings' are immutable.
# 'Lists' are mutable.
