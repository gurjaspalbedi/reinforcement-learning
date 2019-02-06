from Environment import Environment
from Agent import Agent
from TicTacBoard import TicTacBoard

# store the board size      
BOARD_SIZE = 3

# After how many iteration human wants to play?
HUMAN_PLAY_AFTER_COUNT = 10000

# Total number of episodes we want to have
EPISODES = 10010

# Initializing the first agent with different parameters
agent1 = Agent(0.1 , 0.2 , BOARD_SIZE, 1)

# Initializing the second agent with different parameters
agent2 = Agent(0.1 , 0.2 , BOARD_SIZE, 2)

# The tic tac toe board object  
tic_tac_board = TicTacBoard(BOARD_SIZE)

# Initializing the environment
env = Environment(agent1, agent2, tic_tac_board)

# The run function that takes the number of episodes we want agents to play
env.run(EPISODES, HUMAN_PLAY_AFTER_COUNT)



