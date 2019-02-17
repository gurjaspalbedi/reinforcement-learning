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
        self.step_reward = 0
        self.rewards= np.full((self.rows * self.cols), self.step_reward)
        self.SMALL_CHANGE = 1e-3
        self.gamma = 1
        self.set_actions()
    
    def get_nearby_states(self, position: int):
        """To get the nearby state of any given state.
        This function is used to determine the moves adjacent to block position
        
        Parameters
        ----------
        position : int
            State number in the grid, 0 for (0,0) and 11 for (2,3)
        
        """
        left_state = position - 1 if position - 1 >=0 else None
        right_state = position + 1 if position + 1 < (self.rows * self.cols) else None
        up = position - self.cols if position - self.rows >=0 else None
        down = position + self.cols if position + self.rows < (self.rows * self.cols) else None

        return [{left_state : 'R'},{right_state: 'L'}, {up:'D'}, {down:'U'}]

    def set_actions_misc(self):
        """Function to set the actions for terminal states and blocked positions
        
        """
        states = self.get_terminal_states()
        for state in states:
            self.grid_world_actions[state] = []
        
        blocking_states = self.concrete_grid.block_positions
        for position in blocking_states:
            self.grid_world_actions[position] = []
            nearby_states = self.get_nearby_states(position)
            for nearby_state in nearby_states:
                if list(nearby_state.keys())[0] in self.grid_world_actions:
                    self.grid_world_actions[list(nearby_state.keys())[0]].remove(list(nearby_state.values())[0])
                    

    def set_actions(self) -> None:
        """Initialize actions for all the states
        
        Returns
        -------
        None
        """
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

        self.set_actions_misc()

    def print_actions(self) -> None:
        """To display the actions taken from each state, this is useful for the deterministic policy
        
        Returns
        -------
        None
        """
        actions = np.reshape(self.grid_world_actions, (self.rows,self.cols))
        for row in range(self.rows):
            for col in range(self.cols):
                print(actions[row][col], end=" ")
            print("")

    def get_reward(self, state_number: int):
        """Returns the reward associated witht the particular state
        
        Parameters
        ----------
        state_number : int
            State number for the particular state
        
        """
        if self.concrete_grid.is_positive_goal_position(state_number):
            return self.goal_reward
        
        if self.concrete_grid.is_negative_goal_position(state_number):
            return self.negative_goal_reward
        else:
            return self.step_reward

    def get_position(self,state_number: int) -> Tuple[int,int]:
        """Returns the position Tuple for the state number
        
        Parameters
        ----------
        state_number : int
            State number of the state for which we want position Tuple 
        
        Returns
        -------
        Tuple[int,int]
            Position Tuple of the state
        """
        return (state_number // self.cols , state_number % self.cols)


    def get_next_state_number(self, current_state_number: int, action: str ) -> int:
        """Given the state and action, returns the state number for the next state in which agent would be
        
        Parameters
        ----------
        current_state_number : int
            State number of the state in which the agent is currenly in
        action : str
            Action which the agent takes
        
        Returns
        -------
        int
            State number in which the agent would be after taking particular action
        """
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
        """Returns the reward for particular action in the given state
        
        Parameters
        ----------
        current_state_number : int
            State number of the current state in which agen is in
        action : str
            Action the agent takes from the current state
        
        Returns
        -------
        float
            Reward agent gets after taking give action from the current state
        """
        next_state_number  = self.get_next_state_number(current_state_number, action)
        return self.get_reward(next_state_number)
    
    def get_value_next_state(self, state_number: int, action: str) -> float: 
        """Gets the value function value for the given state
        
        Parameters
        ----------
        state_number : int
            State number of the agent
        action : str
            Action that agent takes
        
        Returns
        -------
        float
            The value of the state, which is the next state in this scenario
        """
        return self.value_function[self.get_next_state_number(state_number,action)]

    def get_terminal_states(self) -> List[int]:
        """Returns the list containing the state number of terminal states
        
        Returns
        -------
        List[int]
            The list containing the state number of the terminal states
        """
        return [self.concrete_grid.positive_goal, self.concrete_grid.negative_goal]

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
                actions = self.grid_world_actions[state]
                expected_value_sum = 0
                for action in actions:
                    expected_value_sum = expected_value_sum + (1/len(actions) * (self.get_action_reward(state,action) + (self.gamma * self.get_value_next_state(state,action))))
                self.value_function[state] = expected_value_sum
                max_expected_value_change = max(max_expected_value_change, np.abs(expected_value_sum - old_value_function))
            if max_expected_value_change <= self.SMALL_CHANGE:
                break

        self.concrete_grid.print_values(self.value_function)

    def set_deterministic_policy(self):
        #Policy : 
        # if we start from Start state we reach goal else we reach negative goal
        self.grid_world_actions[0] = ['R']
        self.grid_world_actions[1] = ['R']
        self.grid_world_actions[2] = ['R']
        self.grid_world_actions[3] = []
        self.grid_world_actions[4] = ['U']
        self.grid_world_actions[5] = []
        self.grid_world_actions[6] = ['R']
        self.grid_world_actions[8] = ['U']
        self.grid_world_actions[9] = ['R']
        self.grid_world_actions[10] = ['R']
        self.grid_world_actions[11] = ['U']


    def iterative_policy_evaluation_deterministic(self):
        self.gamma = 0.9
        self.set_deterministic_policy()
        self.concrete_grid.print_policy(self.grid_world_actions)
        # Policy evaluation for deterministic policy
        # Probability for any action will be 1 as there is only one action
        states = list(range(self.rows * self.cols))

        self.value_function = np.zeros((self.rows * self.cols))
        while True:
            # holds the maximum change 
            max_expected_value_change = 0
            for state in states:
                old_value_function = self.value_function[state]
                actions = self.grid_world_actions[state]
                for action in actions:
                    # Not taking sum because there will be only one action
                    # multiplying by 1 because there will be only one action and probability of that action will be 1
                    self.value_function[state] =  (1 * (self.get_action_reward(state,action)) + (self.gamma * self.get_value_next_state(state,action)))
                max_expected_value_change = max(max_expected_value_change, np.abs(self.value_function[state] - old_value_function))
            if max_expected_value_change < self.SMALL_CHANGE:
                break

        self.concrete_grid.print_values(self.value_function)

        

    