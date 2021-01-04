# This lab demonstrates how to creates lists in Python
# The list will be used in ways that relate to real life scenarios
# It will also aim to format, add and remove items from the list

line_break = "\n"
# declare a list that includes the names of users
users = ['lamin', 'sally', 'bakay', 'satou', 'sainey']

# print all the names in the list
print('These are all the items in the list of users %s' % users)
print(line_break)

# print a single name based on its index (e.g. 'lamin' = index 0, 'sally' = index 1)
print('User at index 0 is ' + users[0].capitalize())
print('User at index 1 is ' + users[1].capitalize(), line_break)

# print the last item in the list
print('Last item in the list is ' + users[-1])
print('Second to last item in the list is ' + users[-2], line_break)

# print users from index 2 to the end of the list
print('Users at index 0 to the index 3 %s' % (users[:3]))
print('Users at index 1 to end of the list are ', users[1:] ) # for a multiple names, this method will result in an err

# example below will result in an error because list cannot be concatenated!!
#print('Users at index 1 to end of the list are ' + users[1:3])