# This is our main branch python file that users will run to use our package


# from defintions import ____
import argparse
from pandas import read_csv
import numpy as np

##### Define a crossmatch function to figure out what recipe you can cook #####
def find_recipe(your_ingredients, recipe_bank):
	"""Find Recipe

    Find what recipes you can cook based on your available
		ingredients and your recipe bank.

    Args:
        your_ingredients (array): Numpy 1-D array. List of ingredients that you have instock that
			that you inputted.
        recipe_bank (DataFrame): Pandas DataFrame. A csv file including all your recipes and
			their corresponding ingredient requirements and other metadata.

    Returns:
        None: a print statement is the output.
    """

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