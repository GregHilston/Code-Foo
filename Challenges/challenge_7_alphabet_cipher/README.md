_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

"[The Alphabet Cipher](https://en.wikipedia.org/wiki/The_Alphabet_Cipher)", published by Lewis Carroll in 1868, describes a Vigenère cipher (thanks /u/Yadkee for the clarification) for passing secret messages.  The cipher involves alphabet substitution using a shared keyword.  Using the alphabet cipher to tranmit messages follows this procedure:

You must make a substitution chart like this, where each row of the alphabet is rotated by one as each letter goes down the chart.  All test cases will utilize this same substitution chart.

      ABCDEFGHIJKLMNOPQRSTUVWXYZ
pqrstuvwxyzabcdefghi
    A abcdefghi
pqrstuvwxyzabcdefghi
 opqrstuvwxyzabcdefghi
rts = { ¿extends¿: ¿airbnb-base¿ };
tuvwxyzabcdefghits = { ¿extends¿: ¿airbnb-base¿ };

    Q qrstuvwxyzabcdefghi
p
    R rstuvwxyzabcdefghi
pq
    S stuvwxyzabcdefghi
pqr
    T tuvwxyzabcdefghi
pqrs
    U uvwxyzabcdefghi
pqrst
    V vwxyzabcdefghi
pqrstu
    W wxyzabcdefghi
pqrstuv
    X xyzabcdefghi
pqrstuvw
    Y yzabcdefghi
pqrstuvwx
    Z zabcdefghi
pqrstuvwxy

Both people exchanging messages must agree on the secret keyword.  To be effective, this keyword should not be written down anywhere, but memorized.

To encode the message, first write it down.

    thepackagehasbeendelivered

Then, write the keyword, (for example, `snitch`), repeated as many times as necessary.

    snitchsnitchsnitchsnitchsn
    thepackagehasbeendelivered

 Now you can look up the column `S` in the table and follow it down until it meets the `T` row. The value at the intersection is the letter `L`. All the letters would be thus encoded.

    snitchsnitchsnitchsnitchsn
    thepackagehasbeendelivered
    lumicjcnoxjhkomxpkwyqogywq

The encoded message is now `lumicjcnoxjhkomxpkwyqogywq`

To decode, the other person would use the secret keyword and the table to look up the letters in reverse.

## Input Description

Each input will consist of two strings, separate by a space.  The first word will be the secret word, and the second will be the message to encrypt.

    snitch thepackagehasbeendelivered

## Output Description
Your program should print out the encrypted message.

    lumicjcnoxjhkomxpkwyqogywq

## Challenge Inputs

_Use these as input to test your program_

    bond theredfoxtrotsquietlyatmidnight
    train murderontheorientexpress
    garden themolessnuckintothegardenlastnight

## Challenge Outputs

_Use these as output to test your program_

    uvrufrsryherugdxjsgozogpjralhvg
    flrlrkfnbuxfrqrgkefckvsa
    zhvpsyksjqypqiewsgnexdvqkncdwgtixkx

# Bonus
For a bonus, also implement the decryption portion of the algorithm and try to decrypt the following messages.

## Bonus Inputs

_Use these as input to test your program_

    cloak klatrgafedvtssdwywcyty
    python pjphmfamhrcaifxifvvfmzwqtmyswst
    moore rcfpsgfspiecbcc

## Bonus Outputs

_Use these as input to test your program_

    iamtheprettiestunicorn
    alwayslookonthebrightsideoflife
    foryoureyesonly

# Acknowledgment

[This Coding Challenge _please don't look until you've finished your own solution_](https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/)
pqrstuvwxyz
    B bcdefghi
pqrstuvwxyza
    C cdefghi
pqrstuvwxyzab
    D defghi
pqrstuvwxyzabc
    E efghi
pqrstuvwxyzabcd
    F fghi
pqrstuvwxyzabcde
    G ghi
pqrstuvwxyzabcdef
    H hi
pqrstuvwxyzabcdefg
    I i
pqrstuvwxyzabcdefgh
    J 
pqrstuvwxyzabcdefghi
    K klmnopqrstuvwxyzabcdefghij
    L lmnopqrstuvwxyzabcdefghi
