# This is our main branch python file that users will run to use our package

import argparse
from pandas import read_csv
import numpy as np

##### Define a crossmatch function to figure out what recipe you can cook #####
def find_recipe(your_ingredients, ingredients_bank, recipe_names):
	"""Find Recipe

    Find what recipes you can cook based on your available ingredients and your recipe bank.

    Args:
        your_ingredients (array): Numpy 1-D array. List of ingredients that you have instock that
			that you inputted.
        ingredients_bank (array): Numpy 1-D array. List including the required ingredients of each recipe.
		recipe_names (array): Numpy 1-D array. List including the names of each recipe.

    Returns:
        None: a print statement is the output.
    """

	# Look for the recipe that has the most matches with your ingredients from the pantry
	ingredients_matches = np.array([len(np.where(np.isin(your_ingredients, i.split(', ')))[0]) for i in ingredients_bank])
	best_match = np.where(ingredients_matches == max(ingredients_matches))[0]
	if all(ingredients_matches == 0):
	    best_match = []

	# Proceed depending on the number of recipes you can cook
	if len(best_match) == 1:
	    print('Based on your ingredients, we suggest you cook', recipe_names[best_match][0])
	    print('You have {}/{} ingredients already.'.format(ingredients_matches[best_match][0], len(ingredients_bank[best_match[0]].split(','))))

	elif len(best_match) > 1:
	    print('Based on your ingredients, we you can cook {} recipes'.format(len(best_match)))
	    for j in range(len(best_match)):
		    print('{} - {}. You have {}/{} ingredients already.'.format(j+1, recipe_names[best_match[j]], ingredients_matches[best_match[j]], len(ingredients_bank[best_match[j]].split(','))))

	elif len(best_match) == 0:
	    print("It doesn't look like you have any ingredients that match out recipes.")
	    build_recipe = input('Would you like to write a new recipe? (Y/[N]): ')
	    if (build_recipe == 'Y') or (build_recipe == 'y'):
			# CALLL WRITING FUNCTION
		    print('You need to write that write a recipe function')
		
	if len(best_match) >=1:
		print('')
		build_shopping_list = input('Would you like to write a shopping list? (Y/[N]): ')
		if (build_shopping_list == 'Y') or (build_shopping_list == 'y'):
			for j in range(len(best_match)):
				print('Shopping list',recipe_bank.ingredients.values[best_match[j]])


# Initialize the reciPY Suite
if __name__ == '__main__':

	# Print a usage message to the command line
	print('\n##########################################################')
	print('#                                                        #')
	print('#                 Hi! Welcome to reciPY!                 #')
	print('#                                                        #')
	print('#  This suite will help you figure out what recipe you   #')
	print('#  can cook right now.                                   #')
	print('#                                                        #')
	print('##########################################################\n')
	
	# Generate arguments for command line parsing
	parser = argparse.ArgumentParser(description='Provide path name to data directory.')
	parser.add_argument('-f', '--filepath',type=str,default='recipe_bank.csv',
						help="Path to location of your recipe bank.")
	args = parser.parse_args()
	# Import the pre-constructed recipe bank
	recipe_bank = read_csv(args.filepath)

	# Input what ingredients you have in the pantry
	print('#  To begin please input what ingredients you currently  #')
	print('#  have in stock, separated by commas.                   #\n')
	ingredients_input = input('List current ingredients: ')

	#            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	#   ADD HERE FUNCTIONALITY TO START OFF BY WRITING A RECIPE?
	#            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	# Double check to see if they would like to add anything else
	print('You entered ' + ingredients_input + '.')
	check_ingredients = input('Would you like to add anything else? (Y/[N]): ')
	if (check_ingredients == 'Y') or (check_ingredients == 'y'):
		new_ingredients = input('Add new ingredients: ')
		ingredients = (ingredients_input + ', ' + new_ingredients).split(', ')
		print('')
	else:
		ingredients = ingredients_input.split(', ')
		print('')

	find_recipe(ingredients,recipe_bank.ingredients.values,recipe_bank.recipe_name.values)




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
