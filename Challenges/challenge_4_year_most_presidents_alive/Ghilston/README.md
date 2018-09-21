Language: Node


Description: My solution does the following steps:
  1. Parse the entire CSV into a object (also known as dictionary or hash table), with the following structure
    
    president name => object("birthYear": value, "deathYear": value)
    
    O(n)

  2. Finds the earliest year in the data set

    O(n)

  3. Finds the latest year in the data set

    O(n)

  4. Loops from the earliest year to the latest year, traversing our object, determining how many presidents were alive in each year, building up a new object with the following structure:

    year => president names[]

    O(n)

  5. Loops through newly built up object, finding year(s) with the most number of alive presidents.

    O(n)

Big O: O(5n) => O(n)


Source:
    
    [REPLACE WITH SOURCE]

Repl.it with test: https://repl.it/@GregHilston/CodeFooChallenge3DiceRoller