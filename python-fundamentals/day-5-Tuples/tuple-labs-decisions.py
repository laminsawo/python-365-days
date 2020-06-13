# manipulating tuples

tup1 = (1, 'cat', 'dog', 5, 'horse', 'rabbit')
tup2 = (2,6,9,0,3)
print(len(tup1))
print(tup1 * 3)
print(tup1 + tup2)

#delete a value in a tuple
if 'cat' in tup1:
    print("Yes")
else:
    print('no')

# delete the whole tuple
#del tup1
#print(tup1, " This is not defined since it has been deleted")

isCat = 'cat'
if tup1.__contains__(isCat):
    print(isCat)
else:
    print('nothing')

