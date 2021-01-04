import datetime
from datetime import date
""""
format strings using the string format() method

"""

name = input('Enter your full name: ').capitalize()
country = input("Enter country of origin: ").capitalize()

year = int(input("Enter year of birth: "))
month = int(input("Enter month of birth: "))
day = int(input("Enter day of the month: "))
date_of_birth = (datetime.date(year, month, day))

date_now = date.today()
#print("Your name is: {0:s}".format(name))
#print("You're from {0:s}".format(country))
#print("Your date of birth is: {0:d}".format(date_of_birth))

# We can  print all of these in a single print statement
print(''' Your name is {0:s} and your country of origin is {1:s}. Your date of birth is {2:} and the date today is 
{3:}
'''.format(name, country, date_of_birth, date_now))


