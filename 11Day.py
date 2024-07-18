# Day : 11 String 

# What are strings?
# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

# It is a quite special 'Data Type' we can write string by enclosing our name, poem or any text by enclosing it in double quotes ("")

name = "Karan"
friend = "Sarrati"
anotherFriend = 'Lokki'

print("Hello " + name)

print("\n")

# apple = "He said, "I want to eat an apple" --> This will generate the error because we don't use " double quote in between the ""Double Quṣote
# apple = "He said, \"I want to eat an apple" # --> this will also work
apple = 'He said, "I want to eat an apple' # --> this will also work
print(apple)

# Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

# Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

# How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience

print("\n")

# Multiline Strings
# If our string has multiple lines, we can create them like this:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("\n")

# Triple Quotes is used to make/print a multiple line prompt 
banana = '''He said, 
Hi Karan
Hey, I am good
"I want to eat an apple'''
print(banana)

print("\n")

# Accessing Characters of a String
# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string.

# So, in Python 'String' is like an array of charcters
print(name[0]) #--> print a name first letter of name variable
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print("\n")

# Looping through the string
# We can loop through strings using a for loop like this:
# Loop: to print a all character of a variable 
print("Lets use a for Loop\n")
for charcter in friend:
    print(charcter)

print("\n")
