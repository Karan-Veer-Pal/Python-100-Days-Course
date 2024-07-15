# Day : 18 While Loop

# Day : 18 While Loop

# Python while Loop
# As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

# for loop
print("For Loop:")
for i in range(3):
  print(i)

print("\n")

# while loop

print("While Loop")
i = 0
while(i <= 3):
  print(i)
  i = i + 1

i = int(input("Enter the number: "))
while(i <= 3):
  i = int(input("Enter the number: "))
  print(i)
  i = i + 1

print("Done with while loop.")

print("\n")

# Decrementing while loop

# Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable count, in our case) or the loop will continue forever.

print("Decrementing While Loop")
count = 5
while (count > 0):
  print(count)
  count = count - 1

print("\n")

# while + else -->

# Else with While Loop
# We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

# when while condition is false then else is run
print("While + Else")
x = -5
while (x > 0):
  print(x)
  x = x - 1
else:
  print("I am Inside else")
  print('counter is 0')

print("\n")

i = 0
while True:
  print(i)
  i = i + 1
  if(i % 10 == 0): # means when i is 10 then break executing
    break

print("\n")

# Do-While loop in python
# do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an exit-controlled loop.

# How to emulate do while loop in python?
# To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

# The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break


# Syntax:
# do{
#   loop body
# }while(condition)

# do-while loop in which code is run at least one time and further depend on the condition for code running


# Explanation
# This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.
