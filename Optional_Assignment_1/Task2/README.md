# Task 2 (50 points)

## Student Infomation

Name: Zhu Zhengyuan
UTAID: 1001778274

------------------

The task in this programming assignment is to design appropriate descriptions of facts, actions, and goals, using the PDDL language, for two planning problems: the [Tower of Hanoi problem](http://en.wikipedia.org/wiki/Tower_of_Hanoi), and the 7-puzzle problem (a variation of the 8-puzzle problem where two squares are clear instead of one). You will use your descriptions as inputs to a Graphplan implementation. If your descriptions are correct, Graphplan will produce appropriate plans.

### Compiling and Running the Software

The Graphplan software can be downloaded from [graphplan.zip](optassmt1_files/graphplan.zip). See the README file in that package for additional information. To compile the software on omega, unzip the directory, and, from that directory, type

make graphplan  

Once the program compiles, it can be invoked from the commandline as follows:

graphplan -o \[operators\_file\] -f \[facts\_file\]  

For example:

graphplan -o block\_ops.txt -f block\_facts3.txt  

*   Argument operators\_file specifies the location of a text file containing definitions of actions. For example, see [block\_ops.txt](optassmt1_filesblock_ops.txt) for definitions of actions appropriate for the blocks world.
*   Argument facts\_file specifies the location of a text file containing definitions of facts about the environment, including objects (and types for those objects), general predicates that are always true, initial state description, and goal description. For example, see [block\_facts2.txt](optassmt1_files/block_facts2.txt), [block\_facts3.txt](optassmt1_files/block_facts3.txt), and [block\_facts4.txt](optassmt1_files/block_facts4.txt) for example fact descriptions for the blocks world.

Once you start running the software, it will ask you three questions. Just hit enter for each question, so as to use the default settings. If your descriptions of actions and facts are correct, the program will print out a plan achieving the stated goal.

Note that the preconds in each fact file will contain both statements that are always true in that domain (i.e., in the Tower of Hanoi domain or the 7-puzzle domain), and statements that simply describe the initial state for that specific planning problem. In addition to the facts files for the specific planning problems you are given, you will have to create a separate text file that includes all the statements that must be present in ANY facts file for that domain.

### Tower of Hanoi Description

A description of the Tower of Hanoi domain can be found at [Wikipedia](http://en.wikipedia.org/wiki/Tower_of_Hanoi). In all problems that your program will be tested with there will be five discs (called disk1, disk2, disk3, disk4, disk5) and three pegs (called A, B, C). In all your facts files you will have to include both a common part (defining objects and relations among objects) and a plan-specific part (describing the initial state and goal for each plan). Note that some of the five disks may not appear in some of the planning problems.

The two planning problems you have to solve are:

**Problem 1**

initial state:  
(on disk1 disk2)  
(on disk2 A)   
(clear disk1)  
(clear B)  
(clear C)   
  
goal:  
(on disk1 B)  
(on disk2 C)

**Problem 2**

initial state:  
(on disk1 disk2)   
(on disk2 disk3)  
(on disk3 disk4)  
(on disk4 disk5)  
(on disk5 C)   
(clear disk1)   
(clear A)   
(clear B)  
  
goal:  
(on disk1 disk2)   
(on disk2 disk3)  
(on disk3 disk4)  
(on disk4 disk5)  
(on disk5 A)   

### 7-puzzle Description

7-puzzle is like 8-puzzle, except that there are only pieces numbered from 1 to 7 (not from 1 to 8), and there are two clear squares on the board. At any move, we can move a numbered piece to an adjacent clear square.

The two planning problems you have to solve are (X indicates a clear square):

**Problem 1**

initial state:  
12X  
356  
4X7  
  
goal:  
123  
456  
7XX

**Problem 2**

initial state:  
XX7  
654  
321  
  
goal:  
123  
456  
7XX  

### Grading

This task will be graded for 50 points. Half the points will correspond to your solutions for the Tower of Hanoi world, and the rest will correspond to your solutions for the 7-puzzle problem. Specifically, the point allocation is:

*   32 points: defining facts and actions correctly. The language that you define (i.e., the actions, objects, and general statements that are always true) should be sufficient not only for the specific plans that you are required to construct, but also for any other planning problems that we can define in the Tower of Hanoi domain or the 7-puzzle domain. As part of grading, we will also test your solutions on planning problems that we will make up.
*   18 points: solving the planning problems you are given (two for the Tower of Hanoi domain, two for the 7-puzzle domain) + 1 additional problem per domain. You get 3 points for each problem. If you solve all 6 correctly, you get 18 points.
