# list of fruits available
fruits = ["apples",
          "mango",
          "pineapple",
          "pear",
          "bananas",
          "papaya",
          "oranges",
          "grapes",
          "blueberries"
          ]
# ask customer what kind of fruit they would like to find from stock
fruit_choice = str(input("Please type in the fruit you are looking for: "))

for fruit in fruits:
    if fruit.__contains__(fruit_choice):
        print("Yes!!! We have %s in stock" %fruit_choice)
        break
    else:
        print("The fruit you are looking for is out of stock \n Please come back another time")
        break
