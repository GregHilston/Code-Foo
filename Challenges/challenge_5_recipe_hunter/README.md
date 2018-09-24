_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Food allergies are becoming more problematic ever year. Your task is to write a small program to help find recipes that would be safe to eat with a given set of allergies. For this challenge you'll be reaching out to a free and public API called "Recipe Puppy".

To read more about Recipe Puppy's API, see [here](http://www.recipepuppy.com/about/api/)

_Note: You will not need to use the `i` or `p` parameter for this challenge. Only the `q` parameter will be needed_

## Input description

Your input will be a search query, like "candy", and a list of allergens, like ["peanut"].

The search query will be a non-empty string and the list of allergens will be a list of non-empty strings. The allergens list may be empty.

## Output description

You're goal is to hit the API with the given search query, fetching all the recipes they have for that query, and filtering out any recipes with any of the given allergens as an ingredient. Use substring matching to find allergens, so given allergen of "peanut" should filter out "peanut butter". Your output should be valid json, formatted in the same way that Recipe Puppy returns.

_Disclaimer: This program should in no way be used by individuals with real allergies._

# Examples

fetchFilteredRecipes("candy", ["peanut]) =>

> {
   "title":"Recipe Puppy",
   "version":0.1,
   "href":"http:\/\/www.recipepuppy.com\/",
   "results":[
      {
         "title":"Hot Cinnamon Candy Covered Apples",
         "href":"http:\/\/allrecipes.com\/Recipe\/Hot-Cinnamon-Candy-Covered-Apples\/Detail.aspx",
         "ingredients":"apple, cinnamon, powdered sugar, corn syrup, food coloring, water, sugar",
         "thumbnail":""
      },
      {
         "title":"Hard Candy",
         "href":"http:\/\/allrecipes.com\/Recipe\/Hard-Candy\/Detail.aspx",
         "ingredients":"powdered sugar, food coloring, corn syrup, orange, water, sugar",
         "thumbnail":"http:\/\/img.recipepuppy.com\/18924.jpg"
      },
      {
         "title":"Chocolate Mint Candy (Fudge)",
         "href":"http:\/\/www.recipezaar.com\/Chocolate-Mint-Candy-Fudge-4075",
         "ingredients":"food coloring, peppermint extract, semisweet chocolate chips, condensed milk, vanilla extract",
         "thumbnail":"http:\/\/img.recipepuppy.com\/215785.jpg"
      },
      {
         "title":"Honeycomb Candy - Aka Hokey-Pokey or Sponge Candy",
         "href":"http:\/\/www.recipezaar.com\/Honeycomb-Candy-Aka-Hokey-Pokey-or-Sponge-Candy-29157",
         "ingredients":"baking soda, chocolate, corn syrup, honey, sugar, water",
         "thumbnail":"http:\/\/img.recipepuppy.com\/218726.jpg"
      },
      {
         "title":"Candy Cane Cake",
         "href":"http:\/\/www.recipezaar.com\/Candy-Cane-Cake-159522",
         "ingredients":"egg whites, milk, flour, shortening, sugar, vanilla extract",
         "thumbnail":""
      },
      {
         "title":"Crushed Candy Cane Lasses Recipe",
         "href":"http:\/\/www.grouprecipes.com\/24718\/crushed-candy-cane-lasses.html",
         "ingredients":"whole milk, butter, cookies, corn syrup, food coloring, eggs, frosting, powdered sugar, candy canes",
         "thumbnail":"http:\/\/img.recipepuppy.com\/282979.jpg"
      },
      {
         "title":"Pasteli  - Greek Sesame Seed Candy Recipe",
         "href":"http:\/\/www.grouprecipes.com\/52615\/pasteli---greek-sesame-seed-candy.html",
         "ingredients":"honey, salt, sesame seed, vegetable oil",
         "thumbnail":"http:\/\/img.recipepuppy.com\/283431.jpg"
      },
      {
         "title":"Christmas Hard Candy",
         "href":"http:\/\/www.recipezaar.com\/Christmas-Hard-Candy-211975",
         "ingredients":"powdered sugar, food coloring, sugar, water, karo",
         "thumbnail":""
      },
      {
         "title":"Clear Toy Candy [pa Dutch Traditional]",
         "href":"http:\/\/www.recipezaar.com\/Clear-Toy-Candy-pa-Dutch-Traditional-139685",
         "ingredients":"corn syrup, sugar, water",
         "thumbnail":""
      }
   ]
}

Note that the following result was filtered:
> {
    "title":"Ritz Cracker Cookies - No Bake - Candy Coated",
    "href":"http:\/\/www.recipezaar.com\/Ritz-Cracker-Cookies-No-Bake-Candy-Coated-344989",
    "ingredients":"peanut butter, chocolate, crackers, white chocolate",
    "thumbnail":"http:\/\/img.recipepuppy.com\/33987.jpg"
  }

# Optional Bonus 1

Implement some function cache, so if your function is called with the same query and allergens, then serve the locally cached result instead of hitting the API. This cache does not need to survive restarts of the program. In other words, the cache can exist in memory and does not need to be written to disk.

# Disclaimer

Recipe Puppy is a free public API. Please respect their terms of:

 > Recipe Puppy has a very simple API. This api lets you search through recipe puppy database of over a million recipes by keyword and/or by search query. We only ask that you link back to Recipe Puppy and let me know if you are going to perform more than 1,000 requests a day.

# Acknowledgment

- [Dr. Hazins's Ruby on Rails homework for inspiration](https://ep.jhu.edu/about-us/faculty-directory/1158-kalman-hazins)