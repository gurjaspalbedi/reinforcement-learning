# Dynamic Programming Solutions for Reinforcement Learning

**The Problem Definition**

We have 3 x 4 grid. The grid has the following

- Start(S): Denotes the starting state of agent
- Block(B): The state is not reachable, that is, blocked
- Positive Goal(+G): The state where you get max reward, +1 in our case
- Negative Goal(-G): The state where you do not want your agent to end up, reward of -1 in our case

Apart from these in some algorithms we have -0.1 of rewared for each step agents take. We make it negative so that the agent not only finds the path to GOAL but also the shortest path.

![Policy Evaluation](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/grid.png?raw=true)

1. [Policy Evaluation](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/policyevaluation.py): Given the policy, which can be deterministic or random we get the value function.

    Random Policy: In case of random policy each state would be equally likely so we give all the state equal probability

    Deterministic Policy: In deterministic policy if we want to go up, we will end up going up. That means the actions is as per our desire. In this case the probability will be 1. We define our deterministic policy as : If we start from START position we end in POSITIVE GOAL else in NEGATIVE GOAL STATE

    So for both types of policies we find the value function. The code can be found [here](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/policyevaluation.py)

    ![Policy Evaluation](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/iterative_policy_evaluation.JPG?raw=true)

2. [Policy Iteration](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/policyiteration.py)

    In policy iteration first we take the action from existing policy(randomly initialized) for each state, then we evaluate that policy and assign the new value to the existing value of that state.

    In second step, for each state we get the best action according to the existing policy and update the existing policy. We keep on doing these steps until we find no change in the policies.
    
     ![Policy Iteration](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/policyiteration.JPG?raw=true)
    

3. [Value Iteration](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/valueiteration.py)

    In Value iteration we simply get the best action for each state and assign to the value of that state. In improvement phase we simply get the best action for each state and assign to the policy.
    
     ![Value Iteration](https://github.com/gurjaspalbedi/reinforcement-learning/blob/master/Dynamic-Programming/valueiteration.JPG?raw=true)

**How to run?**

    You can run the code by running Main.py and uncommenting the algorithm you want to run.
