_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling, produces the total score for the game. Here are some things that the program will not do:

- We will not check for valid rolls.
- We will not check for correct number of rolls and frames.
- We will not provide scores for intermediate frames.

Depending on the application, this might or might not be a valid way to define a complete story, but we do it here for purposes of keeping the kata light. I think you’ll see that improvements like those above would go in readily if they were needed for real.

We can briefly summarize the scoring for this form of bowling:

- Each game, or “line” of bowling, includes ten turns, or “frames” for the bowler.
- In each frame, the bowler gets up to two tries to knock down all the pins.
- If in two tries, he fails to knock them all down, his score for that frame is the total number of pins knocked down in his two tries.
- If in two tries he knocks them all down, this is called a “spare” and his score for the frame is ten plus the number of pins knocked down on his next throw (in his next turn).
- If on his first try in the frame he knocks down all the pins, this is called a “strike”. His turn is over, and his score for the frame is ten plus the simple total of the pins knocked down in his next two rolls.
- If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
The game score is the total of all frame scores.

More info on the rules at: [How to Score for Bowling](https://www.topendsports.com/sport/tenpin/scoring.htm)

(When scoring “X” indicates a strike, “/” indicates a spare, “-” indicates a miss)

If you create more examples, please share them!

## Example 1

Input: X X X X X X X X X X X X

Output: 300

Explanation: (12 rolls: 12 strikes) = 10 frames * 30 points = 300 points

## Example 2

Input: 9- 9- 9- 9- 9- 9- 9- 9- 9- 9-

Output: 90

Explanation: (20 rolls: 10 pairs of 9 and miss) = 10 frames * 9 points = 90 points

## Example 3

Input: 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5

Output: 150

Explanation: 21 rolls: 10 pairs of 5 and spare, with a final 5) = 10 frames * 15 points = 150 points

## Acknowledgement

This challenge was taken from [codingdojo](http://codingdojo.org/kata/Bowling/).