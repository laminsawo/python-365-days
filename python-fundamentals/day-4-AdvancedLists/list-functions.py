"""
- This lab demonstrates how to initialise empty lists
- How modify items in a list
- How to add values  to a list
- how to delete values from a list
- how to replace an item in the list


"""
line_break = "\n"
# Task 1: create a list with initial items
users = ["John", 'Alicia', 'Beth', 'Lamin']

# Now lets  print the size or length of the list
# Knowing th length of the list is important because we'll error if we try to add more items beyond what the
# list can accommodate
print(len(users), line_break) # this should be '4', meaning index ranging from 0 to 3

# replacing items at the index position with  new items
users[0] = 'sainey'
users[1] = 'sally'
users[2] = 'bakay'

# index 3 with remain unchanged
print(users, line_break)

# Creating a substrings from a list
users = ["John", 'Alicia', 'Beth', 'Lamin']
users2 = users[:3]
print(users2, line_break)

users3 = users[0:]
users4 = users[:-1] # This one prints all the items except the last item
print(users3, line_break)
print(users4, line_break)

# Task 2: Extending a list  by using the 'append' method

# list
car_types = ['bmw', 'jeep', 'jaguar', 'ferrari']
print(car_types, line_break)

# Now, we have new car types delivered and they need to be added to the existing list of car types
# We can achieve the objective in several ways

# Option 1: appending a list of items to an exiting list
new_car_types = ['mini', 'ford', 'nissan', 'land rover']

# Now lets append the new car types list to current list
#car_types.append(new_car_types)
#print('These is the complete list of car types: \n', car_types)

# Note: Option 1 adds a new list inside our existing list. This is not what I wanted.
#  What I want is to add the items to the exiting list that we have

# Option 2
#car_types.append('mini', 'ford', 'nissan', 'land rover')
#print("A single list of car types after adding new arrivals is: \n ", car_types)
# The  above example will error because the append methods only one item!!

# Option 2.1
car_types.append('mini')
car_types.append('ford')
car_types.append('nissan')
car_types.append('land rover')
print(car_types, line_break)
# Option 2.1 works for us, however using this method might not be very efficient or tidy

# Option 2.2 - Using the 'extend' method - works for only iterable items? Example numbers  in range
# This example below will extend the number range from 1-9 to 1-20 inclusive
numbers = [1,2,3,4,5,6,7,8,9]
print('Initial number range is: ', numbers)
numbers.extend(range(10,21)) # Note 21 will not be printed
print('Extended number range is: ',  numbers)











