#some varibles and objects concepts 

a = 10
b = a
print(id(a))
print(id(b))
a = 20
print(id(a))
print(id(b))


x = [1, 2, 3]
y = x
y.append(4)
print(x)
print(y)

x = [1, 2, 3]
y = x
y = [10, 20]
print(x)
print(y)

# Exercise 1
# Create variables for:
# * Your name
# * Your age
# * Your height
# * Whether you’re a student
# * Your favorite programming language

name = "Jordan"
age = 25
height = 5.9
is_student = True
favorite_language = "Python"   
print(f"""Name: {name}
Age: {age}
Height: {height}
Student: {is_student}
Favorite Language: {favorite_language}""")


#Question 2 — Variable Swapping
#Without using a third variable, swap the values.

a = 5
b = 10
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

#example of variable swapping using tuple unpacking:
a = 1
b = 2
c = 3

a, b, c = c, a, b

print(a, b, c)