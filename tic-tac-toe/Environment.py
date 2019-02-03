import numpy as np
from Agent import Agent
import TicTacBoard

class Environment:

    def __init__(self, agent1: Agent, agent2: Agent, tic_tac_board : TicTacBoard ):
        self.agent1 = agent1
        self.agent2 = agent2
        self.tic_tac_board = tic_tac_board
        self.numerical_board = np.zeros(tic_tac_board.board_size * tic_tac_board.board_size, dtype=int)

    def get_reshaped_board(self):
        return self.numerical_board.reshape( self.tic_tac_board.board_size, self.tic_tac_board.board_size)
    
    def get_row_winner(self):
        board = self.get_reshaped_board()
        if np.all(board) == 1:
            return 1
        if np.all(board) == 2:
            return 2
        return -1
    
    def get_diagonal_winner(self):
        board = self.get_reshaped_board()
        if (np.all(np.diag(board)) == 1 or (np.all(np.diag(np.transpose(board)) == 1))):
            return 1
        if (np.all(np.diag(board)) == 2 or (np.all(np.diag(np.transpose(board)) == 2))):
            return 2
        return -1

    def get_col_winner(self):
        board = self.get_reshaped_board()
        for i in range(self.tic_tac_board.board_size):
            if np.all(board[:,i]) == 1:
                return 1
            if np.all(board[:,i]) == 2:
                return 2
        return -1
    
    def board_is_full(self):
        return not ((self.numerical_board) == 0).any()

    def get_winner(self):
        winner = self.get_diagonal_winner()
        winner = self.get_col_winner()
        winner = self.get_row_winner()
        return winner
    
    def get_draw_status(self):
        return self.board_is_full()
    
    def run(self):
        prev_played = 1
        winner = -1
        draw = False
        while(winner == -1 and draw == False):
            if prev_played == 1:
                prev_played =2
                self.numerical_board = self.agent2.make_move(self.numerical_board)
                self.tic_tac_board.print_board(self.numerical_board)
            else:
                prev_played = 1
                self.numerical_board = self.agent1.make_move(self.numerical_board)
                self.tic_tac_board.print_board(self.numerical_board)
            winner = self.get_winner()
            if (winner == -1):
                draw = self.get_draw_status()
        if (winner != -1):
            print("Winner is " + winner)
        if (draw):
            print("Draw")
        