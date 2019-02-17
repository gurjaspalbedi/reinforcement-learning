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
        self.positive_goal = state_number

    def set_negative_goal_position(self, state_number: int) -> None:
        self.negative_goal = state_number

    def set_start_position(self, state_number: int) -> None:
        self.start_position = state_number
    
    def set_block_positions(self, state_number_list: List[int]) -> None:
        self.block_positions = state_number_list
    
    def get_state_number(self, row,col):
        return ((row * self.cols) + (col))

    def is_positive_goal_position(self, state_number: int) -> bool:
        return self.positive_goal == state_number
    
    def is_negative_goal_position(self, state_number: int) -> bool:
        return self.negative_goal == state_number
    
    def is_start_position(self, state_number: int) -> bool:
        return self.start_position == state_number

    def show_grid_positions(self) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                state_number = self.get_state_number(row,col)
                if self.is_positive_goal_position(state_number):
                    print("G", end=" ")
                elif self.is_negative_goal_position(state_number):
                    print("N", end=" ")
                elif self.is_start_position(state_number):
                    print("S", end=" ")
                else:
                    print("O", end=" ")
            print("")
    
    def print_values(self, values: List[List[int]]) -> None:
        grid = values.reshape(self.rows,self.cols)
        shape = grid.shape
        rows = shape[0]
        cols = shape[1]
        for row in range(rows):
            for col in range(cols):
                print(" %.3f" % grid[row][col], end=" ")
            print("")


