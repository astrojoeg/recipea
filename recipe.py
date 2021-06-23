#recipe class that has ingredients, cook_time, and calorie count attributes
#the ingredients will be an array of Ingredient objects
#Ingredient objects will have calorie attribute that the recipe class will use
#to calculate total calorie count for the recipe

import csv
from reciPY import recipe_bank

class recipe(object):
    def __init__(self, name, ingreds, cook_time, tot_cal, origin):
        self.origin = origin
        self.name = name
        self.tot_cal = 0
        self.ingreds = ingreds
        for i in range(len(ingreds)):
            self.tot_cal += ingreds[i].calorie
        self.cook_time = cook_time
        self.add_rec()


    def add_rec(self, rec):
        recipe_bank.append(self.name, self.ingreds, self.cook_time, self.origin)




