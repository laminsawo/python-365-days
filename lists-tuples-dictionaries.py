# # Lists fundamentals - adding, appending, etc.
#
# names = ["lamin", "sally", "bakay", "sainey", "emily", "sandra", "satou", "binta", "jankey"]
#
# #print all names in list
# print(names)
# print(names[0])
# print(names[-1])
# print(names[1:3])
#
# #add new names to list
# names.append("james ")
# names.append("Ellie")
#
# #now print the complete list (after append)
# print(names)
#
# #-------UPDATING THE LIST -----#
# #
# # replace -1 (Ellie) with 'Laura'
# names[-1] = "laura"
# print(names)
#
# #delete items in list
# del names[4:6]
# print(names)
# print(names[4:6],"...deleted from list")
# print(names)

#--------------Tuples ------------------------------------#

monthsOfTheYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",  "Nov", "Dec")
print(monthsOfTheYear)

#print last month of the year
print(monthsOfTheYear[-1])

#find out if an item is in a tuple
print ("Dec" in monthsOfTheYear)

#length of a tuple
monthsOfTheYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",  "Nov", "Dec")
print(len(monthsOfTheYear))
#deletting a typle
#del monthsOfTheYear
#print(monthsOfTheYear)


#----------------Dictionaries--------------------------#
# {} are used instead of [] for list abd () for tuples
#example
luckyNumbers = {"Lamin":77, "Amy":74, "Sandra":77, "Sally":99, "Satou":7}
print(luckyNumbers["Lamin"])
# or use the dictionary method
# using this methods does not require quotation marks to be put arrount dictionary keys
#example () are used instead
luckyNumbers = dict(Lamin = 77, Amy = 74, Sandra = 78, Sally = 99, Satou =100)

#modify items in a dictionary
luckyNumbers["Amy"] = 88
luckyNumbers["Stranger"] = 200
print(luckyNumbers)

#creating a dictionary to add values later
luckyNumbers = {}
luckyNumbers["Lamin"] = 100
luckyNumbers["Sally"] = 200
luckyNumbers["Satou"] = 300
print(luckyNumbers)

#delete/remove items in a dictionary
#del luckyNumbers
#print(luckyNumbers)

del luckyNumbers["Lamin"]
print(luckyNumbers)

