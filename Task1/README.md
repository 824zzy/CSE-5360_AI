# Task 1

## Student Information

`Name`: Zhengyuan Zhu
`UTA ID`: 1001778274

## Program Information

1. `Programming Language`: Python3
2. `The structure of code`:
   1. `data/`: Store the test data of input and heuristic, image as well.
   2. `find_route.py`: the main entrance for the task.
   3. `opts.py`: the command line arguments are defined here.
   4. `utils.py`: helper function and base class.

## How to run the code

1. Jump to this directory: `cd [your_path]/Task1`
2. With heuristic information:
   - `python find_route.py input1.txt Bremen Kassel h_kassel.txt`
3. Without heuristic information:
   - `python find_route.py input1.txt Bremen Kassel`
4. If you want to see the details of process:
   - `python find_route.py input1.txt Bremen Kassel --printLog`

## Task 1 description

![Visual representation of input1.txt](./data/visual_representation.gif)
Implement a search algorithm that can find a route between any two cities. Your program will be called find_route, and will take exactly commandline arguments as follows:

`find_route input_filename origin_city destination_city heuristic_filename`

An example command line is:

`find_route input1.txt Bremen Kassel (For doing Uninformed search)`
or
`find_route input1.txt Bremen Kassel h_kassel.txt (For doing Informed search)`

If heuristic is not provided then program must do uninformed search. Argument input_filename is the name of a text file such as input1.txt, that describes road connections between cities in some part of the world. For example, the road system described by file input1.txt can be visualized in Figure 1 shown above. You can assume that the input file is formatted in the same way as input1.txt: each line contains three items. The last line contains the items "END OF INPUT", and that is how the program can detect that it has reached the end of the file. The other lines of the file contain, in this order, a source city, a destination city, and the length in kilometers of the road connecting directly those two cities. Each city name will be a single word (for example, we will use New_York instead of New York), consisting of upper and lowercase letters and possibly underscores.

**IMPORTANT NOTE:** MULTIPLE INPUT FILES WILL BE USED TO GRADE THE ASSIGNMENT, FILE input1.txt IS JUST AN EXAMPLE. YOUR CODE SHOULD WORK WITH ANY INPUT FILE FORMATTED AS SPECIFIED ABOVE.

The program will compute a route between the origin city and the destination city, and will print out both the length of the route and the list of all cities that lie on that route. It should also display the number of nodes expanded, nodes generated and max number of nodes in the fringe. For example,

find_route input1.txt Bremen Kassel

should have the following output:

``` latex
nodes expanded: 12
nodes generated: 19
max nodes in memory: 11
distance: 297.0 km
route:
Bremen to Hannover, 132.0 km
Hannover to Kassel, 165.0 km
```

and

find_route input1.txt London Kassel

should have the following output:

nodes expanded: 7
nodes generated: 6
max nodes in memory: 3
distance: infinity
route:
none

For full credit, you should produce outputs identical in format to the above two examples.

If a heuristic file is provided then program must perform Informed search. The heuristic file gives the estimate of what the cost could be to get to the given destination from any start state (note this is just an estimate). In this case the command line would look like

find_route inf input1.txt Munich Kassel h_kassel.txt

Here the last argument contains a text file what has the heuristic values for every state wrt the given destination city (note different destinations will need different heuristic values). For example, you have been provided a sample file h_kassel.txt which gives the heuristic value for every state (assuming kassel is the goal). Your program should use this information to reduce the number of nodes it ends up expanding. Other than that, the solution returned by the program should be the same as the uninformed version. For example,

find_route input1.txt Bremen Kassel h_kassel.txt

should have the following output:

``` latex
nodes expanded: 3
nodes generated: 7
max nodes in memory: 6
distance: 297.0 km
route:
Bremen to Hannover, 132.0 km
Hannover to Kassel, 165.0 km
```

## Suggestions

Pay close attention to all specifications on this page, including specifications about output format, submission format. Even in cases where the program works correctly, points will be taken off for non-compliance with the instructions given on this page (such as a different format for the program output, wrong compression format for the submitted code, and so on). The reason is that non-compliance with the instructions makes the grading process significantly (and unnecessarily) more time consuming.

## Grading

The assignments will be graded out of 50 points.
20 points: The program always finds a route between the origin and the destination, as long as such a route exists.
10 points: The program terminates and reports that no route can be found when indeed no route exists that connects source and destination (e.g., if source is London and destination is Berlin, in the above example).
10 points: In addition to the above requirements, the program always returns optimal routes. In other words, no shorter route exists than the one reported by the program.
10 points: Correct implementation of any informed search method.
Negative points: penalty points will be awarded by the instructor and TA generously and at will, for issues such as: code not running on omega, submission not including precise and accurate instructions for how to run the code, wrong compression format for the submission, or other failures to comply with the instructions given for this assignment. Partial credit for incorrect solutions will be given ONLY for code that is well designed and well documented. Code that is badly designed and badly documented can still get full credit as long as it accomplishes the required tasks.
