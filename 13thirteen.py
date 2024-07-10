# Day : 13 String Method (Operation)

# --> String are immutable
name = "Karan"
print(len(name))
print(name.upper()) # --> name.upper() return a new string, turns all letter of the string in a Upper case, it is not change a name string, it make a copy of the name string as a new string

print(name.lower()) # --> turn all letter in lower case as a new strig

# rstrip() removes any trailing characters
str1 = "Hello !!!"
print(name.rstrip("!")) # return Hello !!! Karan
str2 = "!!! Hello !!!"
print(name.rstrip("!")) #but in leading it can't be strip

# replace() method replaces all occurences of a string with another string
st = "Silver Spoon Spring Sprint"
print(st.replace("Sp", "M"))

# split() method splits the given string at the specified instance and returns the separated
print(str1.split(" "))

# capatalize() 
blogHeading = "introduction tO Chess"
print(blogHeading.capitalize()) # to convert capital First letter in a string, only the first character of the string to uppercase and the rest other characters of the string are truned to lowercase. The string has no effect if the first character is  already uppercase.

# center() method aligns the string to the center as per the parameters given by the user.
string = "Welcome to the Console!!!"
print(len(string))
print(len(string.center(100))) #100 means shift 100 to the left of the monitor

# count() method returns the number of times the given value has occurred the given string
countstring = string.count("o")
print(countstring)

# endswith() method checks if the string ends with a given value. If yes then return True, else return False
print(string.endswith("!!!"))

# find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent form the string then return -1.
s = "He's name is Dan. He is an honest man."
print(s.find("is")) # return first occurence of is
print(s.find("ishh")) # return -1 because of ishh is not present in the string 

# isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or puntuation are present, then it returns False.
stir = "WelcomeToTheConsole"
print(stir.isalnum())

# isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or puntuation or number(0-9) are present, then it returns False.
print(stir.isalpha())

# islower() method returns True if all the characters in the string are lower case, else it returns False
print(stir.islower())

# isprintable() method returns True if all the values within the given string are printable, if not, then return False
strin = "We wish you a very Happy Chrismas\n"
print(strin.isprintable())

# isspace() method returns True only and only if the string contains white spaces else returns False.
b = "           " #using spacebar
print(b.isspace())
c = "       " #using Tab
print(c.isspace())

# istitle() method returns True if the first letter of each word of the string is capitalized, else it returns False
d = "World Health Organization"
print(d.istitle())

# isupper() method returns True if all the characters in the string are upper case, else it returns False
e = "WORLD HEALTH ORGANIZATION"
print(e.isupper())

# stratswith() method checks if the string starts with a given values. If yes then return True, else return False.
f = "Python is a Interpreted Language"
print(f.startswith("Python"))

# swapcase() method changes the characters casing of the string. Upper case ase converted to lower case and lower case to uppercase.
print(f.swapcase())

# title() method capitalizes each letter of the word within the string.
print(f.title())