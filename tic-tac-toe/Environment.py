import numpy as np
from Agent import Agent
import TicTacBoard

class Environment:

    def __init__(self, agent1: Agent, agent2: Agent, tic_tac_board : TicTacBoard ):
        self.agent1 = agent1
        self.agent2 = agent2
        self.tic_tac_board = tic_tac_board
        self.winner_reward = 1
        self.losing_reward = 0
        self.average_reward = 0.5
        self.numerical_board = np.zeros(tic_tac_board.board_size * tic_tac_board.board_size, dtype=int)

    def get_reshaped_board(self):
        return self.numerical_board.reshape( self.tic_tac_board.board_size, self.tic_tac_board.board_size)

    def get_row_winner(self):
        board = self.get_reshaped_board()
        for row in board:
            if np.all(row == 1):
                return 1
            if np.all(row == 2):
                return 2
        return -1
    
    def get_diagonal_winner(self):
        board = self.get_reshaped_board()
        trans_diag = np.diag(np.fliplr(board))
        if (np.all(np.diag(board) == 1) or (np.all(trans_diag == 1))):
            return 1
        if (np.all(np.diag(board) == 2) or (np.all(trans_diag == 2))):
            return 2
        return -1

    def get_col_winner(self):
        board = self.get_reshaped_board()
        for i in range(self.tic_tac_board.board_size):
            if np.all(board[:,i] == 1):
                return 1
            if np.all(board[:,i] == 2):
                return 2
        return -1
    
    def board_is_full(self):
        return not np.any((self.numerical_board) == 0)

    def get_winner(self):
        winnerc = self.get_diagonal_winner()
        if winnerc != -1:
            return winnerc
        winnerd = self.get_col_winner()
        if winnerd != -1:
            return winnerd
        winnerr = self.get_row_winner()
        if winnerr != -1:
            return winnerr
        return -1
    
    def get_draw_status(self):
        return self.board_is_full()
    
    def get_state_value(self, state):
        pass
    
    # def get_all_moves(self, agent: int):
    #     if agent == 1:
    #         return self.agent1.moves
    #     return self.agent2.moves

    def update_value_function_for_agent(self, agent: Agent, reward):
        agent.moves.reverse()
        states = agent.moves
        value_board = agent.values_board
        target_reward = reward
        for state in enumerate(states):
            i = self.agent1.get_state_identifier(state[1])
            if i in value_board:
                agent.values_board[i] = value_board[i] + agent.learning_rate * (target_reward - value_board[i])
            else:
                agent.values_board[i] = self.average_reward + agent.learning_rate * (target_reward - self.average_reward)
            target_reward = value_board[i]
    
    def update_value_function(self, winner):
        reward1 = self.winner_reward if winner == 1 else self.losing_reward
        reward2 = self.winner_reward if winner == 2 else self.losing_reward
        self.update_value_function_for_agent(self.agent1, reward1)
        self.update_value_function_for_agent(self.agent2, reward2)

    def clear_agent_moves(self):
        self.agent1.moves = []
        self.agent2.moves = []

    def clear_board(self):
        self.numerical_board = np.zeros(self.tic_tac_board.board_size * self.tic_tac_board.board_size, dtype=int)

    def run(self, iterations):
        for iteration in range(iterations):
            # if iteration > 10000 or debug == 1:
            #     print("The current iteration is ", iteration)
            print("The current iteration is ", iteration)
            prev_played = 1
            winner = -1
            draw = False
            while(winner == -1 and draw == False):
                if prev_played == 1:
                    prev_played =2
                    # if iteration > 10000:
                    print("Agent playing ", 2)
                    self.numerical_board = self.agent2.make_move(self.numerical_board, iteration)
                    if iteration > 10000:
                        self.tic_tac_board.print_board(self.numerical_board)
                else:
                    prev_played = 1
                    # if iteration > 10000:
                    print("Agent playing ", 1)
                    self.numerical_board = self.agent1.make_move(self.numerical_board, iteration)
                    # if iteration > 10000:
                    self.tic_tac_board.print_board(self.numerical_board)
                # self.agent1.moves.append(np.copy(self.numerical_board))
                # self.agent2.moves.append(np.copy(self.numerical_board))
                winner = self.get_winner()
                if (winner == -1):
                    draw = self.get_draw_status()
            self.update_value_function(winner)
            self.clear_board()
            self.clear_agent_moves()
            # if iteration > 10000:
            if (winner != -1):
                print("Winner is " + str(winner))
            if (draw):
                print("Draw")
            
        print("All iterations complete")
        