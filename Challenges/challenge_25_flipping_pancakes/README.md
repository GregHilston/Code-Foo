_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

I work as a waiter at a local breakfast establishment. The chef at the pancake house is sloppier than I like, and when I deliver the pancakes I want them to be sorted biggest on bottom and smallest on top. Problem is, all I have is a spatula. I can grab substacks of pancakes and flip them over to sort them, but I can't otherwise move them from the middle to the top.

How can I achieve this efficiently?

This is a well known problem called the pancake sorting problem. Bill Gates once wrote a paper on this that established the best known upper bound for 30 years.

This particular challenge is two-fold: implement the algorithm, and challenge one another for efficiency.

_Note: Only tackle efficiently as much as you want to. Just solving the problem set is good enough._

Look at the input on [Github here](https://github.com/GregHilston/Code-Foo/tree/master/Challenges/challenge_25_flipping_pancakes).

## Example 1

### Input Description

You'll be given a pair of lines per input. The first line tells you how many numbers to read in the next line. The second line tells you the pancake sizes as unsigned integers. Read them in order and imagine them describing pancakes of given sizens from the top of the plate to the bottom. Example:

    3
    3 1 2

### Output Description

Your program should emit the number of spatula flips it took to sort the pancakes from smallest to largest. Optionally show the intermediate steps. Remember, all you have is a spatula that can grab the pancakes from the 0th to the _n_th position and flip them. Example:

    2 flips: 312 -> 213 -> 123

### Challenge Example 2

_Note: This is harder than just Example 1 and I don't have output for this at the time. Feel free to provide the answers to this._

    8
    7 6 4 2 6 7 8 7

### Challenge Example 3

_Note: This is harder than just Example 1 and I don't have output for this at the time. Feel free to provide the answers to this._

    8
    11 5 12 3 10 3 2 5

### Challenge Example 4

_Note: This is harder than just Example 1 and I don't have output for this at the time. Feel free to provide the answers to this._

    10
    3 12 8 12 4 7 10 3 8 10

## Acknowledgement

[This challenge was taken from /r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer/comments/82pt3h/20180307_challenge_353_intermediate/). There are awesome submissions here, so check your work afterwords to learn something new!