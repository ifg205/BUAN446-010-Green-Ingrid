# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:11:57 2023

@author: ifg205
"""

#Exercise 7.14

import numpy as np

array1 = np.array([[0, 2], [4, 6]])

print("array1:\n",array1)

array2 = np.array([[1, 3], [5, 7]])

print("array2:\n",array2)

array3 = np.hstack((array2, array1))
print("a: array3\n", array3)


array4 = array3[0]
array5=array3[-1]
print("b: array4:\n ",array4, "\narray5:\n", array5  )

array6 = np.hstack((sorted(array4), sorted(array5)))

print("c: array6:\n", array6)

array7 = np.vstack((array6, array6 * 10))
print("d: array 7:\n",array7)
