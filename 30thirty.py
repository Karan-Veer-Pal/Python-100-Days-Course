# Day : 30 Recursion

# Recursion is the process of defining something in terms of itself.

# factorial(7) = 7*6*5*4*3*2*1
# factorial(0) = 1

# Formula : factorial(n) = n * factorial(n-1)

# Factorial Program :

# Python Recursive Function
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.
    
def factorial(num):
  if(num == 0 or num ==1):
    return 1
  else:
    return num * factorial(num-1)

n = 3
print("Factorial of",n, "is", factorial(n))
p = 4
print("Factorial of",p, "is", factorial(p))
q = 5
print("Factorial of",q, "is", factorial(q))

# Dry Run :
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 * factorial(0)
# 5 * 4 * 3 * 2 * 1 * 1 = Result.

print("\n")

# Fibonacci Series :
# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# Upcoming Result = 0 1 1 2 3 5 8....

# In mathematics, the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted Fn . The sequence commonly starts from 0 and 1, although some authors start the sequence from 1 and 1 or sometimes from 1 and 2. Starting from 0 and 1.

def fibonacci(n):
    if(n < 0):
        print("Invalid Input.")
    elif(n == 0):
        return 0
    elif(n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

r = 4
print("Fibonacci series of",r,"th place is", fibonacci(r))
s = 5
print("Fibonacci series of",s,"th place is", fibonacci(s))
t = 6
print("Fibonacci series of",t,"th place is", fibonacci(t))