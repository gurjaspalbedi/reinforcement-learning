**TIC-TAC-TOE with Reinforcement Learning**

This reinforcement learning algortihm is explained below:

1. **Value function** : For each episode we update the confidence for each state in episode by the following formula.

    V(S) = V(S) + (learning_rate * (V(S) - V(S'))) 

2. **Initial Confidence Values:** We give value of 0.5 initially for all the moves if information about that move is not available. This may happen if the agent has never visited the state. By default the winning reward is 1 and losing reward is 0, 0.5 if the game results in draw.
   
You can run the progam by running the Main.py file.

