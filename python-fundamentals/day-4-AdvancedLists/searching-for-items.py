items = [1, 2, 3, 4, 'red', 'blue', 'green']

if items.__contains__(1):
    print("Items list contains \'1\'")
else:
    print("Items list does now contain the number '1'")

# Now, let's make this program more dynamic

lookup = input("Enter the item you're looking for: ")

if items.__contains__(lookup):
    print("The item %s is found in the inventory" % lookup)
else:
    print("The item %s is not found in the inventory" % lookup)

# we could use a simple if statement like this ..