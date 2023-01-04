# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:06:01 2023

@author: ifg205
"""

#Exercise 3.16 - Fastest Runners

#initialization
fastest_time = 999999998
second_fastest_time = 999999999

print ('You will be prompted to enter speed (in ms) for each of ten runners')

#processing phase
for count in range(10):
    input_str = input('Enter speed (ms): ')
    if input_str.isdigit(): 
        new_time = int(input_str)
        if (new_time < fastest_time):
            second_fastest_time = fastest_time
            fastest_time = new_time
        elif (new_time < second_fastest_time):
            second_fastest_time = new_time
        #else do nothing
    else:
        print ('Invalid input ignored')
    
#termination phase
print('Fastest time was ', fastest_time)
print('Second fastest time was ', second_fastest_time)

