import numpy as np
from typing import Any
from TicTacBoard import TicTacBoard

class Agent:

    def __init__(self, exploration_rate: float, learning_rate: float, number: int, size: int):
        self.exploration_rate = exploration_rate
        self.learning_rate = learning_rate
        self.state_history = []
        self.number = number
        self.size = size
        self.values_board = np.zeros((size, size))

    def move_decision(self, board):
        invalid_move = True
        while(invalid_move):
            move = np.random.choice(np.arange(self.size * self.size))
            if board[move] == 0:
                invalid_move = False
        return move

    def make_move(self, numerical_board):
        index = self.move_decision(numerical_board)
        if numerical_board[index] != 0:
            raise Exception("Invalid move by agent " + self.number)
        numerical_board[index] = self.number
        return numerical_board




