# Optimistic-Greedy Implementation

In this program we assume that we have four slot machines with following mean rewards:

 1. Machine 1 - Mean reward of 1
 2. Machine 2 - Mean reward of 20
 3. Machine 3 - Mean reward of 30
 4. Machine 4 - Mean reward of 40

The below shown graph depicts how this is different then Greedy-Epsilon, as this doesn't explores but only exploits. These two graphs show the difference between the two algorithms.

The Bar graph displaying how many times which machine was selected is as shown below

![Selection of Machines](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Optimistic-Greedy/bar_graph.jpg?raw=true)

If we give the mean rewards as 1, 10, 20, 30 and plot a graph of iteration vs reward we get the following plot.

![Iterations](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Optimistic-Greedy/line_graph.jpg?raw=true)

The graph for the cumulative average of awards vs number of iterations

![Cumulative Average](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Optimistic-Greedy/cumulative_average.jpg?raw=true)

File Details:

 - Main.py - File that contains the main function from where we run the algorithm by initializing the machines.
 - SlotMachine.py  - Contains the class that can instantiate Slot Machines
 - Optimistic.py - Contains the code for the algorithm
Running Program: Just run Main.py python file.
