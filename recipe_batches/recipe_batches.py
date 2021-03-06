#!/usr/bin/python
"""
******** Polya ********
1) Understand the problem
----------------------
What is our input?
• We get two dictionaries with key/value pairs

What are the restrictions?
• The restrictions are based on the values inside each dictionary,
  we may not have enough ingredients to work with for a given recipe.

What does our function return?
• We return an integer that is equal to the number of batches we can make, i.e. the count.

2) Plan
• What is the minimum number of loops we need to perform in order to write a working implementation.
• Dictionaries do not maintain order.
• To search a dictionary is O(1) so to search for an item in a recipe dictionary it will always be constant by using recipe['milk']
• We need to loop through the ingredients dictionary, and may loop through it more than once.
• This function looks like a linear solution as the best case, where the number of batches is equal to zero.
• We will loop through the ingredients dictionary
  • We will take the value of the current index in the ingredients dictionary
  • We will check if the ingredient is in the recipe dictionary
  • If so we will use bracket notation to get the value for example recipe['milk']
  • We will subtract value of recipe['milk'] from the value of ingredient['milk']
  • If the value is less than 0 we know we haven't got enough ingredients to make this recipe and we will break out the loop
  • If we have enough ingredients to make one batch we will add 1 to the count
  • When we break out the loop we will return the count.
3) Execute the plan
-------------------

"""

import math


def recipe_batches(recipe, ingredients):
    batch = 0
    update = True

    while update:
        for key in recipe.keys():
            if key not in ingredients.keys():
                update = False
            elif ingredients[key] - recipe[key] < 0:
                update = False
            else:
                ingredients[key] -= recipe[key]
        if update:
            batch += 1
    return batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}."
        .format(batches=recipe_batches(recipe, ingredients),
                ingredients=ingredients))
