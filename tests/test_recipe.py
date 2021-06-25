import pandas as pd
from reciPY import find_recipe

recipe_bank = pd.read_csv('recipe_bank.csv')


def test_find_recipe(recipe_bank):
    ingredients = recipe_bank.ingredients.values
    for i in range(len(ingredients)):
        print(ingredients[i])
        find_recipe(ingredients[i].split(', '), ingredients, recipe_bank.recipe_name.values, recipe_bank)


if __name__ == "__main__":
    test_find_recipe(recipe_bank)