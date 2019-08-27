_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

The nation of Examplania has the following income tax brackets:

    income cap      marginal tax rate
      ¤10,000           0.00 (0%)
      ¤30,000           0.10 (10%)
     ¤100,000           0.25 (25%)
        --              0.40 (40%)

If you're not familiar with how tax brackets work, see the section below for an explanation.

Given a whole-number income amount up to ¤100,000,000, find the amount of tax owed in Examplania. Round down to a whole number of ¤.

## How tax brackets work

A tax bracket is a range of income based on the income caps, and each tax bracket has a corresponding marginal tax rate, which applies to income within the bracket. In our example, the tax bracket for the range ¤10,000 to ¤30,000 has a marginal tax rate of 10%. Here's what that means for each bracket:

* If your income is less than ¤10,000, you owe 0 income tax.
* If your income is between ¤10,000 and ¤30,000, you owe 10% income tax on the income that exceeds ¤10,000. For instance, if your income is ¤18,000, then your income in the 10% bracket is ¤8,000. So your income tax is 10% of ¤8,000, or ¤800.
* If your income is between ¤30,000 and ¤100,000, then you owe 10% of your income between ¤10,000 and ¤30,000, plus 25% of your income over ¤30,000.
* And finally, if your income is over ¤100,000, then you owe 10% of your income from ¤10,000 to ¤30,000, plus 25% of your income from ¤30,000 to ¤100,000, plus 40% of your income above ¤100,000.

One aspect of progressive taxation is that increasing your income will never decrease the amount of tax that you owe, or your overall tax rate (except for rounding).

# Examples

tax(0) => 0
tax(10000) => 0
tax(10009) => 0
tax(10010) => 1
tax(12000) => 200
tax(56789) => 8697
tax(1234567) => 473326

## Acknowledgement

This challenge was taken from [Daily Programmer](https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/).
