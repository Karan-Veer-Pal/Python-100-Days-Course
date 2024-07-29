# Day: 6 Variables and Data Types 

What is a variable?
# Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

# What is a Data Type?
# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:

a = 1
print(a)
print("The type of a is ", type(a))
print("\n")

b = "Karan"
print(b)
print("The type of b is ", type(b))
print("\n")

c = 6.7777
print(c)
print("The type of c is ", type(c))
print("\n")

d = None
print(d)
print("The type of d is ", type(d))
print("\n")

e = True
print(e)
print("The type of e is ", type(e))
print("\n")

f = complex(8, 2)
# print(e)
print("The type of f is ", type(f))
print("\n")

print(a+c)
print("\n")
# print(a+b) Not Worked 

# 1. Numeric data: int, float, complex
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i

# 2. Text data: str
# str: "Hello World!!!", "Python Programming"

# 3. Boolean data:
# Boolean data consists of values True or False.

# 4. Sequenced data: list, tuple
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

# Example:
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print("This is a List:")
print(list1)
print("\n")

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
# Example:
tuple1 = (("parrot", "sparrow", "lion", "tiger"))
print("This is a Tuple:")
print(tuple1)
print("\n")

# Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
# Example:
dict1 = {"name" : "karan", "age" : 20, "canVote" : True}
print("This is a Dictionary:")
print(dict1)
print("\n")
