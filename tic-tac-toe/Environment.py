import numpy as np
from Agent import Agent
import TicTacBoard

class Environment:

    def __init__(self, agent1: Agent, agent2: Agent, tic_tac_board : TicTacBoard ):
        """Initializing the environment
        
        Parameters
        ----------
        agent1 : Agent
            The first agent that will play our game
        agent2 : Agent
            The second agent object that will play our game
        tic_tac_board : TicTacBoard
            The board class responsible for maintaining the board and printing the same.
        
        """
        self.agent1 = agent1
        self.agent2 = agent2
        self.tic_tac_board = tic_tac_board
        # Reward the agents get if they win
        self.winner_reward = 1
        # Reward the agents get if they lose
        self.losing_reward = 0
        # Otherwise reward
        self.average_reward = 0.5
        self.numerical_board = np.zeros(tic_tac_board.board_size * tic_tac_board.board_size, dtype=int)
        self.states = []

    def get_reshaped_board(self):
        """At places we are using 1D board and sometime we want 2D board
        So this function gets the current state board in 2D
        
        """
        return self.numerical_board.reshape( self.tic_tac_board.board_size, self.tic_tac_board.board_size)

    def get_row_winner(self):
        """This function return the winner in any row if exists, -1 otherwise
        
        """
        board = self.get_reshaped_board()
        for row in board:
            if np.all(row == 1):
                return 1
            if np.all(row == 2):
                return 2
        return -1
    
    def get_diagonal_winner(self):
        """Function to get the diagonal winner if any
        
        """
        board = self.get_reshaped_board()
        trans_diag = np.diag(np.fliplr(board))
        if (np.all(np.diag(board) == 1) or (np.all(trans_diag == 1))):
            return 1
        if (np.all(np.diag(board) == 2) or (np.all(trans_diag == 2))):
            return 2
        return -1

    def get_col_winner(self):
        """Function to ge the column winner if any
        
        """
        board = self.get_reshaped_board()
        for i in range(self.tic_tac_board.board_size):
            if np.all(board[:,i] == self.agent1.agent_id):
                return self.agent1.agent_id
            if np.all(board[:,i] ==  self.agent2.agent_id):
                return  self.agent2.agent_id
        return -1
    
    def board_is_full(self):
        """Function to check if the board is full
        
        """
        return not np.any((self.numerical_board) == 0)

    def get_winner(self):
        """Function that returns the winner of the game
        
        """
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
        """Returns if the game is draw of not.
        
        """
        return self.board_is_full()
    
    def update_value_function_for_agent(self, agent: Agent, reward: int):
        """Funtion that upates the value function for the agents
        
        Parameters
        ----------
        agent : Agent
            The agent for which the value function should be updated
        reward : int
            The reward that agents receive in that particular episode
        
        """
        target = reward
        # Updating the value function based on the following equation
        # V(S) = V(S) + learning_rate * (V(S' - V(S)))
        for state in reversed(agent.moves):
            prev = self.agent1.get_state_identifier(state)
            if prev in agent.values_board:
                value = agent.values_board[prev] + agent.learning_rate*(target - agent.values_board[prev])
            else:
                # In case we do not have value information or the state is new, take the average reward
                value = self.average_reward + agent.learning_rate * (target - self.average_reward)
            agent.values_board[prev] = value
            target = value
    
    def update_value_function(self, winner: int):
        """Functio to updat the value function for both the agenst
        
        Parameters
        ----------
        winner : int
            Denotes who is the winner.
        
        """
        reward1 = self.winner_reward if winner == self.agent1.agent_id else self.losing_reward
        reward2 = self.winner_reward if winner == self.agent2.agent_id else self.losing_reward
        self.update_value_function_for_agent(self.agent1, reward1)
        self.update_value_function_for_agent(self.agent2, reward2)

    def clear_agent_moves(self):
        """Clears the all moves save for both the agents
        
        """
        self.agent1.moves = []
        self.agent2.moves = []

    def clear_board(self):
        """Clears the board
        
        """
        self.numerical_board = np.zeros(self.tic_tac_board.board_size * self.tic_tac_board.board_size, dtype=int)

    def append_moves_for_agent(self):
        """Function to add the moves for both the agents
        
        """
        self.agent1.moves.append(np.copy(self.numerical_board))
        self.agent2.moves.append(np.copy(self.numerical_board))

    def run(self, episodes: int, human_play_after_count: int):
        """Running function of the algorithm
        
        Parameters
        ----------
        episodes : int
            Number of episodes we want in our Reinforcement Algorithm
        
        human_play_after_count: int
            After how many iterations human wants to play
        """
        for iteration in range(episodes):
            prev_played = self.agent1.agent_id
            winner = -1
            draw = False
            while(winner == -1 and not draw):

                if prev_played == self.agent1.agent_id:
                    prev_played = self.agent2.agent_id
                    self.numerical_board = self.agent2.make_move(self.numerical_board, iteration, human_play_after_count)
                else:
                    prev_played = self.agent1.agent_id
                    self.numerical_board = self.agent1.make_move(self.numerical_board, iteration, human_play_after_count)

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

    def print_winner(self, episode: int, winner: int, draw: bool):
        """Function that prints results of the episode
        
        Parameters
        ----------
        episode : int
            The episode of RL algorithm
        winner : int
            Id of the agen who won the episode
        draw : bool
            Flag to know if the episode resulted in draw or not
        
        """
        if episode > 10000:
            if (winner != -1):
                print("Winner is " + str(winner))
            if (draw):
                print("Draw")
        