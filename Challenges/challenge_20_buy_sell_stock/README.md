_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

You can either copy and paste the Strings into your function call, or look at the following input files [input_1.json](https://github.com/GregHilston/Code-Foo/blob/master/Challenges/challenge_20_buy_sell_stock/input_1.json) or [input_2.json](https://github.com/GregHilston/Code-Foo/blob/master/Challenges/challenge_20_buy_sell_stock/input_2.json) I'll provide. Do whatever is easier for you.

_Note:_

- _You cannot sell a stock before you buy one._
- _You may assume that all numbers are `0` or greater._

## Examples

### Example 1

Input: [7,1,5,3,6,4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Not 7-1 = 6, as selling price needs to be larger than buying price.

### Example 2

Input: [7,6,4,3,1]

Output: 0

Explanation: In this case, no transaction is done, i.e. max profit = 0.

## Acknowledgement

[This challenge was taken from Leet Code Please don't look at this link until you've solved it yourself](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/). There are awesome submissions here, so check your work afterwords to learn something new!