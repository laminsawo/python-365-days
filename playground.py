# name = input('Enter your full name: ').title()
# print(name)
#
# name = "Lamin Sawo Jadama".swapcase()
# print(name)
line = '#-------------------------------------------------------#'
names = ['lamin','sally','bakay']
print(names[0])
print(names[-1])
print(line)

days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
print('First day of the week is %s' %days[0])
print(line)

# filtering weekdays from weekend days
days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
for day in days:
    if day.startswith('S'):
        print('These are weekend days', day)
    else:
        print('These are week days', day)
print(line)

# working with dictionaries
person = {'name': 'lamin', 'surname': 'sawo', 'age': 27, 'height': 1.78, 'weight': 70, 'build': 'slim'}

print(person.values())  # prints the values of the dictionary keys
#  print('This is popped', person.pop('name'))  # prints the value of name and removes it from the dict
print(person.keys())  # because name was popped, it won't be in dictionary anymore

# Assigning new key value pairs and changing the value of existing keys
# Example 1: add a new key value pair

person['name'] = 'sally'
print(person['name'])
print(person)  # new name 'sally' will replace 'lamin'

# item() allows for the
for x, y in person.items():
    print(x.upper(), ':', y)

names = []
names.append("Lamin")
names.append("Sally")
print(names)
