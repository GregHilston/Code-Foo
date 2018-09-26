"use strict" // forcing ourselves to write better NodeJS

const request = require('request')  // used to make http requests
const util = require('util')        // used to print objects

function fetchFilteredRecipes(query, allergens) {
    const baseUrl = "http://www.recipepuppy.com/api/?q="
    var filtered_recipes = []

    request(baseUrl + query, { json: true }, (err, res, body) => {
        if (err) { 
            console.log("fetchFilteredRecipes experience error: " + err)
            return err
        }

        // console.log("err: " + err)
        // console.log("res: " + util.inspect(res, false, null, true))
        console.log("body.results: " + util.inspect(body.results, false, null, true))
        // console.log("body.explanation: " + body.explanation)

        body.results.forEach((element, index, array) => {
            console.log("element: " + util.inspect(element, false, null, true))
            console.log(body.results["ingredients"])

            body.results.ingredients.forEach(function(ingredient) {
                console.log(ingredient);
              });

            for (var ingredient in body.results.ingredients) {
                console.log("HERE")
                console.log("ingredient: " + ingredient)
            }
        })
      })
}

fetchFilteredRecipes("candy", ["peanut"])