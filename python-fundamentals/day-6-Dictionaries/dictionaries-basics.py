
person = {"name": "lamin", "age": 28, "height": 185, "weigh": 70, "smokes": "no", "drinks": "no", "married": "no",
          "worth": 100000, "income": 2500, "street": "Glendower Road", "street-number": 11, "post-code": "B42 1SY"}

person_name = person["name"]
person_age = person["age"]
person_height = person["height"]
person_post_code = person["post-code"]

print("Person's name is {}, age is {}, height is {}, and {}'s post code is "
      "{}".format(person_name, person_age, person_height, person_name, person_post_code))
print(person["name"])
print(person["age"])

for details in person:
    print(details)
    # This loop only prints the dictionary keys

for person_values in person.values():
    print(person_values)
    # This other loop prints only the dictionary values
print("------------------------line breaker------------------------")

person = {"name": "sally", "age": 28, "height": 185, "weigh": 70, "smokes": "no", "drinks": "no", "married": "no",
          "worth": 100000, "income": 2500, "street": "Glendower Road", "street-number": 11, "post-code": "B42 1SY"}

# Clear the values in the dictionary
#person.clear()

# Print all the items in the dictionary (keys and values)
#print(person.items())

# Print only the dictionary keys values
#print(person.values())

# removes and prints the last value from the dictionary or the key
print(person.pop("age"))
print(person) # printing the dictionary will show that 'age' dictionary key and value is not present  anymore

#len(person)

