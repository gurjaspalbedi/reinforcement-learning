#%%
import numpy as np
class TicTacBoard:

    def __init__(self, board_size):
        self.board_size = board_size
    
    def print_board(self, numerical_board):
        board = numerical_board.reshape(self.board_size, self.board_size)
        for i in range(self.board_size):
            for j in range(self.board_size):
                print('1', end=" " ) if board[i][j] == 1 else (print ("2" , end=" ") if board[i][j] == 2 else print("O", end=" " ))
            print("\n")
        print("_____________________________________________________")
    


    