from typing import List, Type, Tuple
import numpy as np
Board = List[List[int]]

class Grid:

    def __init__(self, rows: int, cols: int, state_and_blocks) -> None:
        self.grid_board = np.zeros((rows,cols))
        self.rows: int = rows
        self.cols: int = cols
        self.state_and_blocks = state_and_blocks

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

    def show_grid_positions(self) -> None:
        """Function to print the Goals, Negative Goals, Block positions and Start position
        
        Returns
        -------
        None
        """
        for row in range(self.rows):
            for col in range(self.cols):
                state_number = self.get_state_number(row,col)
                if state_number in self.state_and_blocks.positive_terminal_states:
                    print("|G|", end=" ")
                elif state_number in self.state_and_blocks.negative_terminal_states:
                    print("|N|", end=" ")
                elif state_number in self.state_and_blocks.starting_states:
                    print("|S|", end=" ")
                elif state_number in self.state_and_blocks.blocking_states:
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
        if type(policy) is dict:
            grid = np.array(list(policy.values())).reshape(self.rows,self.cols)
        else:
            grid = policy.reshape(self.rows,self.cols)
        shape = grid.shape
        rows = shape[0]
        cols = shape[1]
        for row in range(rows):
            print("----------------------------------------------")
            for col in range(cols):
                print(" ", grid[row][col][0], end=" |") if len(grid[row][col]) > 0 else print("   ", end=" |")
            print("")
        print("\n")

