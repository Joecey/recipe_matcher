# recipe matcher code (using breakfast api)
# functions (list all ingredients in one input)

def convert(lst):
    converted = lst.split()
    return converted

# list ingredients one by one
def give_ingredients():
    repeat_ask = True
    food_list = []

    while repeat_ask is True:
        ask = str(input("Type food item in lower case, or type DONE to complete: "))
        
        if ask == "DONE":
            repeat_ask = False

        else:
            # add a checker for miss spellings? (compare to ingredients.txt file???)
            # add ingredient to food list
            food_list.append(ask)

    return food_list

# find suitable recipe with food list
def find_recipe(food_list):
    pass


# ask user for food list
# ask_food = str(input("Please list food available in pantry. Use lower case letter and separate items with a space. \n"))

food_list = give_ingredients()


# depending on what's in food list...
if len(food_list) == 0:
    print("food list is empty")

else:
    print(food_list)

