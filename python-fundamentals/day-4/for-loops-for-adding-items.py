names = ['Lamin', 'John', 'Beth', 'Ash']

new_names = 'Sarah', 'Alison', 'Melissa'

print(new_names)

for name in new_names:
    names.append(name)
    print(name + ' has been  added to the list')

print('These are the names in the list: \n \t', names)
