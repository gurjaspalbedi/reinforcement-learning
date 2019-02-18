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

from policyiteration import PolicyIteration

config  = Config()
policy = Policy()
states_and_blocks = StatesAndBlocks(config.positive_terminal_states,config.negative_terminal_states,config.starting_states,config.blocking_states)
grid = Grid(config.numer_of_rows,config.number_of_columns , states_and_blocks)
rewards = Rewards(config.positive_reward, config.negative_reward, config.step_reward, states_and_blocks)
grid.show_grid_positions()
actions = Actions(states_and_blocks, rewards, grid)

policyIteration = PolicyIteration(grid, policy, actions, config.small_change, config.gamma)
policyIteration.actions.set_actions()
actions  = policyIteration.actions.grid_actions

random_policy = policy.get_random_policy(grid.rows,grid.cols)
test.assertEqual(len(random_policy), (grid.cols*grid.rows))