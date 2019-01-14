_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note. 

You can either copy and paste the Strings into your function call, or look at the [input files](https://github.com/GregHilston/Code-Foo/tree/master/Challenges/challenge_19_ransom_note) I'll provide. Do whatever is easier for you.

_Note:_

_You may assume that both strings contain only lowercase letters. _

## Examples

The first String is the letters needed to construct the note, while the second String are the letters you have from cutting out of magazines. 

**Example 1**

    `canConstruct("a", "b") -> false`

We're trying to construct a ransom note with the letter `a`, while we only have the letter `b`. Since this is not possible, we return `false`.

**Example 2**

    `canConstruct("aa", "ab") -> false`

We're trying to construct a ransom note with the letter `aa`, while we only have the letters `ab`. We're able to satisfy the first letter `a`, but not the second, as we can't reuse letters so we return `false`.

**Example 3**

    `canConstruct("aa", "aab") -> true`

We're trying to construct a ransom note with the letter `aa`, while we have the letters `aab`. We're able to satisfy the first letter `a` and the second letter `a` and we don't use the `b`. Since we've successfully built our ransom note, we return `true`

## Acknowledgement

[This challenge was taken from Leet Code Please don't look at this link until you've solved it yourself](https://leetcode.com/problems/ransom-note/). There are awesome submissions here, so check your work afterwords to learn something new!