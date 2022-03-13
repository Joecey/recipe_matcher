# recipe matcher code (using breakfast api)
import requests

# split string into individual words and convert to a list (might not use)
def convert(lst):
    converted = lst.split()
    return converted

# Function to ask user to list available ingredients
def give_ingredients():
    repeat_ask = True
    food_list = []


    while repeat_ask is True:
        ask = str(input("Type food item, or type DONE to complete: "))
        
        if ask == "DONE":
            repeat_ask = False

        else:
            # add a checker for miss spellings? (compare to ingredients.txt file???)
            # convert to lowercase and add ingredient to food list
            ask = ask.lower()
            food_list.append(ask)

    # return complted food list
    return food_list

# find suitable recipe with food list using breakfast api
def find_recipe(food_list):
    confirm_recipe = False

    # check available recipes until suitable one found
    while confirm_recipe is False:
        # pull random reciepe from breakfastapi
        print("new recipe!")
        r = requests.get("https://breakfastapi.fun/")
        data = r.json()

        # pull ingredients from random recipe
        ingre_check = data["recipe"]["ingredients"]
        recipe_title = data["recipe"]["name"]
        recipe_directions = data["recipe"]["directions"]

        # check ingredient list together
        # keep track of how far you are in food_list
        list_progress = 0

        #check if item is in random recipe
        for i in food_list:

            # if it is...
            if i in ingre_check:
                list_progress = list_progress+1

                # if we make it to the end of food_list with no problems, confirm recipe
                if list_progress == len(food_list):
                    confirm_recipe = True

            # if not... check the following
            else:

                # if at least ONE INGREDIENT WAS FOUND, return recipe
                if list_progress > 0: 
                    confirm_recipe = True

                # if no ingredient was successfully matched beforehand, dont change confirm
                # recipe status
                else:
                    break
    
    # return random recipe
    return recipe_title, ingre_check, recipe_directions


# ask user for ingredient list 
food_list = give_ingredients()

# depending on what's in food list...
if len(food_list) == 0:
    print("food list is empty")

else:
    print(food_list)

    # find suitable recipe and print title, ingredients and directions
    recipe, ingredie, direct = find_recipe(food_list)
    print(recipe)
    print(ingredie)
    print(direct)

