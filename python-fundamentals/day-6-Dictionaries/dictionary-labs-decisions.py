dict1 = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'key': 54}

print(dict1)
print(dict1['one'])
print(dict1['two'])
print(dict1['three'])

# modify a dictionary key value
dict1['key'] = 22
print(dict1, '\n')

# add new a dictionary key and a value
dict1['newKey'] = 66
print(dict1, '\n')


# create a new dictionary without assigning any value
dict2 = {}
dict2['first'] = 1
dict2['second'] = 2
dict2['third'] = 3

print(dict2)
print(dict2['second'], '\n')

# clear all data and keys in a dictionaries
dict3 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'key': 54}
dict3.clear()
print(dict3, ' <-- the contents of the list has been  cleared \n')

# print the keys in dictionary
dict3 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'key': 54}
print(dict3.keys(), '\n')

dict3 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'key': 54}
print(dict3.items(),'\n')

# look for item with using key 'four', delete and print the rest of the
dict3 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'key': 54}
dict3.pop('four')
print(dict3, '\n')

#print the values of keys in a dictionary
dict3 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'key': 54}
print(dict3.values(), '\n')

# update multiple dictionaries to provide a unique key entry as the final result
# example, this removes duplicated kye pair and keep one unique key pair
dict3 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'ten': 10}
dict4 = {'one': 1, 'six': 6, 'seven': 7, 'four': 4, 'eight': 8, 'nine': 9}
dict3.update(dict4)
print(dict3, '\n')

# remove a dictionary key
del dict2['first']
print(dict2,'\n')

# delete the entire dictionary
# printing the dict2 with result in an  error
# del dict2
print(dict2)

dict3 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'ten': 10}
if 'hundred' in dict3:
    print('1')
else:
    print('no match')

while 'eleven' in dict3:
    print(dict3)
    break
