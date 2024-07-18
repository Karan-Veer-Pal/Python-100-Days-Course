# Day : 19 Break and Continue  

# break statement
# The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

# --> break statement tells that stop the execution of code in a loop

for i in range(12):
  if(i == 10):
    break
  print("5 X", i + 1, "=", 5*(i+1))

print("Left the loop here! \n")

# Continue Statement
# The continue statement skips the rest of the loop statements and causes the next iteration to occur.

# --> continue means left the iteration and go to execute next further code 

for i in range(12):
  if(i == 6):
    print("Skip the iteration!")
    continue
  print("6 X", i + 1, "=", 6*(i+1))

