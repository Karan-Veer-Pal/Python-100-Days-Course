# Day : 18 While Loop

# Day : 18 While Loop

# Python while Loop
# As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

# for loop
# for i in range(3):
#   print(i)

# print("\n")

# while loop

# i = 0
# while(i <= 3):
#   print(i)
#   i = i + 1

# i = int(input("Enter the number: "))
# while(i <= 38):
#   i = int(input("Enter the number: "))
#   print(i)
#   i = i + 1

# print("Done with while loop.")

# Decrementing while loop

# Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.

# count = 5
# while (count > 0):
#   print(count)
#   count = count - 1

# while + else -->

# when while condition is false then else is run
# x = -5
# while (x > 0):
#   print(x)
#   x = x - 1
# else:
#   print("I am Inside else")
#   print('counter is 0')

# Do-While loop in python
# do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

# Syntax:
# do{
#   loop body
# }while(condition)

# do-while loop in which code is run at least one time and further depend on the condition for code running
i = 0
while True:
  print(i)
  i = i + 1
  if(i % 10 == 0): # means when i is 10 then break executing
    break