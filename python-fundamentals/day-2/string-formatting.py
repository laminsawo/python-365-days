"""
This lab demonstrates how to format strings % operator and the format() method
Strings, integers, and floating numbers can all be formatted using both methods
'string-formatting-method.py' shows examples on how to use the format() method
Examples:
    %f - when used gives a floating number with 6 decimal points
    %.2f - This example limits the decimal points to just '2'
    %.x - where x is the number of decimal points required
    %10.2f - this example gives 10 spaces inclusive to before floating number plus with 2 decimal point

    %s - The string format inserts strings in place
    %10s - gives 10 spaces inclusive and then insert string from position
    %.2s - this will truncate a string to just two characters

    %d - formats a number to integer
    %10d -
"""
# cost is in Pound Sterling
#
mobile_phone = {'brand': 'iphone', 'colour': 'black', 'weight': 1.7, 'cost': 1200}
exchange_rate = 1.2  # 1.20 Euro is equal to £1.20 Euro

# get the cost of the phone and covert into an integer
phone_cost = int((mobile_phone['cost']))
print('Print the cost of the phone \n Cost: £ %.2f' % phone_cost)

# Task 1 - calculate how much the phone will cost in Euros
cost_in_euros = phone_cost * exchange_rate
# print cost of phone in Euros
print('An £ %.2f phone will cost %.2f in Euros' % (phone_cost, cost_in_euros))

# Formatting a string - for example, we need to format a users input to a string
age = input("Please enter your age: ")
height = input("What about your height? ")
print('You are %s years old and you\'re %s feet tall' % (age, height))



""" The code below is not directly related to this lab
I only used this verify that i'm using a dictionary - pretty easy :)
"""
print(type(mobile_phone))
