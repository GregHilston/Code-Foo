_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Your goal is to decode a time encoding that is used to explain when a business is open.

## Input Description

Each input will consist of multiple 11-character chunks, with no separators
Format as follows:

    ABCCCCDDDDE
    ABCCCCDDDDE
    ABCCCCDDDDE

Where:
    A: day code (start)
    B: day code (end)
    C: time code (start)
    D: time code (end)
    E: time type code

    day code:
        M: Monday
        T: Tuesday
        W: Wednesday
        R: Thursday
        F: Friday
        S: Saturday
        N: Sunday

    time code:
        ####: (military time format - hhmm, where 0000 is midnight)

    time type codes:
        H: Hours Open                   "open"

    Please note: time range 00000000 means '24h'

## Output Description

    Returns the open hours:

        {
            sunday: '24h',
            monday: '8:00am - 12:30pm, 2:30pm - 6:00pm',
            tuesday: '2:00pm - 5:00pm',
            ...
        }

    When a block spans multiple days, copy its time range to each day
        For example:
            "MF09001700H" would parse out to
            {
                sunday: '',
                monday: '9:00am - 5:00pm',
                tuesday: '9:00am - 5:00pm',
                wednesday: '9:00am - 5:00pm',
                thursday: '9:00am - 5:00pm',
                friday: '9:00am - 5:00pm',
                saturday: ''
            }

# Acknowledgment

Dakota Sullivan (/u/djqballer) wrote this challenge, so props to him