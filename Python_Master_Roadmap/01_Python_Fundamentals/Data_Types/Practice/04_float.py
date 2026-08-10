import math

x = 10.5
print(type(x)) # Output: <class 'float'>

print(10/2) # Output: 5.0, division always returns a float
print(10//2) # Output: 5, floor division returns an integer if both operands are integers
print(10.0//3) # Output: 3.0, floor division returns a float if any operand is a float

a = 5.5
b = 2.0

print(a + b) # Output: 7.5, addition of two floats
print(a - b) # Output: 3.5, subtraction of two floats
print(a * b) # Output: 11.0, multiplication of two floats
print(a / b) # Output: 2.75, division of two floats 
print(a ** b) # Output: 30.25, exponentiation of two floats

print(0.1 + 0.2) # Output: 0.30000000000000004, floating-point arithmetic can lead to precision issues

inf = float('inf') # Positive infinity
neg_inf = float('-inf') # Negative infinity

num=[10.5,20.2,30.7]
avg = sum(num)/len(num)
print(avg) # Output: 20.466666666666665, average of a list of floats
print(f"Average: {avg:.2f}") # Output: Average: 20.47, using f-string formatting to display the average with 2 decimal places
print(f"Rounded: {round(avg)}")
print(f"0.1 + 0.2: {0.1 + 0.2}")
print(math.isclose(0.1 + 0.2, 0.3)) # Output: True, using math.isclose() to compare floating-point numbers for equality



#challenge :
# Input:
# 0.1 0.2

# Output:
# Sum: ...
# Rounded: ...
# Exact equality: ...
# Close enough: ...

sum_result = 0.1 + 0.2
rounded_result = round(sum_result) #round helps to round the floating-point number to the nearest integer
exact_equality = sum_result == 0.3
close_enough = math.isclose(sum_result, 0.3) #isclose() helps to compare floating-point numbers for equality, taking into account the precision issues that can arise with floating-point arithmetic

round(3.14159, 2) # Output: 3.14, rounding to 2 decimal places
#if there is no second argument, it rounds to the nearest integer
#example 
round(3.7) # Output: 4, rounding to the nearest integer
round(3.2) # Output: 3, rounding to the nearest integer
round(3.4) # Output: 3, rounding to the nearest integer
round(3.5) # Output: 4, rounding to the nearest integer

#round in negative numbers
round(-3.7) # Output: -4, rounding to the nearest integer
round(-3.2) # Output: -3, rounding to the nearest integer  
round(1234, -2) # Output: 1200, rounding to the nearest hundred
#this happend because the second argument of round() specifies the number of decimal places to round to. When it is negative, it rounds to the left of the decimal point. In this case, -2 means rounding to the nearest hundred.
round(1234, -1) # Output: 1230, rounding to the nearest ten
round(1234, -3) # Output: 1000, rounding to the nearest thousand 
#here negative values of the second argument in round() indicate rounding to the left of the decimal point, while positive values indicate rounding to the right of the decimal point. For example, round(1234, -2) rounds to the nearest hundred, round(1234, -1) rounds to the nearest ten, and round(1234, -3) rounds to the nearest thousand.

#Python’s rounding has a weird-looking case
#example :
round(2.5) # Output: 2, rounding to the nearest integer
round(3.5) # Output: 4, rounding to the nearest integer
#this happens because Python uses a rounding method called "round half to even" or "bankers' rounding". In this method, when a number is exactly halfway between two integers, it rounds to the nearest even integer. So, 2.5 rounds down to 2 (even), while 3.5 rounds up to 4 (even). This method helps to reduce bias in rounding when dealing with large datasets.

# 2.5 → 2
# 3.5 → 4
# 4.5 → 4
# 5.5 → 6

a = 0.3
b = 0.3000000001
close_enough = math.isclose(a, b) #output: True, using math.isclose() to compare floating-point numbers for equality, taking into account the precision issues that can arise with floating-point arithmetic
abs(a - b) < 1e-9 #output: True, using absolute difference to compare floating-point numbers for equality

# challenge:
# Write a program that takes:
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"diff:{abs(a-b)}")#output: diff: 0.0000000001, using absolute difference to compare floating-point numbers for equality  
print(f"exactly_equal:{a==b}")#output: exactly_equal: False, using == operator to compare floating-point numbers for equality
print(f"close_enough:{math.isclose(a,b)}")#output: close_enough: True, using math.isclose() to compare floating-point numbers for equality, taking into account the precision issues that can arise with floating-point arithmetic
