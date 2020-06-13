# Creating a dictionary using the dictionary 'dict()' method
# With this,  we don't need to enclose the key strings in quotes!!
person = dict(name="sally", age=28, height=185, weight=70, smokes="no", drinks="no", married="no",
              worth=100000, income=2500, street="Glendower Road", street_number=11, post_code_code="B42 1SY")

# print(person["name"])


#  Print each key item and it's value  pair
for x, y in person.items():
    print(x, ":", y)

car = dict(model="Ford", series="Fiesta", year=2018, colour="Blue")
print(car)

for x in car:
    print(car[x])

car = dict(model="Ford", series="Fiesta", year=2018, colour="Blue")

car_type = car[model]


