# Greedy-Epsilon Implementation

In this program we assume that we have four slot machines with following mean rewards:

 1. Machine 1 - Mean reward of 1
 2. Machine 2 - Mean reward of 2
 3. Machine 3 - Mean reward of 3
 4. Machine 4 - Mean reward of 4
We take epsilon value of 0.1 that means that we our algorithms explores new options for the 10 % of the time and exploits remaining 90% of the time.
The Bar graph displaying how many times which machine was selected is as shown below

![Selection of Machines](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Greedy-Epsilon/BarGraph.jpg?raw=true)

If we give the mean rewards as 1, 10, 20, 30 and plot a graph of iteration vs reward we get the following plot.

![Iterations](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Greedy-Epsilon/line_graph.png?raw=true)

File Details:

 - Main.py - File that contains the main function from where we run the algorithm by initializing the machines.
 - SlotMachine.py  - Contains the class that can instantiate Slot Machines
 - GreedyEpsilon.py - Contains the code for the algorithm
