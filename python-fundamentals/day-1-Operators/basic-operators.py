# This Python file exhibits basic Python Maths operators
"""
Operators and usage:
+ = addition of numbers
* = multiplication of numbers
- = subtraction of numbers
/ = division of numbers
"""
# Examples:
#x = 50
#y = 10

# Improvements: Make the variables dynamic in the sense that the user gets asked to input values for x and y
# Comment out the example static variables
x = int(input("Enter value for X: "))
y = int(input("Enter value for Y: "))

# adding the numbers
a = x + y
print(" %d plus %d is %d" %(x, y, a))

# subtracting the numbers
a = x - y
print(" %d minus %d is %d" %(x, y, a))

# multiplying the numbers
a = x * y
print(" %d multiplied by %d is %d" %(x, y, a))

a = x / y
print(" %d divided by %d is %d" %(x, y, a))
