# Day : 35 For Loop with Else

# As you have learned before, the else clause is used along with the if statement.

# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

# Syntax: 
#for counter in sequence:
  #Statements inside for loop block
#else:
  #Statements inside else block 

for x in range(5):
  print ("iteration no {} in for loop".format(x+1))
else:
  print ("else block in loop")
print ("Out of loop")

print("\n")

for i in range(5):
  print(i)
else:
  print("Sorry no i here.")

print("\n")

for i in []: # [] -> Empty List
  print(i)
else:
  print("Sorry no i here")

print("\n")

#In this case, the else block will not be executed because the loop is terminated by the break statement.
for i in range(6):
  print(i)
  if i == 4:
    break
else:
  print("Sorry no i here")

print("\n")

i = 0
while i < 7:
  print(i)
  i = i + 1
  if i == 4:
    break
else:
  print("Sorry no i here")

print("\n")
