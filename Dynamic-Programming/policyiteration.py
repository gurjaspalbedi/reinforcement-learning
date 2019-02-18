import numpy as np
class PolicyIteration:

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
    
    def run_policy_iteration(self):

        print("Random Policy")
        self.grid.print_policy(self.initial_policy)
        # Policy evaluation for deterministic policy
        # Probability for any action will be 1 as there is only one action
        states = list(range(self.rows * self.cols))
        # we stop if we have 10 iterations under which the policy doesn't improve
        count = 0
        self.value_function = np.zeros((self.rows * self.cols))
        # we continute doing policy iteration and policy improvement until policy stops improving
        while True:
            # policy evaluation phase
            # In our random policy we have one action for each state.
            # For that action we do policy evaluation and we get value function of state which we store
            # we do this for all the states
            while True:
                # holds the maximum change 
                max_expected_value_change = 0
                for state in states:
                    old_value_function = self.value_function[state]
                    action = self.initial_policy[state]
                    if action in self.actions.grid_actions[state]:
                        # Not taking sum because there will be only one action
                        # multiplying by 1 because there will be only one action and probability of that action will be 1
                        # That means if we try to go up, agent would end up going up, it is deterministic
                        self.value_function[state] =  (1 * (self.actions.get_action_reward(state,action)) + (self.gamma * self.value_function[self.actions.get_next_state_number(state,action)]))
                        max_expected_value_change = max(max_expected_value_change, np.abs(self.value_function[state] - old_value_function))
                if max_expected_value_change < self.SMALL_CHANGE:
                    break

            # policy improvement phase
            # In policy improvement, we try to find other actions of each state that can have better value.
            # If we find any action for state that has better value than the current action, we update our policy to that action
            for state in states:
                old_policy = self.initial_policy.copy()
                best_action_value = float('-inf')
                actions  = self.actions.grid_actions[state]
                best_action = None
                for action in actions:
                    probability = 1
                    reward = self.actions.get_action_reward(state,action)
                    next_state_value = self.value_function[self.actions.get_next_state_number(state,action)]
                    value =  (probability * reward) + (self.gamma * next_state_value ) 
                    if value > best_action_value:
                        best_action_value = value
                        best_action = action
                self.initial_policy[state] = best_action 
            # The number of time the policy remains same. It it is 10 we assume that it has converged
            if np.all(old_policy == self.initial_policy):
                count += 1
            if count == 10:
                break
        
        self.grid.print_values(self.value_function)
        self.grid.print_policy(self.initial_policy)



        