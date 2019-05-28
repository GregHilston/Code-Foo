_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

There are `n` bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the `i-th` round, you toggle every `i` bulb. For the `n-th` round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

## Example 1

Input: 3

Output: 1

Explanation:

At first, the three bulbs are [off, off, off].

After first round, the three bulbs are [on, on, on].

After second round, the three bulbs are [on, off, on].

After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.

## Acknowledgement

This challenge was taken from [Leet Code](https://leetcode.com/problems/bulb-switcher/).