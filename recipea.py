# This is our main branch python file that users will run to use our package

import argparse
import pandas as pd
import numpy as np


class recipe(object):
    def __init__(self, name, ingreds, cook_time, origin):
        self.origin = origin
        self.name = name
        # self.tot_cal = 0
        self.ingreds = ingreds
        # for i in range(len(ingreds)):
		# self.tot_cal = sum([ingreds[i].calorie for i in range(len(ingred))])
        self.cook_time = cook_time
        # self.add_rec()
		
    def add_rec(self):
        recipe_df = pd.DataFrame([[self.name, self.ingreds, self.cook_time, self.origin]],columns=['recipe_name','ingredients','cook_time','origin'])
        return recipe_df


class ingredients(object):
    def __init__(self, name, vegan, veg, gf, nf):
        self.name = name
        #self.cal = cal
        self.vegan = vegan
        self.veg = veg
        self.gf = gf
        self.nf = nf
        
    def is_vegan(self):
        if self.vegan == 'yes':
            return True
        else:
            return False

    def is_veg(self):
        if self.veg == 'yes':
            return True
        else:
            return False

    def is_gf(self):
        if self.gf == 'yes':
            return True
        else:
            return False
			
    def is_nf(self):
        if self.nf == 'yes':
            return True
        else:
            return False



##### Define a crossmatch function to figure out what recipe you can cook #####
def find_recipe(your_ingredients, ingredients_bank, recipe_names, recipe_bank):
	"""Find Recipe

    Find what recipes you can cook based on your available ingredients and your recipe bank.

    Args:
        your_ingredients (array): Numpy 1-D array. List of ingredients that you have instock that
			that you inputted.
        ingredients_bank (array): Numpy 1-D array. List including the required ingredients of each recipe.
		recipe_names (array): Numpy 1-D array. List including the names of each recipe.
		recipe_bank (DataFrame): Pandas DataFrame. The csv file containing all the known recipes' information.

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
			new_name = input("Please enter your recipe's name: ")
			new_ingredients = input("Please enter your recipe's ingredients (comma-separated): ")
			new_time = int(input("Please enter your recipe's required cooking time (minutes): "))
			new_origin = input("Please enter your recipe's place of origin: ")
			new_recipe = recipe(new_name,new_ingredients,new_time,new_origin).add_rec()
			new_bank = recipe_bank.append(new_recipe, ignore_index=True)
			
			save_recipe = input('Would you like to save this recipe to the recipe bank? (Y/[N]): ')
			if (save_recipe == 'Y') or (save_recipe == 'y'):
				new_bank.to_csv('recipe_bank.csv')
		
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
	parser.add_argument('-i', '--ingredients',type=str,default='ingredients_bank.csv',
						help="Path to location of your ingredient bank.")
	args = parser.parse_args()
	# Import the pre-constructed recipe bank
	recipe_bank = pd.read_csv(args.filepath)
	ingredient_bank = pd.read_csv(args.ingredients)

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

	find_recipe(ingredients,recipe_bank.ingredients.values,recipe_bank.recipe_name.values,recipe_bank)




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
