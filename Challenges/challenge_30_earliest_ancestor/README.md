_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Write a function to find the id of the earliest common ancestor of two nodes in a tree. The tree will consist of unique ids. If no common ancestor exists, return -1. You may assume that the two ids given exist in the tree and do not need to handle any error handling for input given.

A sample function signature:

```
public int commonAncestor(int idOne, int idTwo) {
}
```

Please use the tree struct used by [this other challenge on leetcode](https://leetcode.com/problems/subtree-of-another-tree/), as they have structs for many many languages.

## Example 1

Given:

         3
        / \
       4   5
      / \
     1   2

```
    int commonAncestor = this.commonAncestor(1, 2);

    System.out.println(commonAncestor); // 4
```

## Example 2

Given:

         3
        / \
       4   5
      / \
     1   2

```
    int commonAncestor = this.commonAncestor(1, 4);

    System.out.println(commonAncestor); // 3
```

## Example 3

Given:

         3
        / \
       4   5
      / \
     1   2

```
    int commonAncestor = this.commonAncestor(1, 3);

    System.out.println(commonAncestor); // -1
```

## Acknowledgement

Grehg made up this challenge.