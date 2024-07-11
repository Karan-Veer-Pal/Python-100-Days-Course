# Day : 14 If Else Conditional Statements 

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

# elif:
applePrice = 10
budget = 200
if(budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
elif(budget - applePrice > 70):
    print("Its okay you can buy.")
else:
    print("Alexa, do not add Apples to the cart.")

num = int(input("Enter the value of num: "))
if(num < 0):
    print("Number is Negative.")
elif(num == 0):
    print("Number is Zero.")
elif(num == 786):
    print("Number is Special.")
else:
    print("Number is Positive.")


# Nested if statement
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
    