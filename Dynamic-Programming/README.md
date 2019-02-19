# Dynamic Programming Solutions for Reinforcement Learning

**The Problem Definition**

We have 3 x 4 grid. The grid has the following

- Start(S): Denotes the starting state of agent
- Block(B): The state is not reachable, that is, blocked
- Positive Goal(+G): The state where you get max reward, +1 in our case
- Negative Goal(-G): The state where you do not want your agent to end up, reward of -1 in our case

Apart from these in some algorithms we have -0.1 of rewared for each step agents take. We make it negative so that the agent not only finds the path to GOAL but also the shortest path.

|   |   |   |+G |
|   |B  |   |-G |
| S |   |   |   |

1. [Policy Evaluation](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/policyevaluation.py): Given the policy, which can be deterministic or random we get the value function.

    Random Policy: In case of random policy each state would be equally likely so we give all the state equal probability

    Deterministic Policy: In deterministic policy if we want to go up, we will end up going up. That means the actions is as per our desire. In this case the probability will be 1.

    So for both types of policies we find the value function. The code can be found [here](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/policyevaluation.py)

    ![Cumulative Average](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/iterative_policy_evaluation.JPG?raw=true)


