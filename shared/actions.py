import numpy as np

class Actions:

    def __init__(self, states_and_blockers, rewards, grid):
        self.states_and_blockers = states_and_blockers
        self.rewards = rewards
        self.grid = grid

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
        row, col = self.grid.get_position(current_state_number)
        if action == 'R':
            col = col + 1
        if action == 'L':
            col = col -1
        if action == 'U':
            row = row - 1
        if action == 'D':
            row = row + 1
        return self.grid.get_state_number(row, col)

    def set_actions_misc(self):
        """Function to set the actions for terminal states and blocked positions
        
        """
        states = self.grid.state_and_blocks.get_terminal_states()
        for state in states:
            self.grid_actions[state] = []
        
        blocking_states = self.grid.state_and_blocks.blocking_states
        for position in blocking_states:
            self.grid_actions[position] = []
            nearby_states = self.grid.get_nearby_states(position)
            for nearby_state in nearby_states:
                if list(nearby_state.keys())[0] in self.grid_actions:
                    self.grid_actions[list(nearby_state.keys())[0]].remove(list(nearby_state.values())[0])
                    
    def set_actions(self) -> None:
        """Initialize actions for all the states
        
        Returns
        -------
        None
        """
        rows, cols = self.grid.grid_board.shape
        self.grid_actions = {}
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                actions = []
                if row > 0:
                    actions.append('U')
                if row < rows - 1:
                    actions.append('D')
                if col > 0:
                    actions.append('L')
                if col < cols - 1:
                    actions.append('R')
                state = self.grid.get_state_number(row,col)
                self.grid_actions[state]= actions

        self.set_actions_misc()
    
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
        return self.rewards.get_reward(next_state_number)
    