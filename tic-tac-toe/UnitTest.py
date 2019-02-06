import unittest
import Environment
from Environment import Environment
from Agent import Agent
from TicTacBoard import TicTacBoard
import numpy as np

test = unittest.TestCase()
BOARD_SIZE = 3

agent1 = Agent(0.1 , 0.01 , BOARD_SIZE ,1)
agent2 = Agent(0.1 , 0.01 , BOARD_SIZE,2)
tic_tac_board = TicTacBoard(BOARD_SIZE)

env = Environment(agent1, agent2, tic_tac_board)

env.numerical_board = np.array([1,1,1,0,0,0,0,0,0])
test.assertEqual(env.get_row_winner(), 1)

env.numerical_board = np.array([0,0,0,2,2,2,0,0,0])
test.assertEqual(env.get_row_winner(), 2)

env.numerical_board = np.array([0,0,0,0,0,0,1,1,1])
test.assertEqual(env.get_row_winner(), 1)

env.numerical_board = np.array([1,0,0,0,1,0,1,1,1])
test.assertEqual(env.get_diagonal_winner(), 1)

env.numerical_board = np.array([1,0,0,0,0,0,1,1,1])
test.assertEqual(env.get_diagonal_winner(), -1)

env.numerical_board = np.array([0,0,1,0,1,0,1,0,0])
test.assertEqual(env.get_diagonal_winner(), 1)

env.numerical_board = np.array([2,0,1,2,1,0,2,0,0])
test.assertEqual(env.get_col_winner(), 2)

env.numerical_board = np.array([0,2,1,0,2,0,1,2,0])
test.assertEqual(env.get_col_winner(), 2)

env.numerical_board = np.array([0,0,2,0,2,2,1,2,2])
test.assertEqual(env.get_col_winner(), 2)

env.numerical_board = np.array([2,1,1,1,2,2,1,1,1])
test.assertEqual(env.get_draw_status(), True)

numerical_board = np.array([2, 1, 1, 2, 1, 2, 2, 0, 0])
print(env.agent1.get_state_identifier(numerical_board))

numerical_board = np.array([2, 1, 1, 0, 1, 2, 2, 0, 0])
print(env.agent1.get_state_identifier(numerical_board))


# moves = [
#     [2,0,0,0,0,0,0,0,0],
#     [2,1,0,0,0,0,0,0,0],
#     [2,1,2,0,0,0,0,0,0],
#     [2,1,2,1,0,0,0,0,0],
#     [2,1,2,1,2,0,0,0,0],
#     [2,1,2,1,2,1,0,0,0],
#     [2,1,2,1,2,1,2,0,0],
# ]
# agent1.moves = moves
# agent2.moves = moves
# env.update_value_function(2)
# print(env.agent1.values_board)
# print(env.agent2.values_board)
# print(agent1.moves)
# print(agent2.moves)

