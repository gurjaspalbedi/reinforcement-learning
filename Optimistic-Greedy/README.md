# Optimistic-Greedy Implementation

In this program we assume that we have four slot machines with following mean rewards:

 1. Machine 1 - Mean reward of 1
 2. Machine 2 - Mean reward of 20
 3. Machine 3 - Mean reward of 30
 4. Machine 4 - Mean reward of 40

The below shown graph depicts how this is different then Greedy-Epsilon, as this doesn't explores but only exploits. These two graphs show the difference between the two algorithms.

Greedy-Epsilon

![Greedy-Epsilon](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Greedy-Epsilon/line_graph.png?raw=true)

Optimistic-Greedy

![Optimistic-Greedy](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Optimistic-Greedy/line_graph.png?raw=true)

File Details:

 - Main.py - File that contains the main function from where we run the algorithm by initializing the machines.
 - SlotMachine.py  - Contains the class that can instantiate Slot Machines
 - Optimistic.py - Contains the code for the algorithm
Running Program: Just run Main.py python file.