# Day : 20 Functions]

# Python Functions
# A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

# There are two types of functions:

# Built-in functions
# User-defined functions

# Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

# def function_name(parameters):
#   pass
  # Code and Statements

# Create a function using the def keyword, followed by a function name, followed by a paranthesis (()) and a colon(:).
# Any parameters and arguments should be placed within the parentheses.
# Rules to naming function are similar to that of naming variables.
# Any statements and other code within the function should be indented.

# Normal Working -->
# a = 8
# b = 9
# if(a > b):
#   print("a is greater than b")
# else:
#   print("b is greater than a")
# gmean = (a*b)/(a+b)
# print(gmean)


# It is a function: function declaration + function body
# Syntax:
# def function_name(parameters):
#   pass
  # Code and Statements

# Function -->
def calculateGmean(c, d):
  mean = (c*d)/(c+d)
  print(mean)

# Function -->
def isGreater(c, d):
  if(c > d):
    print("c is greater than d")
  else:
     print("d is greater than c")

print("\n")

# only function declaration
def islesser(c, d):
  # means only declare the function and pass the function only
  pass  

print("\n")

# Calling a function:
# We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

# Example:
def name(fname, lname):
    print("Hello,", fname, lname)
name("Sam", "Wilson")

print("\n")

c = 9
d = 7
calculateGmean(c, d) # --> Function Calling
isGreater(c, d) # --> Function Calling
islesser(c, d) # --> Function Calling

print("\n")

# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.
