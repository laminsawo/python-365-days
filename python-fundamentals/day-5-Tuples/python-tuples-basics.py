# A tuple operates like a list but it's initial values can't be modified
# Tuples are declared using the ()
# Use case examples of using Tuple - Dates of the week,  Months of the Year, Hours of  the clock

# we can create a tuple like this...
monthsOfTheYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# Prints all the items in the tuple
print(monthsOfTheYear)

# prints an item  in the tuple
print(monthsOfTheYear[0])

print(monthsOfTheYear[:3])

# If we try to run the code below it will error
# This is because we are change a value in the tuple, which is not allowed!
# monthsOfTheYear[0] = "January"

# Other operations we can do with tuples

# find an item in the tuple
myTuple = ('Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun')

print(len(myTuple))

print(sorted(myTuple))

names = ['John', 'Lamin', 'Vicky', 'Jasmine']
print(names * 3)