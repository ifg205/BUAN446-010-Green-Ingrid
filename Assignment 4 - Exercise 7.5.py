# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 11:46:34 2023

@author: ifg205
"""

#Exercise 7.5 - Flattending arrays with Flatten vs. ravel

""" Using the array created in Exercise 7.4 (create an array from a list 
of two lists.  The first list consists of the even numbers counting down 
from 10 to 0 and the second counting up frmo 0 to 10)  first flatten the 
array with the method flatten.  Change the second element of the new array
to 10. Compare the new and the original array.  Second, flaten the array
using the method ravel and perfom the same comparison."""

import numpy as np


list1 = [number for number in range(10,-1,-2)]
print("list1:",list1)

list2 = [number for number in range(0,11,2)]
print("list2:",list2)

original_array = np.stack((list1,list2))
print("original_array: \n", original_array)
print("ID original_array: ", id(original_array))
    
new_array = original_array.flatten()   
print("new_array with flatten: \n", new_array)
print("ID new_array: ", id(new_array))

new_array[1] = 10
print("new_array with second element changed to 10 \n", new_array)
print("ID new_array: ", id(new_array))

print("compare:", original_array == new_array)


new_array = original_array.ravel()   
print("new_array with ravel: \n", new_array)
print("ID new_array: ", id(new_array))

print("compare:", original_array == new_array)
