# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 14:15:26 2022

@author: ifg205
"""

#Exercise 3.1:Validating user input from figure 3.3

# fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
for student in range(10):
    # get one exam result
    result = input('Enter result (1=pass, 2 = fail): ')      # using result as str instead of int
   
    while (result not in('1','2')):  # if entry invalid, re-prompt
        result = input('Please re-enter result (1=pass, 2=fail): ')
        
    if result == '1':
        passes = passes + 1
    else:
        failures = failures + 1

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')