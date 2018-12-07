_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Before you is a device's tiny screen, which reads "Error: Device must be calibrated before first use. Frequency drift detected. Cannot maintain destination lock." Below the message, the device shows a sequence of changes in frequency (your puzzle input). A value like +6 means the current frequency increases by 6; a value like -3 means the current frequency decreases by 3.

Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

## Example 1

**Input**: +1, -2, +3, +1

**Output**: 3

**Explanation**:

Starting from a frequency of zero, the following changes would occur:
    Current frequency  0, change of +1; resulting frequency  1.
    Current frequency  1, change of -2; resulting frequency -1.
    Current frequency -1, change of +3; resulting frequency  2.
    Current frequency  2, change of +1; resulting frequency  3.

## Example 2

**Input**: +1, +1, +1

**Output**: 3

**Explanation**:

## Example 3

**Input**: +1, +1, -2

**Output**: 0

## Example 4

**Input**: -1, -2, -3

**Output**: -6

## Second Part Of Challenge

The following was released during the Friday level up.

You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to find the first frequency it reaches twice.

For example, using the same list of changes above, the device would loop as follows:

    Current frequency  0, change of +1; resulting frequency  1.

    Current frequency  1, change of -2; resulting frequency -1.

    Current frequency -1, change of +3; resulting frequency  2.

    Current frequency  2, change of +1; resulting frequency  3.

    (At this point, the device continues from the start of the list.)

    Current frequency  3, change of +1; resulting frequency  4.

    Current frequency  4, change of -2; resulting frequency  2, which has already been seen.

In this example, the first frequency reached twice is 2. Note that your device might need to repeat its list of frequency changes many times before a duplicate frequency is found, and that duplicates might be found while in the middle of processing the list.

Here are other examples:

    +1, -1 first reaches 0 twice.

    +3, +3, +4, -2, -4 first reaches 10 twice.

    -6, +3, +8, +5, -6 first reaches 5 twice.

    +7, +7, -2, -7, -4 first reaches 14 twice.

What is the first frequency your device reaches twice?

## Sample Input File

[Find Here](https://github.com/GregHilston/Code-Foo/blob/master/Challenges/challenge_15_advent_of_code_day_1/input.txt)

## Commentary

You are more than welcome, and borderline encouraged, to post your solution on [Advent of Code](https://adventofcode.com/).

## Acknowledgement

[This is day one of the 2018 Advent of Code. For full "role play" description, see here](https://adventofcode.com/2018/day/1)