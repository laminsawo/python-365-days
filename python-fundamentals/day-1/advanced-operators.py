# This Python file exhibits Advanced Python Maths operators
"""
Operators and usage:
// = Floor division - This rounds down the answer to the nearest whole number when two numbers are divided
% = Modulus - This gives the remainder when two numbers are divided e.g. 5 % 2 = 1
** = Exponent - gives the result of powers e.g. 2**2 = 4 and 2**8 = 256
"""
x = 25
y = 10

# Floor division in action - expected result is 2
a = x//y
print("A floor division of %d by %d is equal to %d" %(x,y,a))

# Modulus operator in action
# Expected result is 5
a = x%y
print("A modulus of %d by %d is equal to %a" %(x,y,a))

# Exponential operator in action
# Example, let's find out what is 2 ** 8?
# This should return 256
x = 2
y = 8
a = x**y

print("%d ** %d is equal to %d" %(x,y,a))

