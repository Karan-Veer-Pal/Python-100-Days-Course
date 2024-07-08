# Day : 11 String 

# It is a quite special 'Data Type' we can write string by enclosing our name, poem or any text by enclosing it in double quotes ("")


name = "Karan"
friend = "Sarrati"
anotherFriend = 'Lokki'

print("Hello " + name)

# apple = "He said, "I want to eat an apple" --> This will generate the error because we don't use " double quote in between the ""Double Quṣote
# apple = "He said, \"I want to eat an apple" # --> this will also work
apple = 'He said, "I want to eat an apple' # --> this will also work
print(apple)

# Triple Quotes is used to make/print a multiple line prompt 
banana = '''He said, 
Hi Karan
Hey, I am good
"I want to eat an apple'''
print(banana)

# So, in Python 'String' is like an array of charcters
print(name[0]) #--> print a name first letter of name variable
print(name[1])
print(name[2])
print(name[3])
print(name[4])

#Loop: to print a all character of a variable 
print("Lets use a for Loop\n")
for charcter in friend:
    print(charcter)