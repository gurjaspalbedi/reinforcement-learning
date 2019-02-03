from Environment import Environment
from Agent import Agent
from TicTacBoard import TicTacBoard
BOARD_SIZE = 3

agent1 = Agent(0.1 , 0.01 , 1 , BOARD_SIZE)
agent2 = Agent(0.1 , 0.01 , 2 , BOARD_SIZE)
tic_tac_board = TicTacBoard(BOARD_SIZE)

env = Environment(agent1, agent2, tic_tac_board)
env.run()



