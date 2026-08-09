print(-17//5)  # Output: -4
print(-17%5)   # Output: 3

n = 1234
last_digit = n % 10
n = n // 10
print(last_digit)  # Output: 4

last_digit = n % 10
n = n // 10
print(last_digit)  # Output: 3  


q, r = divmod(17, 5)
print(q)  # Output: 3
print(r)  # Output: 2

print(divmod(-17, 5))  # Output: (-4, 3)
print(divmod(17, -5))  # Output: (-4, -3)

print(2**3)  # Output: 8
print(2**-1)  # Output: 0.5

print(2**3.0)  # Output: 8.0
print(2**-1.0)  # Output: 0.5, 1/2=0.5
print(9**0.5)  # Output: 3.0 , backward compatibility with math.sqrt(9)


pow(2, 3)  # Output: 8
# this is equivalent to 2**3


pow(2, 5, 7)
print(pow(2, 5, 7))  # Output: 4, equivalent to (2**5) % 7

abs(-5)  # Output: 5
abs(5)  # Output: 5
diff = abs(-5) - abs(5)
print(diff)  # Output: 0

#abs function can be used to find the absolute value of a number. It returns the non-negative value of the number, regardless of its sign. For example, abs(-5) returns 5, and abs(5) also returns 5. The difference between the absolute values of -5 and 5 is 0, as shown in the code above.

a = 10
b = 15
diff = abs(a-b) - abs(b-a)
print(diff)  # Output: 0

diff= abs(a-b)
print(diff)  # Output: 5


# //       floor division
# %        remainder
# **       power
# divmod() quotient + remainder
# pow()    power / modular power
# abs()    absolute value


print(2+3*4)  # Output: 14, multiplication has higher precedence than addition
print((2+3)*4)  # Output: 20, parentheses change the order

#power operator has higher precedence than multiplication and division, which in turn have higher precedence than addition and subtraction. Parentheses can be used to change the order of operations.
print(2 * 3 ** 2 ) # Output: 18, exponentiation is performed first, then multiplication

print(20//3*2)  # Output: 12, floor division is performed first, then multiplication

print(20%6+2)  # Output: 4, modulus is performed first, then addition
print(20%(6+2))  # Output: 4, parentheses change the order
print(20//3*2)  # Output: 12, floor division is performed first, then multiplication
print(20 - 5 + 3)  # Output: 18, subtraction is performed first, then addition
print(20 - (5 + 3))  # Output: 12, parentheses change the order

x = 17 // 5 + 17 % 5
print(x)  # Output: 6, floor division is performed first, then modulus, and finally addition

result = 2 + 3 * 4 ** 2 // 5
print(result)  # Output: 10, exponentiation is performed first, then multiplication, floor division, and finally addition

#  Parentheses
#     ↓
#   Power
#     ↓
#  × ÷ // %
#     ↓
#    + -

print(10 + 6 // 2 * 3 ** 2)  # Output: 37
# The order of operations is as follows:
# 1. Exponentiation: 3 ** 2 = 9
# 2. Floor division: 6 // 2 = 3
# 3. Multiplication: 3 * 9 = 27
# 4. Addition: 10 + 27 = 37 

result = (20 - 3) ** 2 // 5 * 2 + 17 % 6
print(result)  # Output: 119
# The order of operations is as follows:
# 1. Parentheses: (20 - 3) = 17
# 2. Exponentiation: 17 ** 2 = 289
# 3. Floor division: 289 // 5 = 57
# 4. Multiplication: 57 * 2 = 114
# 5. Modulus: 17 % 6 = 5
# 6. Addition: 114 + 5 = 119

#challenge question

# Write a Python program that takes an integer n and prints:

# 1. The last digit
# 2. The remaining number after removing the last digit
# 3. The quotient and remainder when n is divided by 7
# 4. n²
# 5. The absolute difference between n and 100

n=int(input("Enter an integer: "))
print("last digits:",n%10)
print("remaining number:",n//10)
q,r=divmod(n,7)
print("quotient:",q)
print("remainder:",r)
print("n squared:",n**2)
print("absolute difference with 100:",abs(n-100))


