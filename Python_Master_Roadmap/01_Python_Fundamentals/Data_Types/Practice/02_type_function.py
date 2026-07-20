# Question 1 :
# Create one variable of each of the following data types:
# * Integer
# * Float
# * String
# * Boolean

integer_var = 10
float_var= 3.14
string_var = "hello"
boolean_var = True
print(f"""{type(integer_var)}
{type(float_var)}
{type(string_var)}
{type(boolean_var)}""")

print(f"""{id(integer_var)}
{id(float_var)}
{id(string_var)}
{id(boolean_var)}""")

#mini quiz
#1
a = 10
b = 10
print(id(a))
print(id(b))
print(a is b)

#2
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

#3
a = [1, 2]
b = a

print(a == b)
print(a is b)
b.append(3)
print(a)
print(b)

# Question 2/10 — type() with User Input
# Problem
# Write a program that:
# 1. Takes the user’s:
#     * Name
#     * Age
#     * Height
# 2. Prints the type of each input.

name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to integer
height = float(input("Enter your height: "))  # Convert to float

print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")

#Question 3/10 — isinstance()
# This is a function you’ll use a lot in real-world Python.

a = 10
b = 3.14
c = "Python"
d = [1, 2, 3]
e = True

print(isinstance(a, int))      # True
print(isinstance(b, float))    # True  
print(isinstance(c, str))      # True
print(isinstance(d, list))     # True
print(isinstance(e, bool))     # True

#Question 4/10 
a = 100
b = 100

print(id(a))
print(id(b)) #id(a) and id(b) will be the same because small integers are cached in Python

print(a is b)  # True, because small integers are cached in Python


#Question 5/10
a = 1000
b = 1000

print(a == b) #True, because the values are equal
print(a is b) #False, because larger integers are not cached in Python


#one of the biggest realizations in Python is that everything is an object. This means that every value you create in Python is an instance of a class. The type() function allows you to check the type of an object, and the isinstance() function allows you to check if an object is an instance of a specific class or a subclass thereof.
x = 10
y = "Hello"
z = [1, 2, 3]

print(type(x))
print(type(y))
print(type(z))

print(type(type(x)))


