# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:53:49 2023

@author: ifg205
"""

# Exercise 7.20: Performance Analysis
"""use timeit% to determine execution time for populating
    1) a list 
    2) a one-dimensional array 
For both data types, use the same method to generate a random number 
between 1 and 6 (die roll) to populate the elements.

Get the performance metric of each for 1, 10, 100, 1,000, 10,000, 100,000, 
and 1,000,000 data elements """

import random
import numpy as np

exponent = 0

while exponent <= 6:
    magnitude = 10**exponent
    print("\nnumber of elements: ", magnitude)
    #rolls_list =    [random.randrange(1, 7) for i in range(0, magnitude)]
    print("list average execution time:")
    %timeit rolls_list = [random.randrange(1, 7) for i in range(0, magnitude)]
    
    #rolls_array = np.array([random.randrange(1, 7) for i in range(0, magnitude)])
    print("array average execution time:")
    %timeit rolls_array = np.array([random.randrange(1, 7) for i in range(0, magnitude)])
    
    exponent += 1
    
    

  


