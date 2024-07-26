# Day : 28 f-strings

# String formatting in python
# String formatting can be done in python using the format method.

# Normal Way:

name = "Karan"
country = "India"

Quote = "Hey! My name is {} and I am from {}"
print(Quote.format(name, country))

print("\n")

Quote = "Hey! My name is {} and I am from {}"
print(Quote.format(country, name))

print("\n")

Quote = "Hey! My name is {1} and I am from {0}"
print(Quote.format(country, name))

print("\n")

# In this method, we can write more code or want to know the working of the this, it is the problem, so we can solve this problem by using f-strings.

# f-strings in python
# It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

#f-string means that you can now put variables inside your string.
print(f"Hey! My name is {name} and I am from {country}")

print("\n")

# Normally:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.09999))

print("\n")

# Using f-string:
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

print("\n")

# f-string introduce in python 3.6 onwards.

print(f"{2 * 30}") # return string data type
print(type(f"{2 * 30}"))

print("\n")

# To print as it is string:
print(f"We use f-strings like this: Hey! My name is {{name}} and I am from {{country}}")

print("\n")

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")