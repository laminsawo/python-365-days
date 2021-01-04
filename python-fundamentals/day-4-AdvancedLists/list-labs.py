carTypes = ["BMW", "VW", "Bently", "Vauxhall", "Land Rover", "Ferrari", "Lamborghini"]
carTypes.append("Rolls Roys")
for car in carTypes:
    if "BMW" in car:
        print(car, " is a German made car!")
    else:
        print(car, "is not German made")
        print()

print(carTypes)

# making this code interactive
bookTypes = []
getBookTypes = str(input("Enter book type: "))

bookTypes.append(getBookTypes)
print(len(bookTypes))
print(bookTypes)

# reversing numbers in a list
numbers = [1,10,30,5,3,88,2,3,4,5,6,7,8,9,10]
numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

numbers = [1,10,30,5,3,88,2,3,4,5,6,7,8,9,10]
numbers.remove(1)
print(numbers)

#insert a value in a specific location
numbers = [1,2,4,6,7,8,9,10]
#now insert 20 at index 0
numbers.insert(0,20)
print(numbers)

