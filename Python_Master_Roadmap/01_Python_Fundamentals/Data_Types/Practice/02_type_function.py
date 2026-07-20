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