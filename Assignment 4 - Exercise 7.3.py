# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 11:35:50 2023

@author: ifg205
"""

# Exercise 7.3 Element-wise array multiplication

"""Create a 10-by-10 array containing the number 4 in each position.  Create a 
second 10-by-10 array containing the numbers 1 to 100 in assending order.  
Multiple te first array by the second array."""

import numpy as np

array1 = np.full((10, 10), 4)

print('array1')
print(array1)


array2 = np.arange(1, 101).reshape(10,10)

print('\narray2')
print(array2)

    
array3 = array1 * array2      

print('\narray1 multipled by array2')
print(array3)