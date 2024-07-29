# Day : 10 Taking User Input in Python

# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable

# Syntax:
# variable=input()

# print("Enter Your Name:")
a = input("Enter Your Name:")
print("My Name is", a)

# input() function having a rule that is whatever you entered in x variable will be stored as a string.  
x = input("Enter First Number: ")
y = input("Enter Second Number: ")
print("When Input Act like a string:")
print(x + y)
print("When Input Act like a Number:")
print(int(x) + int(y))
