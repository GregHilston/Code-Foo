_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

This is a little different then most of the challenges we do. In this challenge you're asked to 

> Implement a Hash Table. Hash Collisions should be resolved using a List.

If you don't know what a Hash Table is, read about them [here](https://www.interviewcake.com/concept/java/hash-map).

You can do this any way you want, as long as you satisfy the collision resolution using a List. I recommend writing some code to prove your Hash Table is working. At a minimum, do the following:

1. Get an item from the Hash Table that's not in the Hash Table.
2. Add an item to the Hash Table that's not in the Hash Table.
3. Add an item to the Hash Table that forces a collision. Depending on your hashing algorithm, this may prove to be difficult.
4. Get an item from the Hash Table that has a key colliding with another item.

**Generally, I recommend you _never_ write your own Hashing algorithm. For this coding challenge, I think will be more fun and better for learning, if you implement your own.**