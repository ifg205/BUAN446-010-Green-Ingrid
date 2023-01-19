# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:33:41 2023

@author: ifg205
"""

# Exercise 7.9

import numpy as np


my_array = np.arange(1, 16).reshape(3,5)

print('\nmy_array')
print(my_array)

print ("a: select row 2: ", my_array[2])

print("b: select column 4: ", my_array[:,4])

print("c: select columns 1-3: \n", my_array[:,1:4])


print ("a: select row  negative 2", my_array[-2])

print("b: select column negative 4: ", my_array[:,-4])

print("c: select columns negative 1 to negative 3: \n", my_array[:,-4:-1])
 

print("d: element in row 1, column 4: ", my_array[0,3])

print("e: all elements from rows 1 and 2 that are in columns 0, 2, 4:\n", my_array[0:2, [0,2,4]])
