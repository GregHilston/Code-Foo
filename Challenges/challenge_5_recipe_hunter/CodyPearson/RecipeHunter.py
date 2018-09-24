import urllib.request
import urllib.parse
import json
import string

class RecipeFilter:
    def __init__(self, excludeIngredients):
        self.excludeIngredients = excludeIngredients

    def filterSingleRecipe (self, recipe):
        for ingredient in self.excludeIngredients:
            if ingredient in recipe["ingredients"]:
                return False
        
        return True

def fetchFilteredRecipes (query, excludeIngredients):
    myFilter = RecipeFilter(excludeIngredients)
    params = urllib.parse.urlencode({'q': query})
    url = "http://www.recipepuppy.com/api/?%s" % params 
    rawResponse = urllib.request.urlopen(url)
    jsonResponse = json.loads(rawResponse.read())
    filteredRecipes = list(filter(myFilter.filterSingleRecipe, jsonResponse["results"]))
    return json.dumps(filteredRecipes)

anchoviesNoCheese = fetchFilteredRecipes('anchovies', ['cheese']);

print(anchoviesNoCheese)