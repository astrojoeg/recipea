# This is our main branch python file that users will run to use our package


# from defintions import ____
import pandas as pd
import numpy as np

# Import the pre-constructed recipe bank
recipe_bank = pd.read_csv('recipe_bank.csv')

# Print a usage message to the command line
print('\n##########################################################')
print('#                                                        #')
print('#                 Hi! Welcome to reciPY!                 #')
print('#                                                        #')
print('#  This suite will help you figure out what recipe you   #')
print('#  can cook right now.                                   #')
print('#                                                        #')
print('#  To begin please input what ingredients you currently  #')
print('#  have in stock, separated by commas.                   #\n')

ingredients_input = input('List current ingredients: ')

# Double check to see if they would like to add anything else
print('You entered ' + ingredients_input + '.')
check_ingredients = input('Would you like to add anything else? (Y/[N]): ')
if (check_ingredients == 'Y') or (check_ingredients == 'y'):
	new_ingredients = input('Add new ingredients: ')
	ingredients = (ingredients_input + ', ' + new_ingredients).split(', ')
else:
	ingredients = ingredients_input.split(', ')


##### Call the sorting/cross match function here to figure out what recipe you can cook #####
def find_recipe(your_ingredients, recipe_bank):
	# Look for the recipe that has the most matches with your ingredients from the pantry
    ingredients_bank = recipe_bank.ingredients.values
    ingredients_matches = np.array([len(np.where(np.isin(your_ingredients, i.split(', ')))[0]) for i in ingredients_bank])
    best_match = np.where(ingredients_matches == max(ingredients_matches))[0]
    if all(ingredients_matches == 0):
	    best_match = []

	# Proceed depending on the number of recipes you can cook
    if len(best_match) == 1:
	    print('Based on your ingredients, we suggest you cook', recipe_bank.recipe_name.values[best_match][0])
	    print('You have {}/{} ingredients already.'.format(ingredients_matches[best_match][0], len(ingredients_bank[best_match[0]].split(','))))

    elif len(best_match) > 1:
	    print('Based on your ingredients, we you can cook {} recipes'.format(len(best_match)))
	    for j in range(len(best_match)):
		    print('{} - {}. You have {}/{} ingredients already.'.format(j+1, recipe_bank.recipe_name.values[best_match[j]], ingredients_matches[best_match[j]], len(ingredients_bank[best_match[j]].split(','))))
	
    elif len(best_match) == 0:
	    print("It doesn't look like you have any ingredients that match out recipes.")
	    build_recipe = input('Would you like to write a new recipe? (Y/[N]): ')
	    if (build_recipe == 'Y') or (build_recipe == 'y'):
			# CALLL WRITING FUNCTION
		    print('You need to write that write a recipe function')
		
    if len(best_match) >=1:
       build_shopping_list = input('Would you like to write a shopping list? (Y/[N]):')
       if (build_shopping_list == 'Y') or (build_shopping_list == 'y'):
           for j in range(len(best_match)):
               print('Shopping list',recipe_bank.ingredients.values[best_match[j]])


# Test the function
find_recipe(ingredients,recipe_bank)





#### We can go a few routes here:
#### 1) They have all the ingredients for a recipe
####    - Give them option to see metadata about the recipe
####    - Give option to have it printed/written out to a text file

#### 2) They don't have all the recipes
####    - Give them the recipe that closest matches their ingredients?
####    - Write a shopping list for that recipe?
####    - Give optionodify the recipe 














# Print a closing message to the command line
print('\nFinished!\n')