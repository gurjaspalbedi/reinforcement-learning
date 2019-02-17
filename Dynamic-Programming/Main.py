import sys
sys.path.append('../ReinforcementLearning')


from shared.GridWorld import ConcreateGrid
from dynamic_programming import DynamicProgramming


concreate_grid = ConcreateGrid(3,4)
concreate_grid.set_goal_position(3)
concreate_grid.set_negative_goal_position(7)
concreate_grid.set_start_position(8)
concreate_grid.show_grid_positions()
d = DynamicProgramming(concreate_grid)
d.iterative_policy_evaluation()




