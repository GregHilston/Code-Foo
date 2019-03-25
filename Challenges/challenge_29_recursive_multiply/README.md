_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Write a recursive function to  multiply two positive integers without using the `*` operator. You can use addition, subtraction and bit shifting, but you should minimize the number of those operators.

A sample function signature:

```
public int recursiveMultiply(int multiplicand, int multiplier) {
    return someOtherFunctionThatWillCallItselfRecursively(multiplicand, multiplier);
}
```

## Example 1

```
int product = this.recursiveMultiply(5, 5));

System.out.println(product); // 25
```

## Acknowledgement

[This challenge was taken from Cracking the Code Interview 6 Edition](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850/ref=sr_1_1?crid=29V41WCUZNYNX&keywords=cracking+the+coding+interview&qid=1553518745&s=books&sprefix=crac%2Cstripbooks%2C171&sr=1-1).