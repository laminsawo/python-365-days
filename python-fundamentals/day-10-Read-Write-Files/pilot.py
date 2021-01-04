# create a new file and open in append mode
names = open('names.tx', 'a')

# add some data to the file
names.write("Lamin" + '\n')

# Now, let's open the file in read mode and read the content(s)
names_input = open('names.tx', 'r')
names = names_input.readline(8)
print(names)
#for name in names:
#    print(name)

# Now, close the file
names_input.close()
