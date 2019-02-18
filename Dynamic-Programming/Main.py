import sys
sys.path.append('../ReinforcementLearning')


from shared.grid import Grid
from shared.policy import Policy
from shared.actions import Actions
from shared.rewards import Rewards
from shared.config import Config
from policyevaluation import PolicyEvaluation
from policyiteration import PolicyIteration
from shared.statesandblockers import StatesAndBlocks


policy = Policy()
config = Config()
states_and_blocks = StatesAndBlocks(config.positive_terminal_states,config.negative_terminal_states,config.starting_states,config.blocking_states)
grid = Grid(config.numer_of_rows,config.number_of_columns , states_and_blocks)
rewards = Rewards(config.positive_reward, config.negative_reward, config.step_reward, states_and_blocks)
grid.show_grid_positions()

actions = Actions(states_and_blocks, rewards, grid)

policy_iteration = PolicyIteration(grid, policy, actions, config.small_change, config.gamma)
policy_iteration.run_policy_iteration()
# d = PolicyEvaluation(grid, policy, actions, config.small_change, config.gamma)
# d.iterative_policy_evaluation()
# d.iterative_policy_evaluation_deterministic()






