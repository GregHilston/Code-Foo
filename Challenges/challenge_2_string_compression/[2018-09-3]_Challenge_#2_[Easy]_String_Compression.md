_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3.

If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

# Examples
`compress("aabcccccaaa")` => `"a2blc5a3"`

`compress("a")` => `"a"`

`compress("aa")` => `"aa"`

`compress("aaa")` => `"a3"`

`compress("A")` => `"A"`

`compress("AA")` => `"AA"`

`compress("AAA")` => `"A3"`

`compress("abbcccddddeeeee")` => `"a1b2c3d4e5"`

# Optional Bonus 1
Write unit tests for your function.

_Hint: Use the examples above as your tests_


# Optional Bonus 2
What is the big O of your solution?


# Acknowledgment
*Thanks to [Gayle McDowell's Cracking the Coding Interview, Fifth Edition](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/098478280X)*
