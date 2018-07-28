# Lists fundamentals - adding, appending, etc.

names = ["lamin", "sally", "bakay", "sainey", "emily", "sandra", "satou", "binta", "jankey"]

#print all names in list
print(names)
print(names[0])
print(names[-1])
print(names[1:3])

#add new names to list
names.append("james ")
names.append("Ellie")

#now print the complete list (after append)
print(names)

#-------UPDATING THE LIST -----#
#
# replace -1 (Ellie) with 'Laura'
names[-1] = "laura"
print(names)

#delete items in list
del names[4:6]
print(names)
print(names[4:6],"...deleted from list")
print(names)