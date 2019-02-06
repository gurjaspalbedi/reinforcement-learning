import numpy as np
from typing import Any, List
from TicTacBoard import TicTacBoard
ListInt1D = List[int]
ListInt2D = List[List[int]]
ListFloat1D = List[float]
class Agent:

    def __init__(self, exploration_rate: float, learning_rate: float, size: int, id: int):
        """Initializing the agent
        
        Parameters
        ----------
        exploration_rate : float
            This value tells the exploration percentage for the agent, Agent will explore for 10% of time if
            the value is 0.1
        learning_rate : float
            This is the rate at which the agent will learn
        size : int
            Size of the board in int
        id : int
            The identificaiton of the agent
        
        """
        self.agent_id = id
        self.exploration_rate = exploration_rate
        self.learning_rate = learning_rate
        self.moves = []
        self.size = size
        self.values_board = {}
        self.board_probabilities = np.array([0.5]* 9)

    def get_state_identifier(self, numerical_board: ListInt1D):
        """For each state we define it's identification by converting the values to base 3
        For each cell there can be three possible cases 0,1,2
        Buy using this strategy we can assign a number of base 3 to any state
        This function calculates that number given the state/board
        
        Parameters
        ----------
        numerical_board : ListInt1D
            These are the board values in 1D: eg: [0,1,0,2,0,0,2,0,2]
        
        """
        identifier = 0
        for i in range(self.size * self.size):
            identifier = identifier  + (numerical_board[i] * (3**(i)))
        return identifier

    def initialize_probability_board(self):
        """The probability board are the value function board.
        Higher value means that the agent is more confident about that move.
        
        """
        return np.array([0] * 9, dtype=float)

    def print_value_function(self, tic_board: ListFloat1D):
        """Function to print the value function values for each possible move
        If the value is zero that means the move is either invlaid or agent has zero confidence
        
        Parameters
        ----------
        tic_board : ListInt1D
            The board with value function values for each move
        
        """
        board_reshaped = tic_board.reshape(self.size, self.size)
        for i in range(self.size):
            for j in range(self.size):
                print(str(round(board_reshaped[i][j],3)), end = " ")
            print("")
        print("====================================================")

    def take_intelligent_move(self, board: ListInt1D, episode: int):
        """Function to take move based on the value funtion
        
        Parameters
        ----------
        board : list
            The current board state 
        iteration : int
            The episode of the RL algorithm
        
        """
        copy_board = np.copy(board)
        all_possible_moves =  np.argwhere(copy_board == 0).reshape(-1)
        max_value = -1
        intelligent_move = None
        confidence_values = self.initialize_probability_board()
        # Here we try to get the value from value function for each move
        # The agent takes the move that has the highert value
        for index in all_possible_moves:
            copy_board[index] = self.agent_id
            # Getting the unique identifier for the state/board, which is the value in base 3
            board_id = self.get_state_identifier(copy_board)

            #we already have the value then we take existing value otherwise 0.5, whic is the default value
            if board_id in self.values_board:
                value_for_this_move = self.values_board[board_id]
            else:
                value_for_this_move = 0.5
            
            # storing the confidence value by the agent for that particular move so that we can print these
            confidence_values[index] = value_for_this_move

            # Getting the index for which agent is most confident about
            if value_for_this_move > max_value:
                max_value = value_for_this_move
                intelligent_move = index

            # Reverting the move after calculating the confidence for that particular move
            # So that we can calculate confidence for other moves
            copy_board[index] = 0
        
        #print the probabilities for all possible moves
        if episode > 10000:
            # Function that prints the confidence values for all the possible moves
            self.print_value_function(np.copy(confidence_values))
        return intelligent_move

    def move_decision(self, current_board_state: ListInt1D, episode: int, human_play: int):
        """Function that helps agent take decision about the move
        
        Parameters
        ----------
        board : ListInt1D
            Current board state 
        episode : int
            The count of Reinforcement Learning Episode
        human_play : int
            After how many iterations the human will play
        
        """
        invalid_move = True
        # Value that will help us taking decision that we should explore or exploit
        value_from_distribution = np.random.rand()
        
        #exploration exploitation 
        if value_from_distribution < self.exploration_rate:
            if episode > human_play:
                print("Playing random move")

            # Looping until we get the valid move
            while(invalid_move):
                move = np.random.choice(np.arange(self.size * self.size))
                if current_board_state[move] == 0:
                    invalid_move = False
        else:
            # The case where we don't play a random move but intelligent one
            if episode > human_play:
                print("Playing intelligent move")
            move  = self.take_intelligent_move(current_board_state, episode)
        return move

    def make_move(self, current_board_state: ListInt1D , episode: int, human_play: int):
        """Function to make a move
        
        Parameters
        ----------
        current_board_state : ListInt1D
            1D list that represents the current state of board
        episode : int
            The current count of Reinforcement Learning episode
        human_play : int
            Afte how many iterations will the human play
        """
        if episode > human_play and self.agent_id == 1:
            # After 'human_play' episodes we play with the human
            invalid_move = True
            while(invalid_move):
                index = int(input("Please input the position you want\n 0 means first row first column\n 8 means the last row last column\n"))
                if current_board_state[index] == 0:
                    invalid_move = False
                else:
                    print("Invalid move!")
        else:
            # Below 'human_play' episodes playing with another agent
            index = self.move_decision(current_board_state , episode, human_play)
        if current_board_state[index] != 0:
            raise Exception("Invalid move by agent ", self.agent_id)
        current_board_state[index] = self.agent_id
        return current_board_state

    


