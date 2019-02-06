**TIC-TAC-TOE with Reinforcement Learning**

This reinforcement learning algortihm is explained below:

1. **Value function** : For each episode we update the confidence for each state in episode by the following formula.

    V(S) = V(S) + (learning_rate * (V(S) - V(S'))) 

2. **Initial Confidence Values:** We give value of 0.5 initially for all the moves if information about that move is not available. This may happen if the agent has never visited the state. By default the winning reward is 1 and losing reward is 0, 0.5 if the game results in draw.
   
You can run the progam by running the Main.py file.

Below is the screen shot of the initial value function. We can see that on the first move agent is most confident to place the stone in the middle of the board. Confidence value of that position is **0.903**

**1** Denotes the move by Agent1
**2** Denotes the move by Agent2
**0** Denotes the empty place

![Value Function](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/tic-tac-toe/initial_confidence.JPG?raw=true)
