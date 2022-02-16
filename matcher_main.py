# recipe matcher code (using breakfast api)

# functions
def convert(lst):
    converted = lst.split()
    return converted

# find suitable recipe
def find_recipe():
    pass

# ask user for food list
ask_food = str(input("Please list food available in pantry. Use lower case letter and separate items with a space. \n"))

# convert string into seperate words
food_list = convert(ask_food)

# print food list
for i in food_list: print(i)


