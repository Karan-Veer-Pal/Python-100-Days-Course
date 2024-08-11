# Day : 44 How import works 

# How importing in python works
# Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

# To import a module in Python, you use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:

# Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation. For example, to use the sqrt function from the math module, you would write:

import math 
math.floor(4.2343)
result = math.sqrt(9)
print(result)

print("\n")

# If we want to import only one function from a module, we can do this by using "from" keyword
# from keyword
# You can also import specific functions or variables from a module using the from keyword. For example, to import only the sqrt function from the math module, you would write:
from math import sqrt
result = sqrt(9) # In which, we can't call a function math. , we can directly call function like sqrt()
print(result)

print("\n")

# from math import * -> Not recommdable because * import all the function of math simultaneously,,,, importing everything
# It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
# Python also allows you to rename imported modules using the as keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.

# "as" keyword : It is used to give a short name to a module or function by using as, when we write a code
# You can also import multiple functions or variables at once by separating them with a comma:
from math import pi, sqrt as s
result = s(9) * pi
print(result)

print("\n")

#                          OR

import math as m
result = m.sqrt(9) * m.pi
print(result)

print("\n")

# The dir function
# Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.
# The dir function : It is used to print all the function and variable of the module.
import math
print(dir(math))
print(math.nan, type(math.nan))

# This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.

# In summary, the import statement in Python allows you to access the functions and variables defined in a module from within your current script. You can import the entire module, specific functions or variables, or use the * wildcard to import everything. You can also use the as keyword to rename a module, and the dir function to view the contents of a module.

print("\n")

# Make another file 44anotherfile.py

from anotherfile import welcome, karan
#                    OR
# from karan import * 

welcome()
print(karan)

print("\n")

# from 44anotherfile import * as s -->> Not Worked

# from anotherfile as hr
# print(hr.welcome())
# print(hr.karan)


print("\n")
