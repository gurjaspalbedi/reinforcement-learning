# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 15:45:48 2019

@author: gurjaspal
"""

"""
In this program we create three Slot Machines and try to estimate the mean of all three by pulling number one by one.
"""

import numpy as np 

class SlotMachine:
    """
    This class will be used to declare the slot machines. It will take one number that will be the true mean of the machine
    """
    
    def __init__(self, mean_reward : float):
        """
        Construct a new slot machine given the mean value of reward it returns
        
        Parameters
        ----------
        
        mean_reward: float
            This is the mean value of reward this slot machine will return
        
        
        Returns
        -------
        None
        """
        self.mean_reward = mean_reward
        self.estimated_mean = 100
        self.iteration = 0
        self.number_of_time_selected = 0
    
    
    def pull(self):
        """
        Returns the next reward from the machine. This will be Gaussian distribution with the mean reward defined for the machine.
        
        Returns
        -------
        reward: float
            Reward from the machine
        """
        reward = np.random.randn() + self.mean_reward
#        print(reward, self.mean_reward)
        return reward
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    