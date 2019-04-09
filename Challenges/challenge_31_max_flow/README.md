_I suggest sorting this thread by *New* to see the most recent submissions_

The goal of these coding challenges is for you to approach these however you'd like and to have us all communicate. Some people will write their answers in languages they know very well, others will try something completely new out. Regardless of your approach, post your solutions as a top level reply below.

Reddit's formatting can be a little wonky, basically add four spaces to every line of code to get a nice looking code format applied.

Please comment on people's solutions. Ask why they did X, point out potential improvements.

Additionally, please list what language your solution is coded in.

You're more then welcome to pull request your solution into the following [Github Repo](https://github.com/GregHilston/Code-Foo)

Feel free to hit me up with any comments or questions on here, Slack or Hipchat. Happy coding!

# Challenge

Write a function to find the maximum flow from the source node to the destination node in a directed acyclic graph (DAG). I like to think of this problem as water flowing from source and destination. When looking at the flow, imagine that water is limited to the smallest pipe in its journey. The graph will be represented by a JSON file. Feel free to parse it and treat it however you'd like. 

Just to be clear, imagine that the source node has an infinite amount of water potential.

A sample function signature:

```
/**
* This function calculates the maximum flow in a DAG, described by the given JSON file path.
* @param filePath File containing the DAG.
* @return int Returns the max flow of the DAG.
*/
public int maxFlow(String filePath) {
}
```

## Example 1

Given: The following DAG 

[visually](https://raw.githubusercontent.com/GregHilston/Code-Foo/master/Challenges/challenge_31_max_flow/dag-example-1.PNG)

in JSON

```
    {
	    "source": [{
			    "1": 16
		    },
		    {
			    "2": 13
		    }
	    ],
	    "1": [{
		    	"3": 12
		    },
	    	{
	    		"2": 10
	    	}
	    ],
	    "2": [{
		    	"1": 4
		    },
		    {
			    "4": 14
		    }
	    ],
    	"3": [{
	    		"2": 9
	    	},
	    	{
	    		"sink": 20
	    	}
    	],
	    "4": [{
	    	"3": 7
    	}, {
	    	"sink": 4
	    }]
    }
```

in graphivz

```
    digraph G {
        rankdir=LR; /* Going left to right */
      
        source -> 1 [label=16];
        source -> 2 [label=13];
    
        1 -> 3 [label=12];
        1 -> 2 [label=10];
    
        2 -> 1 [label=4];
        2 -> 4 [label=14];
    
        3 -> 2 [label=9];
        3 -> sink [label=20];
    
        4 -> 3 [label=7];
        4 -> sink [label=4];
    }
```

The expected output is

```
    int maxFlow = maxFlow("dag-example-1.json);

    System.out.println(commonAncestor); // 23
```

## Additional Resources

Feel free to read [this](https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/), if you're banging your head on the wall. I deliberately used the same example.

## Acknowledgement

Grehg write this challenge. Please reach out to him with any feedback, comments or questions.

Suggested by Ben Michaud! Thanks!