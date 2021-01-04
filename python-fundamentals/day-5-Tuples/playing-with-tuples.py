
myTuple = ('a', 'b', 'c', 'd', 'e')

print(myTuple)

if myTuple.__contains__('a'):
    print('Tuple has \'a\' as an item')
else:
    print('Item \'a\' does not exist')
# Loop through the Tuple
myTuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z')

# print all the items in the tuple line by line
for item in myTuple:
    if item == 'a' or item == 'c':
        print(item, 'found')
    else:
        print(item, 'not found ... skipping')

myTuple = ('a', 'b', 'c', 'd', 'e')

# ask user to enter any single random letter in the alphabet
letterChoice = str(input('Enter the a random letter in the English alphabet: '))

if myTuple.__contains__(letterChoice):
    print('Congrats!!! \n \t The alphabet \'%s\' is in our list' % letterChoice)
else:
    print('Letter \'%s\' does not exist in our list' % letterChoice)




