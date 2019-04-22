_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

## Example 1:

Input: 1

Output: true

Explanation: If there is 1 stone in the heap, then you will win the game. Remove 1 stone and you've won.

## Example 2:

Input: 2

Output: true

Explanation: If there is 2 stone in the heap, then you will win the game. Remove 2 stone and you've won.

## Example 3:

Input: 3

Output: true

Explanation: If there is 3 stone in the heap, then you will win the game. Remove 3 stone and you've won.

## Example 4:

Input: 4

Output: false

Explanation: If there are 4 stones in the heap, then you will never win the game. No matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

## Example 5:

Input: 5

Output: true

Explanation: If there are 5 stones in the heap, you remove 1 stone and no matter 1, 2, or 3 stones, you'll be able to remove the remaining.

## Example 6:

Input: 6

Output: true

Explanation: If there are 5 stones in the heap, you remove 2 stones and no matter 1, 2, or 3 stones, you'll be able to remove the remaining.

## Example 7:

Input: 7

Output: true

Explanation: If there are 7 stones in the heap, then you will never win the game. This was difficult for me to do, but ended up being simple. First turn you remove 3 stones, leaving the opponent with 4 stones. On their turn, no matter 1, 2, or 3 stones they remove, you'll be left with the ability to take the final stone.

## Acknowledgement

This challenge was taken from [Leet Code](https://leetcode.com/problems/nim-game/). Feel free to leverage Leet Code and their  structures of the data to make it easier to focus on your algorithm.