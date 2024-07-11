# Day : 14 If Else Conditional Statements 

# if-else Statements
# Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

# Based on this, the conditional statements are further classified into following types:

# if
# if-else
# if-else-elif
# nested if-else-elif.
# An if……else statement evaluates like this:
# if the expression evaluates True:
# Execute the block of code inside if statement. After execution return to the code out of the if……else block.

# if the expression evaluates False:
# Execute the block of code inside else statement. After execution return to the code out of the if……else block.

# if-else --> Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluate to false, then the program execution follows a different path than it would have if the expression had evaluated to True.


# if-else:
a = int(input("Enter your age:"))
print("Your age is:", a)

if(a >= 18):
    print("Yes")
    print("You are eligible for drive")
else:
    print("No")
    print("You are not eligible for drive")

# Conditional Operator --> <, >, ==, >=, <=, !=. --> return a boolean type answer
print(a > 18)
print(a <= 18)
print(a == 18)
print(a != 18)

print("\n")

applePrice = 210
budget1 = 200
if (applePrice <= budget1):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

print("\n")

# elif:

# elif Statements
# Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

# Working of an elif statement
# Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

# Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

# Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# .
# .
# .
# Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

# Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

bananaPrice = 10
budget2 = 200
if(budget2 - bananaPrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
elif(budget2 - bananaPrice > 70):
    print("Its okay you can buy.")
else:
    print("Alexa, do not add Apples to the cart.")

print("\n")

num = int(input("Enter the value of num: "))
if(num < 0):
    print("Number is Negative.")
elif(num == 0):
    print("Number is Zero.")
elif(num == 786):
    print("Number is Special.")
else:
    print("Number is Positive.")

print("\n")

# Nested if statement
# We can use if, if-else, elif statements inside other if statements as well.

no = 8
if(no < 0):
    print("Number is negative.")
elif(no > 0):
    if(no <= 10):
        print("Number is between 1-10.")
    elif(no > 10 and no <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20.")
else:
    print("Number is zero.")

print("\n")
