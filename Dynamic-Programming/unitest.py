import sys
sys.path.append('../ReinforcementLearning')

import unittest
test = unittest.TestCase()

from shared.GridWorld import ConcreateGrid
from dynamic_programming import DynamicProgramming


concreate_grid = ConcreateGrid(3,4)
concreate_grid.set_goal_position(3)
concreate_grid.set_negative_goal_position(7)
concreate_grid.set_start_position(8)
concreate_grid.set_block_positions([5])
concreate_grid.show_grid_positions()

# testing if we get the correct state number based on position
test.assertEqual(concreate_grid.get_state_number(0,0), 0)
test.assertEqual(concreate_grid.get_state_number(0,1), 1)
test.assertEqual(concreate_grid.get_state_number(0,2), 2)
test.assertEqual(concreate_grid.get_state_number(0,3), 3)
test.assertEqual(concreate_grid.get_state_number(1,1), 5)
test.assertEqual(concreate_grid.get_state_number(1,2), 6)
test.assertEqual(concreate_grid.get_state_number(2,3), 11)

d = DynamicProgramming(concreate_grid)
d.set_actions()
actions  = d.grid_world_actions
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

row, col = d.get_position(3)
test.assertEqual(row, 0)
test.assertEqual(col, 3)

row, col = d.get_position(4)
test.assertEqual(row, 1)
test.assertEqual(col, 0)

row, col = d.get_position(6)
test.assertEqual(row, 1)
test.assertEqual(col, 2)

row, col = d.get_position(11)
test.assertEqual(row, 2)
test.assertEqual(col, 3)

reward = d.get_reward(0)
test.assertEqual(reward, -0.1)

reward = d.get_reward(3)
test.assertEqual(reward, 1)

reward = d.get_reward(7)
test.assertEqual(reward, -1)

reward = d.get_action_reward(0, 'R')
test.assertEqual(reward, -0.1)

reward = d.get_action_reward(3, 'D')
test.assertEqual(reward, -1)

reward = d.get_action_reward(6, 'R')
test.assertEqual(reward, -1)

reward = d.get_action_reward(2, 'R')
test.assertEqual(reward, 1)

reward = d.get_action_reward(11, 'U')
test.assertEqual(reward, -1)

