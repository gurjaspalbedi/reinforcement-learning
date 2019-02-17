import numpy as np
from typing import List, Tuple
import torch
import pylab as plt

class DynamicProgramming:

    def __init__(self, concrete_grid) -> None:
        self.concrete_grid = concrete_grid
        self.grid_world = concrete_grid.grid
        self.rows, self.cols = self.grid_world.shape
        self.value_function = np.zeros((self.rows,self.cols))
        self.goal_reward = 1
        self.negative_goal_reward = -1
        self.step_reward = -0.1
        self.rewards= np.full((self.rows * self.cols), self.step_reward)
        self.SMALL_CHANGE = 1e-3
        self.gamma = 1
        self.set_actions()
    
    def set_actions_terminal_states(self):
        states = self.get_terminal_states()
        for state in states:
            self.grid_world_actions[state] = []

    def set_actions(self) -> None:
        rows, cols = self.grid_world.shape
        self.grid_world_actions = {}
        for row in range(self.rows):
            for col in range(self.cols):
                actions = []
                if row > 0:
                    actions.append('U')
                if row < rows - 1:
                    actions.append('D')
                if col > 0:
                    actions.append('L')
                if col < cols - 1:
                    actions.append('R')
                state = self.concrete_grid.get_state_number(row,col)
                self.grid_world_actions[state]= actions

        self.set_actions_terminal_states()

    def print_actions(self) -> None:
        actions = np.reshape(self.grid_world_actions, (self.rows,self.cols))
        for row in range(self.rows):
            for col in range(self.cols):
                print(actions[row][col], end=" ")
            print("")

    def get_reward(self, state_number):
        if self.concrete_grid.is_positive_goal_position(state_number):
            return self.goal_reward
        
        if self.concrete_grid.is_negative_goal_position(state_number):
            return self.negative_goal_reward
        else:
            return self.step_reward

    def get_position(self,state_number) -> Tuple[int,int]:
        return (state_number // self.cols , state_number % self.cols)


    def get_next_state_number(self, current_state_number: int, action: str ) -> int:
        row, col = self.get_position(current_state_number)
        if action == 'R':
            col = col + 1
        if action == 'L':
            col = col -1
        if action == 'U':
            row = row - 1
        if action == 'D':
            row = row + 1
        return self.concrete_grid.get_state_number(row, col)

    def get_action_reward(self, current_state_number: int, action: str) -> float:
        next_state_number  = self.get_next_state_number(current_state_number, action)
        return self.get_reward(next_state_number)
    
    def get_value_next_state(self, state_number: int, action: str):
        return self.value_function[self.get_next_state_number(state_number,action)]

    def get_terminal_states(self) -> List[int]:
        print(self.concrete_grid.positive_goal)
        return [self.concrete_grid.positive_goal, self.concrete_grid.negative_goal]

    def iterative_policy_evaluation(self):
        # First we do the policy evaluation for random policy.
        # For Random policy all states are equally likely so the probability would be
        # 1/ (No. of states in that policy)

        # X = np.linspace(0,2,1000)
        # Y = X**2 + np.random.random(X.shape)

        # plt.ion()
        # graph = plt.plot(X,Y)[0]

        states = list(range(self.rows * self.cols))

        self.value_function = np.zeros((self.rows * self.cols))
        while True:
            max_expected_value_change = 0
            for state in states:
                # print("taking state",state)
                old_value_function = self.value_function[state]
                actions = self.grid_world_actions[state]
                print(len(actions))
                max_expected_value_change = 0
                expected_value_sum = 0
                for action in actions:
                    expected_value_sum = expected_value_sum + (1/len(actions) * (self.get_action_reward(state,action) + (self.gamma * self.get_value_next_state(state,action))))
                self.value_function[state] = expected_value_sum
                max_expected_value_change = max(max_expected_value_change, np.abs(expected_value_sum - old_value_function))
                # print("max expected value change", max_expected_value_change)
                # graph.set_ydata(max_expected_value_change)
                # plt.draw()
            if max_expected_value_change <= self.SMALL_CHANGE:
                break

        self.concrete_grid.print_values(self.value_function)

        

    