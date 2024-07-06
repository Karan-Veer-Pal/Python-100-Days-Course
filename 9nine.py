# Day : 9 Typecasting in Python.

a = "1"
b = "2"
a = 1
b = 2
print(a + b) # Give 12 because both variables are string
print("a:", type(a), "b:", type(b))
print("\n")

# The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

# Two Types of Typecasting:
# Explicit Conversion (Explicit type casting in python)
# Implicit Conversion (Implicit type casting in python).

# Explicit typecasting:
# The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

# It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum1 = number + string_number
print("The Sum of both the numbers is: ", sum1)

c = "2"
d = "4"
print(int(c) + int(d)) # Typecasted
print("a:", type(c), "b:", type(d))
print("\n")

# Implicit type casting:
# Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

# Python converts a smaller data type to a higher data type to prevent data loss.

e = 1.9
f = 8
print(e + f)
print("a:", type(e), "b:", type(f))
print("\n")

num1 = "15"
num2 = 7
str_num = int(num1)
sum2 = str_num + num2
print("The sum two number is:", sum2)
print("num1:", type(num1), "num2:", type(num2))
