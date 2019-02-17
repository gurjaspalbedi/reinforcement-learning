from typing import List, Type, Tuple
import numpy as np
Point = Tuple[int,int]
Grid = List[List[int]]

class ConcreateGrid:

    def __init__(self, rows: int, cols: int) -> None:
        self.grid = np.zeros((rows,cols))
        self.rows: int = rows
        self.cols: int = cols
        self.postive_goal: Point = None
        self.negative_goal: Point = None
        self.start_position: Point = None

    def set_goal_position(self, pos: Point) -> None:
        self.postive_goal = pos

    def set_negative_goal_position(self, pos: Point) -> None:
        self.negative_goal = pos

    def set_start_position(self, pos: Point) -> None:
        self.start_position = pos
    
    def is_positive_goal_position(self, row: int, col: int) -> bool:
        return row == self.postive_goal[0] and col == self.postive_goal[1]
    
    def is_negative_goal_position(self, row: int, col: int) -> bool:
        return row == self.negative_goal[0] and col == self.negative_goal[1]
    
    def is_start_position(self, row: int, col: int) -> bool:
        return row == self.start_position[0] and col == self.start_position[1]

    def show_grid_positions(self) -> None:
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_positive_goal_position(row, col):
                    print("G", end=" ")
                elif self.is_negative_goal_position(row, col):
                    print("N", end=" ")
                elif self.is_start_position(row,col):
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


