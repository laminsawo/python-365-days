""""
What is the purpose of 'type casting' in Python programming?
Casting is when you convert a variable value from one type to another

Examples include the following methods: int() or float() or str()
"""
num_in_string = int("100")
int_to_float = float(2)
float_to_int = int(2.5)

print(num_in_string, "converted from string to int")
print(int_to_float, "converted from int to float")
print(float_to_int, "converted from float to int")

print("---------------------------------------------------------------------------------")
# a good you case example of by type casting user input or converting from one type to another for various reasons

print("This is maths drill!!!")
print("Choose operation type: \n 1 = add a and b \n 2 = subtract b from a \n 3 = multiply a by b \n 4 = divide a by b")

operation = int(input("Enter operation value here: "))
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second: "))


if operation == 1:
    value = float(number1 + number2)
    print(number1, "plus", number2, "is equal to", value)
elif operation == 2:
    value = float(number1 - number2)
    print(number1, "minus", number2, "is equal to", value)
elif operation == 3:
    value = number1 * number2
    print(number1, "multiplied by", number2, "is equal to", value)
elif operation == 4 and number2 != 0:
    value = float(number1 / number2)
    print(number1, "divided by", number2, "is equal to", value)
else:
    print("Sorry, you have entered an invalid number")


rate_us = str(input("Are you a happy customer and would return again? Please type yes/no"))
rate_us = rate_us
if rate_us.__contains__("yes"):
    print("We are glad you're an  happy customer. See you soon again")
elif rate_us.__contains__("no"):
    print("We'll try make it up to you next time")
else:
    print("Errrrrrrrrrrrrrrrrr")
