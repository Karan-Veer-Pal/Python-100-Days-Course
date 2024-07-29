# Day : 12 String Slicing and Operation on Strings 
# Slicing means print a string as per user requirement by using index number [0:5] --> 0 to 4 print

# String Slicing & Operations on String
# Length of a String
# We can find the length of a string using len() function.

names = "Karan,Veer"
print(names[0:7]) # [0:5] --> Means where to where you want to print a string, this is known as slicing, ,this will return a Karan,V
print(len(names)) # --> this will return a 10

# String as an array
# A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

# Eg. --> To finding a length of a string
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.") # --> this will return a Mango is a 5 letter word.
# Slicing -->
print(fruit[0:4]) # --> Including a 0 but not 4, this will return a Mang
print(fruit[1:4]) # --> Including a 1 but not 4, this will return a ang
print(fruit[:3]) # --> automatically take a starting string index, this will return a Man
print(fruit[:]) # --> Automatically a take a length of the string, this will return a Mango
print(fruit[0:-3]) # --> it is a negative slicing, in this python interpreter automatically take a print(fruit[0:len(fruit)-3]), this wil print a only 2 element of a string 5 - 3 = 2, this will return a Ma 
print(fruit[-1:-3]) # --> this will return a 5 
print(fruit[-3:-1]) # --> this will return a ng, 5-3:5-1 = 2:4

# Loop through a String:

# Loop through a String:
# Strings are arrays and arrays are iterable. Thus we can loop through strings.

alphabets = "ABCDE"
for i in alphabets:
    print(i)# --> this will return a A, B, C, D, E  
