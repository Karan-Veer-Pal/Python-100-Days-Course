# Day : 36 Exception Handling

# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

# Exceptions in Python
# Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

# When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")

# for i in range(1, 11): # This for loop will throw an error if the user enters a string instead of a number. So, after for loop, the remaining lines will not execute. Hence, to save the program from crashing, we use try and except Method
    # print(f"{int(a)} X {i} = {int(a)*i}")
    
# print("Some imp lines of code")
# print("End of program")

# Python try...except
# try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

#Syntax:
#try:
     #statements which could generate 
     #exception
#except:
     #Soloution of generated exception

a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")      
except Exception as e:
  print(e)

print("Some imp lines of code")
print("End of program")

print("\n")

try:
    num = int(input("Enter an integer: "))
    b = [6, 3]
    print(b[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
  print("Index Error")
