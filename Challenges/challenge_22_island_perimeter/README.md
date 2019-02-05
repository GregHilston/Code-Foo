_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

You can either copy and paste the Strings into your function call, or look at the input files in the [repo](https://github.com/GregHilston/Code-Foo/tree/master/Challenges/challenge_21_word_pattern).

## Example 1

Input:
[

 [0,1,0,0],

 [1,1,1,0],

 [0,1,0,0],

 [1,1,0,0]

]

Output: 16

Explanation: The perimeter is the 16 yellow stripes, seen in this [image](https://assets.leetcode.com/uploads/2018/10/12/island.png)

## Acknowledgement

[This challenge was taken from Leet Code Please don't look at this link until you've solved it yourself](https://leetcode.com/problems/island-perimeter/). There are awesome submissions here, so check your work afterwords to learn something new!