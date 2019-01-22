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


class GreedyEpsilon:
    """
    Defining the has a realtionship with Slot Machine
    """
    
    def __init__(self, slot_machines : List[SlotMachine], epsilon_exploration_percentage : float):
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
        return np.argmax([machine.mean_reward for machine in self.slot_machines])
    
    def draw_plot(self, iterations: int, list_of_means : List[List[float]]):
        for machine_index in range(self.machine_count):
            x_digits = list(range(iterations))
            y_digits = [item[machine_index] for item in list_of_means]
            plt.plot(x_digits, y_digits)
        
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
        self.iteration += 1 
#        update our calculated mean
        sum_uptil_previous_iteration = self.slot_machines[machine_index].estimated_mean * (self.iteration - 1)
#        updating the mean
        self.slot_machines[machine_index].estimated_mean = (sum_uptil_previous_iteration + reward) / self.iteration
    
    def draw_bar_graph(self,x_labels: List[str], machine_counts: List[int]):
        """
        Draws the bar graph of how many times each machine was selected
        
        Parameters
        ----------
        
        x_labels: List[str]
            Name of the machines
        
        machine_counts: List[int]
            List containing the number of times each machine was selected
            
        Returns
        -------
        None
        """
        
        plt.bar(x_labels, machine_counts)
        plt.show()
        print(machine_counts)
        
        
        
    def run_greedy_epsilon(self, total_iterations: int):
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
        estimated_means = [[0] * self.machine_count] * total_iterations
        for iteration in range(total_iterations):
#            get value from distribution
            p = np.random.random()
            
#            if p is greater than our exploration percentage, we exploit else we explore
            if p > self.epsilon_exploration_percentage:
#                exploitation
                best_machine_index = self.get_the_best_machine_index()
            else:
#                exploration
                best_machine_index = np.random.choice(3)
            
#            get the next reward from the mahchine
            next_reward = self.slot_machines[best_machine_index].pull()
#            update the mean reward for the machine
            self.update_estimated_mean_for_given_machine(next_reward , best_machine_index)
            estimated_means[iteration][best_machine_index] = self.slot_machines[best_machine_index].estimated_mean
            selected_machine_count[best_machine_index] +=1
            x_labels = ['Machine'+ str(i+1) for i in range(self.machine_count)]
        self.draw_bar_graph(x_labels, selected_machine_count)
        self.draw_plot(total_iterations , estimated_means)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
            
            
            
    
    