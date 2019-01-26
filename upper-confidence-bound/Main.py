# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:55:12 2019

@author: gurjaspal
"""
import sys
sys.path.append('../ReinforcementLearning')

from SlotMachine import SlotMachine
from UpperConfidenceBound import UpperConfidenceBound
from shared.Graphs import Graphs

"""
Here we create three Slot machines and run or Greedy-Epsilon algorithm
"""
s1 = SlotMachine(1)
s2 = SlotMachine(10)
s3 = SlotMachine(20)
s4 = SlotMachine(30)
slot_machines = [s1, s2, s3, s4]
number_of_iterations = 1000
# 10 percent of the time our algorithm will explore and 90% of the time it will exploit
g = UpperConfidenceBound(slot_machines, Graphs())

#we run the algorithm for the 1000 iterations
g.run(number_of_iterations)


        