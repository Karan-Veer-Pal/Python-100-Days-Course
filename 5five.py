# Day: 5 Comments, Escape Sequence & Print Statement

# Python Comments
# A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

# Single-Line Comments:
# To write a comment just add a ‘#’ at the start of the line.

# Hey, Please Don't remove this line this is a comment
print("I am bad Boy \nYou are a good Boy") # \n Use for new line

# Multi-Line Comments:
# To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

# The use of multiline string.
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

# Escape Sequence Character: Enter, \n, \"\", \'\', etc.

# To insert characters that cannot be directly used in a string, we use an escape sequence character.

# An escape sequence character is a backslash \ followed by the character you want to insert.

# An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:
print("This doesnt "execute")
print("This will \" execute")
      
print("I am \"Bad Boy\" \nYou are a \"Good Boy\"")

# Print 

# More on Print statement
# The syntax of a print statement looks something like this:

# print(object(s), sep=separator, end=end, file=file, flush=flush)
# Other Parameters of Print Statement
# object(s): Any object, and as many as you like. Will be converted to string before printed
# sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
# end='end': Specify what to print at the end. Default is '\n' (line feed)
# file: An object with a write method. Default is sys.stdout
      
print("Hey", 6, 7, sep = "~", end = "009\n") # sep = seperator, ~ Use to join a line or a string, Default sep is spaca
print("Karan", end = "\n") # end use to end the line and execute the next code default value of end is \n
print("Karan")