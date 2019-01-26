# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:21:29 2019

@author: gurjaspal
"""

"""
    This class takes a slot machine and tries to estimate the true mean of the machine. The machine is defined in SlotMachine class.
"""
import numpy as np
from SlotMachine import SlotMachine
from typing import List
import matplotlib.pyplot as plt
import os


class GreedyEpsilon:
    """
    Defining the has a realtionship with Slot Machine
    """
    
    def __init__(self, slot_machines : List[SlotMachine], epsilon_exploration_percentage : float, graphs):
        """
        Initialize Greedy-Epsilon algorithm with list of machines and Epsilon
        which is the perfcentage of time the algorithm should explore various options
        
        Parameters
        ----------
        
        slot_machines: list of type SlotMachines
            This is the list that contains all the slot machines we have with different mean rewards
        
        epsilon_exploration_percentage: float
            Value between 0 and 1, represents the fraction of time algorithm should explore rather than exploit
            
        Returns
        -------
            None
        
        Raises
        ------
        ValueError
            Raises the value error if the value of 'epsilon_exploration_percentage' is not between 0 and 1
        """
        if epsilon_exploration_percentage < 0 or epsilon_exploration_percentage > 1:
            raise ValueError("epsilon_exploration_percentage is not between 0 and 1")
        
        self.slot_machines = slot_machines
        self.epsilon_exploration_percentage = epsilon_exploration_percentage
        self.machine_count = len(slot_machines)
        # The number of iteration
        self.iteration = 0
        self.estimated_means_each_iteration = []
        self._graphs = graphs
    
    def estimated_means_after_each_iteration(self):
        """
        Stores the estimated means after each iteration
            
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        means = [slot_machine.estimated_mean for slot_machine in self.slot_machines]
        self.estimated_means_each_iteration.append(means)
        
    def get_the_best_machine_index(self) -> int:
        """
        Returns the best available machine which should be played by the user
        
        Parameters
        ----------
        None
        
        Returns
        -------
        Index : int
            The index of the machine
        """
        estimated_means = [machine.estimated_mean for machine in self.slot_machines]
        selected_machine = np.argmax(estimated_means)
#        print(estimated_means, selected_machine)
        return selected_machine
   
    def update_estimated_mean_for_given_machine(self , reward : float, machine_index: int):
        """
        After we get the number from the machine we update our calculate mean and also the number
        of iterations
        
        Parameters
        ----------
        reward: float
            Reward by slot machine
        
        machine_index: int
            Index of the machine you want to update the estimated mean
        
        Returns
        -------
        None
        """
#        increasing the number of iteration
        machine = self.slot_machines[machine_index]
        machine.iteration += 1
#        update our calculated mean
        sum_uptil_previous_iteration = machine.estimated_mean * (machine.iteration - 1)
#        updating the mean
        estimated_mean = (sum_uptil_previous_iteration + reward) / machine.iteration
#        print("estimated mean and reward")
#        print(estimated_mean, reward)
        self.slot_machines[machine_index].estimated_mean = estimated_mean
        self.estimated_means_after_each_iteration()
          
    def run(self, total_iterations: int):
        """
        Run Greedy Epsilon for given number of iterations
        
        Parameters
        ----------
        total_iterations: int
            Number of iterations you want to run the Greedy Epsilon
        
        Returns
        -------
        None
        """  
        
#        we use a list to cound the number of times each Machine is selected
        selected_machine_count = np.zeros(self.machine_count)
        reward_each_iteration = []
        rewards = []
        for iteration in range(total_iterations):
#            get value from distribution
            p = np.random.random()
            
#            if p is greater than our exploration percentage, we exploit else we explore
            if p > self.epsilon_exploration_percentage:
#                exploitation
                best_machine_index = self.get_the_best_machine_index()
            else:
#                exploration
                best_machine_index = np.random.choice(self.machine_count)
#            get the next reward from the mahchine
            next_reward = self.slot_machines[best_machine_index].pull()
            rewards.append(next_reward)
            reward_each_iteration.append(next_reward)
#            update the mean reward for the machine
            self.update_estimated_mean_for_given_machine(next_reward , best_machine_index)
            selected_machine_count[best_machine_index] +=1
        x_labels = ['Machine'+ str(i+1) for i in range(self.machine_count)]
        print(os.path.dirname(__file__))
        self._graphs.draw_plot(total_iterations , reward_each_iteration , os.path.dirname(__file__))
        self._graphs.draw_bar_graph(x_labels, selected_machine_count , os.path.dirname(__file__))
        self._graphs.draw_cumulated_average_graph(np.cumsum(rewards) / (np.arange(total_iterations)+ 1), total_iterations, os.path.dirname(__file__))