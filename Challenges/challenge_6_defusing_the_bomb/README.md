_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

To disarm the bomb you have to cut some wires. These wires are either white, black, purple, red, green or orange.

The rules for disarming are simple:

    If you cut a white cable you can't cut white or black cable.
    If you cut a red cable you have to cut a green one
    If you cut a black cable you can't cut a white, green or orange one
    If you cut a orange cable you have to cut a red or black one
    If you cut a green one you have to cut a orange or white one
    If you cut a purple cable you can't cut a purple, green, orange or white cable

If you have anything wrong in the wrong order, the bomb will explode. 


There can be multiple wires with the same colour and these instructions are for one wire at a time. Once you cut a wire you can forget about the previous ones. 

## Input description

You will receive a sequence of wires that where cut in that order and you have to determine if the person was succesfull in disarming the bomb or that it blew up.

### Input 1

    white
    red
    green
    white

### Input 2

    white
    orange
    green
    white

## Output description

Whether or not the bomb exploded

### Output 1

    "Bomb defused"

### Output 2

    "Boom"

# #Notes/Hints

A state machine will help this make easy

# Acknowledgment

[This Coding Challenge _please don't look until you've finished your own solution_](https://www.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/)

