# Day : 16 Match Case Statement 

# not use break-keyword in this language

# to check which version is used 
# import os
# print("Hello World ...")
# os.system("python --version")

# Match Statement

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 :
        print("case is 4")
    # use _ for default
    case _ if x != 90:
        print(x, "is not 90")
    case _ if x != 90:
        print(x, "is not 80")
    case _:
        print(x)

# x = 4
# # x is the variable to match
# match x:
#     #if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4 if x % 2 == 0:
#         print("x % 2 == 0 and case is 4")
#     # Empty case with if-condition
#         case _ if x < 10:
#         print("x is < 10")
#         # default case(will only be matched if the above cases were not matched)
#         # so it is basically just an else:
#         case _:
#         print(x)