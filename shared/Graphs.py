"""To draw all type of Grahs

"""
from typing import List
import numpy as np
import matplotlib.pyplot as plt

class Graphs:

        
    def draw_cumulated_average_graph(self, cum_average: List, iterations: int):
        plt.figure(2)
        plt.plot(np.arange(iterations) + 1, cum_average)
        plt.xlabel('Cumulative Average')
        plt.ylabel('Number of Iterations')
        plt.savefig('cumulated_average')
        plt.show()
    
    def draw_plot(self, iterations: int, list_of_means : List):
        plt.figure(1)
        plt.plot(list(range(iterations)) , list_of_means)
        plt.xlabel("Mean reward selected")
        plt.ylabel("Number of iterations")
        plt.savefig("line_graph")
        plt.show()

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
        plt.figure(3)
        plt.xlabel("Number of Time Machine was selected")
        plt.ylabel("Machine Name")
        plt.bar(x_labels, machine_counts)
        plt.savefig("BarGraph.jpg")
        plt.show()