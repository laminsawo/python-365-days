
"""
s = format as string
d = format as integer
f = format as floating number

"""

laptop = "Apple"
cost = 1200
exchange_rate = 1.2333322

# {place-holder: format}
# Apple has position of 0, cost has position of 1, and exchange rate has position of 2
print("The price of this {0:s} laptop is £{1:d} and the exchange rate is {2:f}".format(laptop, cost, exchange_rate))
print("The price of this {0:s} laptop is £{1:d} and the exchange rate is {2:.2f}".format(laptop, cost, exchange_rate))
print("The price of this {0:s} laptop is £{1:d} and the exchange rate is {2:4.4f}".format(laptop, cost, exchange_rate))
print("---------------------------------------------------------------------------------------------------------------")

# what happens if you don't specify the format???
# it inherits the type specified when the variable was declared - this is auto detected?
print("The price of this {0:} laptop is £{1:} and the exchange rate is {2:}".format(laptop, cost, exchange_rate))
print("The price of this {0:} laptop is £{1:} and the exchange rate is {2:}".format(laptop, cost, exchange_rate))
print("The price of this {0:} laptop is £{1:} and the exchange rate is {2:}".format(laptop, cost, exchange_rate))
print("--------------------------------------------------------------------------------------------------------------")

# Explicitly specifying the format overrides the default type
# For example, by default cost is an integer value with no decimal points. Now, let format it so it becomes a floating
print("The price of this {0:s} laptop is £{1:.2f} and the exchange rate is {2:.4f}".format(laptop, cost, exchange_rate))

# this example formats cost 1200 to 1200.00 and exchange rate to 4 decimal places
