from typing import List
import numpy as np
import random
class Policy:
    
    def set_deterministic_policy(self, grid_actions):
        #Policy : 
        # if we start from Start state we reach goal else we reach negative goal
        grid_actions[0] = ['R']
        grid_actions[1] = ['R']
        grid_actions[2] = ['R']
        grid_actions[3] = []
        grid_actions[4] = ['U']
        grid_actions[5] = []
        grid_actions[6] = ['R']
        grid_actions[8] = ['U']
        grid_actions[9] = ['R']
        grid_actions[10] = ['R']
        grid_actions[11] = ['U']

        return grid_actions

    def get_random_policy(self, rows: int, cols: int) -> List[str]:
        print(rows,cols)
        policy  = np.full((rows*cols),'R', dtype=str)
        for i in range(rows * cols):
                action = random.choice(['R','L','U','D'])
                policy[i] = action
        return policy
