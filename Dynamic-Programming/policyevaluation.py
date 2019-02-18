import numpy as np
from typing import List, Tuple
import torch
import pylab as plt

class PolicyEvaluation:

    def __init__(self, grid, policy, actions, small_change, gamma) -> None:
        self.grid = grid
        self.policy = policy
        self.actions = actions
        self.rows, self.cols = self.grid.grid_board.shape
        self.value_function = np.zeros((self.rows,self.cols))
        self.SMALL_CHANGE = small_change
        self.gamma = gamma
        self.actions.set_actions()

    def iterative_policy_evaluation(self):
        # First we do the policy evaluation for random policy.
        # For Random policy all states are equally likely so the probability would be
        # 1/ (No. of states in that policy)

        states = list(range(self.rows * self.cols))

        self.value_function = np.zeros((self.rows * self.cols))
        while True:
            # we iterate through all the states, for each state select action and sum there values.
            # this summation of values for each action multiplied by probability is known as expectation of that state
            # This expectation is then assigned to that particular state.
            # This process is continued untile we find very small change between two iterations for particular state.
            max_expected_value_change = 0
            for state in states:
                old_value_function = self.value_function[state]
                actions = self.actions.grid_actions[state]
                expected_value_sum = 0
                for action in actions:
                    expected_value_sum = expected_value_sum + (1/len(actions) * (self.actions.get_action_reward(state,action) + (self.gamma * self.value_function[self.actions.get_next_state_number(state,action)])))
                self.value_function[state] = expected_value_sum
                max_expected_value_change = max(max_expected_value_change, np.abs(expected_value_sum - old_value_function))
            if max_expected_value_change <= self.SMALL_CHANGE:
                break

        self.grid.print_values(self.value_function)

    def set_deterministic_policy(self):
        #Policy : 
        # if we start from Start state we reach goal else we reach negative goal
        self.actions.grid_actions= self.policy.set_deterministic_policy(self.actions.grid_actions)


    def iterative_policy_evaluation_deterministic(self):
        self.gamma = 0.9
        self.set_deterministic_policy()
        self.grid.print_policy(self.actions.grid_actions)
        # Policy evaluation for deterministic policy
        # Probability for any action will be 1 as there is only one action
        states = list(range(self.rows * self.cols))

        self.value_function = np.zeros((self.rows * self.cols))
        while True:
            # holds the maximum change 
            max_expected_value_change = 0
            for state in states:
                old_value_function = self.value_function[state]
                actions = self.actions.grid_actions[state]
                for action in actions:
                    # Not taking sum because there will be only one action
                    # multiplying by 1 because there will be only one action and probability of that action will be 1
                    self.value_function[state] =  (1 * (self.actions.get_action_reward(state,action)) + (self.gamma * self.value_function[self.actions.get_next_state_number(state,action)]))
                max_expected_value_change = max(max_expected_value_change, np.abs(self.value_function[state] - old_value_function))
            if max_expected_value_change < self.SMALL_CHANGE:
                break

        self.grid.print_values(self.value_function)

        

    