# Day : 9 Typecasting in Python.

a = "1"
b = "2"
a = 1
b = 2
print(a + b) # Give 12 because both variables are string
print("a:", type(a), "b:", type(b))
print("\n")

# Explicit Typecasting:
c = "2"
d = "4"
print(int(c) + int(d)) # Typecasted
print("a:", type(c), "b:", type(d))
print("\n")

# Implicit Typecasting
e = 1.9
f = 8
print(e + f)
print("a:", type(e), "b:", type(f))
print("\n")

num1 = "15"
num2 = 7
str_num = int(num1)
sum = str_num + num2
print("The sum two number is:", sum)
print("num1:", type(num1), "num2:", type(num2))
