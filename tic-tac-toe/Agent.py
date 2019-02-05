import numpy as np
from typing import Any
from TicTacBoard import TicTacBoard

# class State:
#     def __init__(self):
#         self.stateNumber: int
#         self.stateValue: float

class Agent:

    def __init__(self, exploration_rate: float, learning_rate: float, number: int, size: int, id: int):
        self.agent_id = id
        self.exploration_rate = exploration_rate
        self.learning_rate = learning_rate
        self.moves = []
        self.number = number
        self.size = size
        self.values_board = {}
        self.board_probabilities = np.array([0.5]* 9)

    def get_state_identifier(self, numerical_board):
        identifier = 0
        for i in range(self.size):
            identifier = identifier  + (numerical_board[i] * (3**(i)))
        return identifier

    def initialize_probability_board(self):
        # index_non_zero = [board != 0]
        # # board_probabilities = np.copy(self.board_probabilities)
        # board_probabilities = np.copy(self.board_probabilities)
        # board_probabilities[index_non_zero] = 0
        return np.array([0] * 9, dtype=float)

    def print_board_probabilities(self,tic_board):
        board_reshaped = tic_board.reshape(self.size, self.size)
        for i in range(self.size):
            for j in range(self.size):
                print(str(round(board_reshaped[i][j],3)), end = " ")
            print("")
        print("====================================================")

    def take_intelligent_move(self, board, iteration: int):
        copy_board = np.copy(board)
        all_possible_moves =  np.argwhere(copy_board == 0).reshape(-1)
        max_value = 0
        intelligent_move = None
        local_board_probabilities = self.initialize_probability_board()
        for index in all_possible_moves:
            copy_board[index] = self.agent_id
            board_id = self.get_state_identifier(copy_board)
            if board_id in self.values_board:
                value_for_this_move = self.values_board[board_id]
            else:
                value_for_this_move = 0.5
            local_board_probabilities[index] = value_for_this_move
            if value_for_this_move > max_value:
                max_value = value_for_this_move
                intelligent_move = index
            copy_board[index] = 0
        if iteration > 10000:
            self.print_board_probabilities(np.copy(local_board_probabilities))
        return intelligent_move

    def move_decision(self, board, iteration):
        invalid_move = True
        value_from_distribution = np.random.rand()
        if value_from_distribution < self.exploration_rate:
            # if iteration > 10000:
            print("playing random move")
            while(invalid_move):
                move = np.random.choice(np.arange(self.size * self.size))
                if board[move] == 0:
                    invalid_move = False
        else:
            # if iteration > 10000:
            print("playing intelligent move")
            move  = self.take_intelligent_move(board, iteration)
        return move

    def make_move(self, numerical_board , iteration: int):
        # if iteration > 10000 and self.agent_id == 1:
        #     index = int(input("enter value"))
        # else:
        index = self.move_decision(numerical_board , iteration)
        if numerical_board[index] != 0:
            raise Exception("Invalid move by agent ", self.number)
        numerical_board[index] = self.number
        self.moves.append(np.copy(numerical_board))
        return numerical_board

    


