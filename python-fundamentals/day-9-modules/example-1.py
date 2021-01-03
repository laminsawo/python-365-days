# Import and use a module
# There are 3 ways to import modules

# Example 1: Import the entire module
import random

# To use this module, we can...
rand_number = random.randrange(1,10)
print(rand_number)

# Note: 'random' is the module and 'randrange' is the function
# This example randomly selects a number between 1 and 10
# We assigned the value of the random number to 'rand_number'
# Then we used the print function to print the number

# Now let's make this a bit more advanced. How about creating a for loop too execute this 100 times
# and also, write the results to a file

count = 100
while count > 0:
    output_file = open('random_numbers.txt', 'a')
    numbers = []

    rand_number = random.randrange(1, 10)
    numbers.append(str(rand_number))  # append each random number to list per iteration

    # now read all the numbers in list individually as strings and append to text file
    for num in numbers:
        output_file.write(num + '\n')
    count -= 1

output_file.close()

# find out how many times a number occurs in the file

input_file = open('random_numbers.txt', 'r')
user_input = '5'  # input('Type in the number you want to search for: ')
count = 0

input_file.readline()
for number in input_file:
    if number.__contains__(user_input):
        count += 1
        print('Number found %s times' % count)

    else:
        print('skipping')

input_file.close()
