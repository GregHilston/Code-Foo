"use strict" // forcing ourselves to write better NodeJS

const request = require('request')  // used to make http requests
const util = require('util')        // used to print objects
const assert = require('assert')

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
    const expectedOutput = '[{"title":"Hot Cinnamon Candy Covered Apples","href":"http:\/\/allrecipes.com\/Recipe\/Hot-Cinnamon-Candy-Covered-Apples\/Detail.aspx","ingredients":"apple, cinnamon, powdered sugar, corn syrup, food coloring, water, sugar","thumbnail":""},{"title":"Hard Candy","href":"http:\/\/allrecipes.com\/Recipe\/Hard-Candy\/Detail.aspx","ingredients":"powdered sugar, food coloring, corn syrup, orange, water, sugar","thumbnail":"http:\/\/img.recipepuppy.com\/18924.jpg"},{"title":"Chocolate Mint Candy (Fudge)","href":"http:\/\/www.recipezaar.com\/Chocolate-Mint-Candy-Fudge-4075","ingredients":"food coloring, peppermint extract, semisweet chocolate chips, condensed milk, vanilla extract","thumbnail":"http:\/\/img.recipepuppy.com\/215785.jpg"},{"title":"Honeycomb Candy - Aka Hokey-Pokey or Sponge Candy","href":"http:\/\/www.recipezaar.com\/Honeycomb-Candy-Aka-Hokey-Pokey-or-Sponge-Candy-29157","ingredients":"baking soda, chocolate, corn syrup, honey, sugar, water","thumbnail":"http:\/\/img.recipepuppy.com\/218726.jpg"},{"title":"Candy Cane Cake","href":"http:\/\/www.recipezaar.com\/Candy-Cane-Cake-159522","ingredients":"egg whites, milk, flour, shortening, sugar, vanilla extract","thumbnail":""},{"title":"Crushed Candy Cane Lasses Recipe","href":"http:\/\/www.grouprecipes.com\/24718\/crushed-candy-cane-lasses.html","ingredients":"whole milk, butter, cookies, corn syrup, food coloring, eggs, frosting, powdered sugar, candy canes","thumbnail":"http:\/\/img.recipepuppy.com\/282979.jpg"},{"title":"Pasteli  - Greek Sesame Seed Candy Recipe","href":"http:\/\/www.grouprecipes.com\/52615\/pasteli---greek-sesame-seed-candy.html","ingredients":"honey, salt, sesame seed, vegetable oil","thumbnail":"http:\/\/img.recipepuppy.com\/283431.jpg"},{"title":"Christmas Hard Candy","href":"http:\/\/www.recipezaar.com\/Christmas-Hard-Candy-211975","ingredients":"powdered sugar, food coloring, sugar, water, karo","thumbnail":""},{"title":"Clear Toy Candy [pa Dutch Traditional]","href":"http:\/\/www.recipezaar.com\/Clear-Toy-Candy-pa-Dutch-Traditional-139685","ingredients":"corn syrup, sugar, water","thumbnail":""}]'.replace(' ', '')

    assert.equal(JSON.stringify(filteredRecipes).replace(' ', ''), expectedOutput, "The recipes should match");
}

fetchFilteredRecipes("candy", ["peanut"], receivedFilteredRecipes)