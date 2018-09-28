"use strict" // forcing ourselves to write better NodeJS

const request = require('request')  // used to make http requests
const util = require('util')        // used to print objects

function fetchFilteredRecipes(query, allergens, callback) {
    const baseUrl = "http://www.recipepuppy.com/api/?q="
    var filtered_recipes = []

    request(baseUrl + query, { json: true }, (err, res, body) => {
        if (err) { 
            console.log("fetchFilteredRecipes experience error: " + err)
            return err
        }

        body.results.forEach((recipe, index, array) => {            
            var ingredients = recipe.ingredients.split(',')
            
            ingredients = ingredients.map(function(ingredient) {
                return ingredient.trim()
            })

            var foundAllergens = ingredients.filter((ingredient) => {
                var subStringsIngredient = ingredient.split(' ').map(function(subStringIngredient) {
                    return subStringIngredient.trim();
                })

                return allergens.some(r=> subStringsIngredient.indexOf(r) >= 0)
            })

            if (foundAllergens.length == 0) {
                filtered_recipes.push(recipe)
            }
        })

        callback(filtered_recipes)
      })
}

function receivedFilteredRecipes(filteredRecipes) {
    console.log(filteredRecipes)
}

fetchFilteredRecipes("candy", ["peanut"], receivedFilteredRecipes)