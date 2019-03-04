_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Have you ever heard the statement:

> Everytime you shuffle a deck of cards, its the first time anyone has ever created that ordering, ever.

That's because with 52 unique cards, there are 52! (fifty two factorial), combinations that one can order a deck of cards. That's 

> 80658175170943878571660636856403766975289505440883277824000000000000 possibilities

or 

> 80 unvigintillion or 10^66

which I didn't even know is a word...

This is a pretty short challenge, but you're tasked with taking a list of items, shuffling them and checking if you've seen that order before. We won't do 52 items, as that will take a very very long time. Instead, you'll work with 5 items, then 6, ... all the up to 11. 

You should do three iterations of each list of items, so that six different sized lists:

1. 5 items, three times and average the number of iterations (rounding up)
2. 6 items, three times and average the number of iterations (rounding up)
3. 7 items, three times and average the number of iterations (rounding up)
4. 8 items, three times and average the number of iterations (rounding up)
5. 9 items, three times and average the number of iterations (rounding up)
6. 10 items, three times and average the number of iterations (rounding up)

for a total of eighteen runs.

Please note, comparing how many iterations your implementation takes, against someone elses, is not significant.

I'm trying to illustrate how long it would take to run this program with 52 items.

## Example 1

### Input Description

input = [0, 1, 2, 3, 4]

### Output Description

Display something similar to this:

5 Items, Run 1: 14 iterations
5 Items, Run 2: 16 iterations
5 Items, Run 3: 11 iterations
5 Items, Run average = 14 + 16 + 11 = 14 iterations (rounded up)

...