import numpy as np
class ValueIteration:

    def __init__(self, grid, policy, actions, small_change: float, gamma: float) -> None:
        self.grid = grid
        self.policy = policy
        self.actions = actions
        self.rows, self.cols = self.grid.grid_board.shape
        self.value_function = np.zeros((self.rows,self.cols))
        self.SMALL_CHANGE = small_change
        self.gamma = gamma
        self.actions.set_actions()
        self.initial_policy = self.policy.get_random_policy(self.rows, self.cols)
    
    def value_evaluation(self, states):
        # Get the best action
        max_value_change = 0
        for state in states:
            max_value = float('-inf')
            old_value_function = self.value_function[state]
            # DIFFERENCE BETWEEN POLICY ITERATION AND VALUE ITERATION
            # We value iteration as name suggest we try to find the maximum value for that state among all actions
            # But in case of Policy iteration we just evaluation the policy based on one actions that it holds
            # In Policy Iteration we assign this value for given policy to that state. But for Value Iteration
            # We assign the maximum value this state can have among all the actions
            for action in self.actions.grid_actions[state]:
                # multiplying by 1 because there will be only one action and probability of that action will be 1
                # That means if we try to go up, agent would end up going up, it is deterministic
                value =  (1 * (self.actions.get_action_reward(state,action)) + (self.gamma * self.value_function[self.actions.get_next_state_number(state,action)]))
                if value > max_value:
                    max_value = value
            self.value_function[state] = 0 if max_value == float('-inf') else max_value
            
            max_value_change = max(max_value_change, np.abs(self.value_function[state] - old_value_function))
  
        
        return max_value_change
    
    def get_best_action(self,state, actions):
        best_action_value = float('-inf')
        best_action = None
        for action in actions:
            probability = 1
            reward = self.actions.get_action_reward(state,action)
            next_state_value = self.value_function[self.actions.get_next_state_number(state,action)]
            value =  (probability * reward) + (self.gamma * next_state_value ) 
            if value > best_action_value:
                best_action_value = value
                best_action = action     
        return best_action

    def run_value_iteration(self):

        print("Random Policy")
        self.grid.print_policy(self.initial_policy)
        # Policy evaluation for deterministic policy
        # Probability for any action will be 1 as there is only one action
        states = list(range(self.rows * self.cols))
       
        self.value_function = np.zeros((self.rows * self.cols))
        # we continute doing policy iteration and policy improvement until policy stops improving
        while True:
            # holds the maximum change 
            max_expected_value_change = self.value_evaluation(states)
            if max_expected_value_change < self.SMALL_CHANGE:
                break

        # policy improvement phase
        # In policy improvement, we try to find other actions of each state that can have better value.
        # If we find any action for state that has better value than the current action, we update our policy to that action
        for state in states:
            actions  = self.actions.grid_actions[state]
            self.initial_policy[state] = self.get_best_action(state, actions)
        
        self.grid.print_values(self.value_function)
        self.grid.print_policy(self.initial_policy)



        