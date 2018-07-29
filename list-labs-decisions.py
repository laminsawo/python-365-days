# Make names or numbers to the list
pupilsLits = []
print("Add items to the list")
addItem = input("Would you like to add an item (YES/NO: ").upper()

while addItem != 'NO':
    addValue = input("Please type value: ")
    pupilsLits.append(addValue)
    addItem = input("Would you like to add an item (YES/NO: ").upper()

print(pupilsLits)
print('Nothing to add. Bye!')

