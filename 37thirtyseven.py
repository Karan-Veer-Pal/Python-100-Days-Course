# Day : 37 Finally Keyword 

# Finally Clause
# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

try:
    k = [1, 5, 6, 7]
    j = int(input("Enter the index: "))
    print(k[j])
except:
    print("Some error occurred")
finally:
    print("I am always executed")

print("\n")

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")

print("\n")

# When you wrap the same thing in a function, the finally block will always be executed, as it is the last part of the function.

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0  
  finally:
    print("I am always executed")


x = func1()
print(x)

# After try or except part executed, when ran a line return 0 or 1, but in programming return means stop the execution of the other part of the program but here, finally part is run after try or except part be executed. this is the difference.
