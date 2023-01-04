# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 10:30:00 2023

@author: ifg205
"""

# Exercise 3.10: Rabbit Births

#initialization
total_does = 0
total_babies = 0

#processing phase

does = int(input('Enter the number of does in the rabbit colony (-1 to end): '))
while (does != -1):
    if does != 0:
        babies = int(input('Enter number of babies born in the last month: '))
        avg_births = babies / does
        print('On average,', avg_births, 'baby rabbits were born for each doe')
        total_does += does
        total_babies += babies
    else:
         print ('You can\'t have zero does')
         
    # get next value     
    does = int(input('Enter the number of does in the rabbit colony (-1 to end): '))
           
#termination phase
if (total_does > 0):
    print ('Total number of baby rabbits for each doe so far:', total_babies/total_does)
    