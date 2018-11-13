_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

You're goal is to write a function that takes in a Roman Numeral, as a String, and returns the Integer value. Your function should work from numbers 1 - 3999.

Use standard accepted definition of Roman Numerals, where all letters are in the upper case form.

The letters are:

I = 1

IV = 4

V = 5

IX = 9

X = 10

XL = 40

L = 50

XC = 90

C = 100

CD = 400

D = 500

CM = 900

M = 1000

## Hint

Roman Numerals are not only read by adding the value of each character. They also can be written with a subtraction rule in place. Look this rule up and understand it, or you'll have trouble with numbers like 19, which is "XIX".

[General Roman Numeral Rules](https://www.math-only-math.com/rules-for-formation-of-roman-numerals.html)
[Further Expaling Subtraction Rule](https://www.quora.com/Why-do-we-write-49-in-Roman-numerals-as-XLIX-Why-dont-we-write-it-as-IL)

## Input Description

You'll receive a single Roman Numeral value in String format, such as:

`XII`

## Output Description

You're to return the Integer representation, such as:

12

## Examples

`convertRomanNumerals(XII)` -> `12`

## Optional Bonus 1

Detect malformed Roman Numerals and return undefined or -1 when found.

`convertRomanNumerals(XLXX)` -> `undefined` (or `-1`)

`XLXX` and `XXXL` are examples where every character is a _valid_ Roman Numeral character, but their ordering is incorrect. Their proper composition of this number would be `LX`, which is 60.