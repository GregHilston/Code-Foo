_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number. 

_Note:_

- _You may assume the greed factor is always positive._
- _You cannot assign more than one cookie to one child._

You can either copy and paste the Strings into your function call, or look at the input files in the [repo](https://github.com/GregHilston/Code-Foo/blob/master/Challenges/challenge_23_assign_cookies/).

## Example 1

Input: 

```
{
  "children": [1, 2, 3],
  "cookies": [1, 1],
  "output": 1
}
```

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.

And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.

You need to output 1.

## Example 2

```
{
  "children": [1, 2]],
  "cookies": [1 ,2, 3]
  "output": 2
}
```

Output: 2

Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.

You have 3 cookies and their sizes are big enough to gratify all of the children,

You need to output 2.

## Acknowledgement

[This challenge was taken from Leet Code Please don't look at this link until you've solved it yourself](https://leetcode.com/problems/assign-cookies/). There are awesome submissions here, so check your work afterwords to learn something new!