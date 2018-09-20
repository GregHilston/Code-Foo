_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!


# Challenge

Plenty of table top and video games use dice rolls for game play. Lets write a function to act as our dice roller!


## Input description

Your input will be in the form of "NdM", where N is the number of di and M is how many sides the die have.

The first number is the number of dice to roll, the d just means "dice", it's just used to split up the two numbers, and the second number is how many sides the dice have. So the above example of "3d6" means "roll 3 6\-sided dice". Also, just in case you didn't know, in most games, not all the dice we roll are the normal cubes. A d6 is a cube, because it's a 6\-sided die, but a d20 has twenty sides, so it looks a lot closer to a ball than a cube.

The first number, the number of dice to roll, can be any integer between 1 and 100, inclusive.

The second number, the number of sides of the dice, can be any integer between 2 and 100, inclusive.


## Output description

You should output the sum of all the rolls of that specified die, each on their own line. so if your input is "3d6", the output should look something like

    14

Just a single number, you rolled 3 6\-sided dice, and they added up to 14.


If the first number is not between 1 and 100, inclusive or the second number is not between 2 and 100, inclusive, return an empty string.

# Examples

`roll("0d100")` `=>` ""

`roll("1d1")` `=>` ""

`roll("1d101")` `=>` ""

`roll("101d2")` `=>` ""

`roll("5d12")` `=>` some number between 5 and 60, probably closer to 32 or 33

`roll("6d4")` `=>` some number between 6 and 24, probably around 15

`roll("1d8")` `=>` some number between 1 and 8

`roll("3d6")` `=>` some number between 3 and 18, probably around 9

`roll("4d20")` `=>` some number between 4 and 80, probably around 40

`roll("100d100")` `=>` some number between 100 and 10000, probably around 5000


# Optional Bonus 1

In addition to the sum of all dice rolls for your output, print out the result of each roll on the same line, using a format that looks something like

    14: 6 3 5
    22: 10 7 1 4
    9: 9
    11: 3 2 2 1 3

# Optional Bonus 2

Write unit tests for your function.

Hint: Use the examples above as your tests


# Optional Bonus 3

What is the big O of your solution?


# Acknowledgment

[This Coding Challenge _please don't look until you've finished your own solution_](https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/)
