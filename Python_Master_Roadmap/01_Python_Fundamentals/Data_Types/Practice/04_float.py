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



