import sys
sys.path.append('../ReinforcementLearning')

import unittest
test = unittest.TestCase()

from shared.grid import Grid
from shared.policy import Policy
from shared.rewards import Rewards
from shared.actions import Actions
from shared.config import Config
from shared.statesandblockers import StatesAndBlocks

from policyevaluation import PolicyEvaluation

config  = Config()
policy = Policy()
states_and_blocks = StatesAndBlocks(config.positive_terminal_states,config.negative_terminal_states,config.starting_states,config.blocking_states)
grid = Grid(config.numer_of_rows,config.number_of_columns , states_and_blocks)
rewards = Rewards(config.positive_reward, config.negative_reward, config.step_reward, states_and_blocks)
grid.show_grid_positions()

# testing if we get the correct state number based on position
test.assertEqual(grid.get_state_number(0,0), 0)
test.assertEqual(grid.get_state_number(0,1), 1)
test.assertEqual(grid.get_state_number(0,2), 2)
test.assertEqual(grid.get_state_number(0,3), 3)
test.assertEqual(grid.get_state_number(1,1), 5)
test.assertEqual(grid.get_state_number(1,2), 6)
test.assertEqual(grid.get_state_number(2,3), 11)

actions = Actions(states_and_blocks, rewards, grid)


d = PolicyEvaluation(grid, policy, actions)
d.actions.set_actions()
actions  = d.actions.grid_actions
test.assertEqual(actions[0], ['D', 'R'])
test.assertEqual(actions[1], ['L', 'R'])
test.assertEqual(actions[2], ['D', 'L', 'R'])
test.assertEqual(actions[3], [])
test.assertEqual(actions[4], ['U','D'])
test.assertEqual(actions[5], [])
test.assertEqual(actions[6], ['U','D', 'R'])
test.assertEqual(actions[7], [])
test.assertEqual(actions[8], ['U', 'R'])
test.assertEqual(actions[9], ['L', 'R'])
test.assertEqual(actions[10], ['U','L', 'R'])
test.assertEqual(actions[11], ['U','L'])

row, col = d.grid.get_position(3)
test.assertEqual(row, 0)
test.assertEqual(col, 3)

row, col = d.grid.get_position(4)
test.assertEqual(row, 1)
test.assertEqual(col, 0)

row, col = d.grid.get_position(6)
test.assertEqual(row, 1)
test.assertEqual(col, 2)

row, col = d.grid.get_position(11)
test.assertEqual(row, 2)
test.assertEqual(col, 3)

reward = rewards.get_reward(0)
test.assertEqual(reward, 0)

reward = rewards.get_reward(3)
test.assertEqual(reward, 1)

reward = rewards.get_reward(7)
test.assertEqual(reward, -1)

reward = d.actions.get_action_reward(0, 'R')
test.assertEqual(reward, 0)

reward = d.actions.get_action_reward(3, 'D')
test.assertEqual(reward, -1)

reward = d.actions.get_action_reward(6, 'R')
test.assertEqual(reward, -1)

reward = d.actions.get_action_reward(2, 'R')
test.assertEqual(reward, 1)

reward = d.actions.get_action_reward(11, 'U')
test.assertEqual(reward, -1)

