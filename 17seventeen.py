# Day : 17 For Loop 
# Sometimes a programmer wants to execute a group of statement a certain number of times. This can be done using Loops. Based on this loops are futher classified into following types: for loop, while loop, nested loop.

# for loop can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

# Introduction to Loops
# Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types;

# for loop
# while loop

# The for Loop
# for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

# Example : iterating over a string:

name = 'Karan Veer Pal'
for i in name:
    print(i, end = ", ")

print("\n")

name = 'Karan'
for i in name:
    print(i)
    if(i == "r"):
        print("This is something special.")

print("\n")

# Example: iterating over a list:
        
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

print("\n")

#range() --> what if we do not want to iterate over a sequence? What if want to use for loop for a specific number of times?

# Here, we can use the range() function.

# the range is go for n-1

#Syntax of range() : range(start, stop, step)

for k in range(5):
    print(k)

print("\n")

for k in range(5):
    print(k+1)

print("\n")

for k in range(1,10):
    print(k)

print("\n")

# Quick-Quiz Explore the step parameter in for syntax: 

# syntax of range(start, stop, step)

# step parameter --> An integer number specifying the incrementation. Default by 1.

for g in range(1, 10, 2): # --> Here, a series is print, gap increment by 2 in between the series. 
    print(g)

print("\n")
