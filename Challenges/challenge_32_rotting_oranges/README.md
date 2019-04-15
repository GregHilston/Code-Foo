_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Alright ladies and bois, I got some moldy fruit in my house. Help me out.

In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

## Example 1

See a visual example [here](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

## Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

## Acknowledgement

This challenge was taken from [Leet Code](https://leetcode.com/problems/rotting-oranges/). Feel free to leverage Leet Code and their  structures of the data to make it easier to focus on your algorithm.