# Day : 21 Functions Arguments

# Function Arguments and return statement
# There are four types of arguments that we can provide in a function:

# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments

# Method One:
def average(a, b): 
  print("The average is ", (a+b)/2)
  
average(4, 6) # Function calling

print("\n")

# Method Two:
# Default arguments:
# We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

# def average(a = 9, b = 4): but when we give the argument in function calling time it have the high priority to exucute the function
def avg(d = 9, c = 4):
  print("The average is ", (c+d)/2)
  
avg() # Function calling

print("\n")

# Method Three:
def av(e, f = 4):
  print("The average is ", (e+f)/2)
  
av(4) # Function calling

print("\n")

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)
  
name("Karan") # Function calling

print("\n")

# Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

# average (b = 9, a = 21) --> We can give the argument is any order, means not having a Sequence

# Required arguments:
# In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition. --> Cumplusory to give arguments

def a(x, y, z = 1):
  print("The average is ", (x+y+z)/2)
  
a(4, 6) # Function calling

print("\n")

# Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

# Actually it take a numbers in a tuple
def averg(*numbers): # * means take as tuple agruments
  print(type(numbers)) # use for check the type 
  sum = 0
  for i in numbers:
    sum = sum + i
  print("Average is: ", sum/len(numbers))
  
averg(5,6,8,2,1) # Function calling

print("\n")

# When we want to take a arguments as a dictionary
def name(**name): # ** means take as dictionary agruments
  print(type(name)) # use for check the type
  print("Hello,", name["fname"], name["mname"], name["lname"])
  
name(mname = "Buchanan", lname = "Barnes", fname = "James")

print("\n")

# return Statement
# The return statement is used to return the value of the expression back to the calling function.

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
  
print(name("James", "Buchanan", "Barnes"))