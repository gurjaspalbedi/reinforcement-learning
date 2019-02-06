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
        self.states = []

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
    
    def update_value_function_for_agent(self, agent: Agent, reward):

        target = reward
        for state in reversed(agent.moves):
            prev = self.agent1.get_state_identifier(state)
            # if agent.agent_id == 1:
            #     print("agent 1 move")
            #     print(prev)
            if prev in agent.values_board:
                value = agent.values_board[prev] + agent.learning_rate*(target - agent.values_board[prev])
            else:
                value = self.average_reward + agent.learning_rate * (target - self.average_reward)
            agent.values_board[prev] = value
            target = value
        # if agent.agent_id == 1:
        #     print("for agent 1")
        #     print(len(agent.values_board))
        # if agent.agent_id == 2:
        #     print("for agent 2")
        #     print(len(agent.values_board))
    
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

    def append_moves_for_agent(self):
        self.agent1.moves.append(np.copy(self.numerical_board))
        self.agent2.moves.append(np.copy(self.numerical_board))

    def run(self, iterations):
        for iteration in range(iterations):
            prev_played = 1
            winner = -1
            draw = False
            while(winner == -1 and not draw):

                if prev_played == 1:
                    prev_played =2
                    self.numerical_board = self.agent2.make_move(self.numerical_board, iteration)
                else:
                    prev_played = 1
                    self.numerical_board = self.agent1.make_move(self.numerical_board, iteration)

                if iteration > 10000:
                    self.tic_tac_board.print_board(self.numerical_board)
                self.append_moves_for_agent()
                winner = self.get_winner()
                if (winner == -1):
                    draw = self.get_draw_status()
            # print("winner", iteration)
            self.update_value_function(winner)
            self.clear_board()
            self.clear_agent_moves()
            self.print_winner(iteration, winner, draw)
            
        print("All iterations complete")

    def print_winner(self, iteration, winner, draw):
        if iteration > 10000:
            if (winner != -1):
                print("Winner is " + str(winner))
            if (draw):
                print("Draw")
        