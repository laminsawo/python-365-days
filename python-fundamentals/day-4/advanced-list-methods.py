"""
List formatting
append - append a single item to an existing list
clear - clear an item from the list
pop - print
reverse - format list in reverse order?
insert - ?
del - delete an item from a list
extend - iterable: extend a list with an iterable list of items e.g. numbers in range of 1 to 30 (index 0 - 30)
"""

names = ['John', 'Lamin', 'Vicky', 'Jasmine']
print('Just four names in the list: ', names)

names.append('Beth')
print('Beth has been appended to the list of names', names)

# what is length of the list??
print('Length of appended list is \'', len(names), '\'')

# Using the 'pop' method - This method takes only one argument
# Purpose: Print 'value' in the list using its index number as a reference point
# if no argument is passed,  the default index is '-1'
print('Item at index 0 is: ', names.pop(0))
print('Item at last index in the list is: ', names.pop(-1))

# Index 3 and 4 cannot be printed using pop
# Error code = ' IndexError: pop index out of range'
# Diagnosis: occurs due to the appending of the list
#print('Item at index 3 is: ', names.pop(3))

# This error does not occur using the non appended list
names = ['John', 'Lamin', 'Vicky', 'Jasmine']
print(names.pop(3))

# Using the 'clear' method to clear all items from the list
names = ['John', 'Lamin', 'Vicky', 'Jasmine']
names.clear()
print(names)

# Using the 'del' method to delete single or a range of items in a list
# Example 1 - Delete a single item in the list
names = ['John', 'Lamin', 'Vicky', 'Jasmine']
del names[0]
print(names)

# Example 2 - Delete multiple items
names = ['John', 'Lamin', 'Vicky', 'Jasmine']
del names[:2]
print(names)

# Example 3 - Delete all items
names = ['John', 'Lamin', 'Vicky', 'Jasmine']
del names[:]
print(names)

# Using the 'reverse' method
# when printed, this will result in Jasmine', 'Vicky', 'Lamin', 'John'
names = ['John', 'Lamin', 'Vicky', 'Jasmine']
names.reverse()
print(names)


# Using the 'insert method'
# Note: This method takes exactly two arguments
# first argument references the index we want to insert the new item
# second argument is the actual value or object (e.g. a string or a number)
names = ['John', 'Lamin', 'Vicky', 'Jasmine']
names.insert(0, 'Frankie')

# The above example inserts  Frankie at index 0, 'John' now becomes index 1, 'Lamin' becomes 2, and etc..
print(names)

# This example sorts the items in the list
names = ['John', 'Lamin', 'Vicky', 'Jasmine']
# names.sort()
print(names.sort())

names = ['John', 'Lamin', 'Vicky', 'Jasmine']
print(sorted(names))

# duplicate the list
print(names * 3)









