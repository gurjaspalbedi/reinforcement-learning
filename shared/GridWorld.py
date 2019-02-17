from typing import List, Type, Tuple
import numpy as np
Grid = List[List[int]]

class ConcreateGrid:

    def __init__(self, rows: int, cols: int) -> None:
        self.grid = np.zeros((rows,cols))
        self.rows: int = rows
        self.cols: int = cols
        self.positive_goal: int = None
        self.negative_goal: int = None
        self.start_position: int = None
        self.block_positions: List[int] = []

    def set_goal_position(self, state_number: int) -> None:
        """Sets the goal position for the grid
        
        Parameters
        ----------
        state_number : int
            State number which should be the goal position
        
        Returns
        -------
        None
        """
        self.positive_goal = state_number

    def set_negative_goal_position(self, state_number: int) -> None:
        """Sets the negative goal position of the grid
        
        Parameters
        ----------
        state_number : int
            State number that should be set as the negative goal position
        
        Returns
        -------
        None
        """
        self.negative_goal = state_number

    def set_start_position(self, state_number: int) -> None:
        """Sets the start position of the grid
        
        Parameters
        ----------
        state_number : int
            State number which should be the start position
        
        Returns
        -------
        None
        """
        self.start_position = state_number
    
    def set_block_positions(self, state_number_list: List[int]) -> None:
        """Sets the positions in the grid where agent can't move
        
        Parameters
        ----------
        state_number_list : List[int]
            The list containing the positions that should be blocked for the agent
        
        Returns
        -------
        None
        """
        self.block_positions = state_number_list
    
    def get_state_number(self, row: int ,col: int) -> int:
        """Get the state number for the given position
        
        Parameters
        ----------
        row : int
            Row for the position
        col : int
            Columns for the position
        
        Returns
        -------
        int
            State number of the given position
        """
        return ((row * self.cols) + (col))

    def is_positive_goal_position(self, state_number: int) -> bool:
        """Checks if the given state number is postitvie goal or not
        
        Parameters
        ----------
        state_number : int
            The state which we wan't to check if it is a goal position or not
        
        Returns
        -------
        bool
            True if it is goal state False otherwise
        """
        return self.positive_goal == state_number
    
    def is_negative_goal_position(self, state_number: int) -> bool:
        """Checks if the given state number is negative  goal or not
        
        Parameters
        ----------
        state_number : int
            State number that we want to check          
        
        Returns
        -------
        bool
            True if it is a negative state 
        """
        return self.negative_goal == state_number
    
    def is_start_position(self, state_number: int) -> bool:
        """Checks if given state is start position or not
        
        Parameters
        ----------
        state_number : int
            State number which we want to check
        
        Returns
        -------
        bool
            True if given state is start position
        """
        return self.start_position == state_number

    def show_grid_positions(self) -> None:
        """Function to print the Goals, Negative Goals, Block positions and Start position
        
        Returns
        -------
        None
        """
        for row in range(self.rows):
            for col in range(self.cols):
                state_number = self.get_state_number(row,col)
                if self.is_positive_goal_position(state_number):
                    print("|G|", end=" ")
                elif self.is_negative_goal_position(state_number):
                    print("|N|", end=" ")
                elif self.is_start_position(state_number):
                    print("|S|", end=" ")
                elif state_number in self.block_positions:
                    print("|X|", end=" ")
                else:
                    print("|O|", end=" ")
            print("")
        print("\n")
    
    def print_values(self, values: List[List[int]]) -> None:
        """Prints the value for each state
        
        Parameters
        ----------
        values : List[List[int]]
            Values for each state in 2D Array
        
        Returns
        -------
        None
        """
        grid = values.reshape(self.rows,self.cols)
        shape = grid.shape
        rows = shape[0]
        cols = shape[1]
        for row in range(rows):
            print("----------------------------------------------")
            for col in range(cols):
                print("| %.3f|" % grid[row][col], end=" ")
            print("")
        print("\n")

    def print_policy(self, policy: List[List[str]]) -> None:
        """Prints the policy which we are using in deterministic case
        
        Parameters
        ----------
        policy : List[List[str]]
            Given policy
        
        Returns
        -------
        None
        """
        grid = np.array(list(policy.values())).reshape(self.rows,self.cols)
        shape = grid.shape
        rows = shape[0]
        cols = shape[1]
        for row in range(rows):
            print("----------------------------------------------")
            for col in range(cols):
                print(" ", grid[row][col][0], end=" |") if len(grid[row][col]) > 0 else print("   ", end=" |")
            print("")
        print("\n")

