_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Imagine a given set of numbers wherein some are cannibals. We define a cannibal as a larger number can eat a smaller number and **increase its value by 1**. There are no restrictions on how many numbers any given number can consume.   A number which has been consumed is **no longer available**.  

Your task is to determine the number of numbers which can have a value equal to or greater than a specified value.  
 
## Example

> 7 2
> 21 9 5 8 10 1 3
> 10 15

*[The input above, as a file](https://github.com/GregHilston/Code-Foo/blob/master/Challenges/challenge_17_cannibal_numbers/input_1.txt)*

Based on the above description, 7 is number of values that you will be given. 2 is the number of queries.

That means:

- Query 1: How many numbers can have the value of at least 10
- Query 2: How many numbers can have the value of at least 15

With expected output:

Your program should calculate and show the number of numbers which are equal to or greater than the desired number.  For the sample input given, this will be - 

> 4 2  

## Explanation

For Query 1 -

The number 9 can consume the numbers 5 to raise its value to 10

The number 8 can consume the numbers 1 and 3 to raise its value to 10.

So including 21 and 10, we can get four numbers which have a value of at least 10.

For Query 2 -

The number 10 can consume the numbers 9,8,5,3, and 1 to raise its value to 15.

So including 21, we can get two numbers which have a value of at least 15. 

## Challenge Example

This example highlights a corner case, described [here](https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/dohd68n/)

> 9 1
> 3 3 3 2 2 2 1 1 1
> 4

The answer is 4, but you might get 3 if you don't account for this corner case.

## Acknowledgement

[This challenge was taken from reddit.com/r/dailyprogrammer Please don't look at this link until you've solved it yourself](https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/)