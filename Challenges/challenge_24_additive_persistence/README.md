_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Inspired by this [tweet](https://twitter.com/fermatslibrary/status/1089883307473543170), today's challenge is to calculate the [_additive persistence_](http://mathworld.wolfram.com/AdditivePersistence.html) of a number, defined as how many loops you have to do summing its digits until you get a single digit number. Take an integer N:

1. Add its digits
2. Repeat until the result has 1 digit

The total number of iterations is the additive persistence of N.

Your challenge today is to implement a function that calculates the additive persistence of a number.

Look at the input on [Github here](https://github.com/GregHilston/Code-Foo/tree/master/Challenges/challenge_24_additive_persistence).

## Example 1

input = 13
output = 1

Explained:

1. Given 13, sum the digits 1 and 3 to get 4.

4 is a single digit number. We're done

## Example 2

input = 1234
output = 2

Explained:

1. Given 1234, sum the digits 1, 2, 3 and 4 to get 10.
2. Given 10, sum the digits 1 and 0 to get 1.

1 is a single digit number. We're done

## Example 3

input = 9876
output = 2

Explained:

1. Given 9876, sum the digits 9, 8, 7 and 6 to get 30.
2. Given 30, sum the digits 3 and 0 to get 3.

3 is a single digit number. We're done

## Example 4

input = 199
output = 3

Explained:

1. Given 199, sum the digits 1, 9 and 9 to get 19.
2. Given 19, sum the digits 1 and 9 to get 10.
3. Given 10, sum the digits 1 and 0 to get 1.

1 is a single digit number. We're done

## Acknowledgement

[This challenge was taken from /r/dailyprogrammer](https://old.reddit.com/r/dailyprogrammer/comments/akv6z4/20190128_challenge_374_easy_additive_persistence//). There are awesome submissions here, so check your work afterwords to learn something new!