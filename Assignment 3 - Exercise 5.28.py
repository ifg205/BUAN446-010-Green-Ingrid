# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:32:58 2023

@author: ifg205
"""

#Exercise 5.28 - Intro to data Science: COVID-19 infection statistics

"""Place the following numbers in a list:
    174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 
            1376, 1502, 894, 665, 1704, 1656, 1342
Use the built-in functions in the statistics module to diplay the following statistics
converning the infection rate: minimum, maximim, range, mean, median, variance, and 
standard deviation"""

import statistics as stats

list = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412, 1301, 1105, 1123, 
        1376, 1502, 894, 665, 1704, 1656, 1342]

print('infection rates:', end=' ')
for item in list:   #then print the table values for that row
    print(f'{item:>3}', end=' ')
print()

print(f'The minimum value is {min(list)}')
print(f'The maximum value is {max(list)}')
print(f'The range is {min(list)} to {max(list)}')
print(f'The mean is {stats.mean(list):.2f}')
print(f'The median is {stats.median(list):.2f}')
print(f'The variance is {stats.variance(list):.2f}')
print(f'The standard deviation is {stats.stdev(list):.4f}')

#for item in sorted(list):   #then print the table values for that row
#    print(f'{item:>3}', end=' ')