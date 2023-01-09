# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:58:57 2023

@author: ifg205
"""

#Exercise 5.20 - Display multiplication tables

def display_table(mult_table):
    
    index = 0
    for row in mult_table:  # By row
        index += 1
        if index == 1: #if just stating, print heading using values from the first row
            print("  X ",end="")
            for count in range (1,len(row)+1):
                print(f'{count:>3}', end=' ')
            print()
                              #and print a row with dashes
            print("---", end=" ")
            for item in row:
                print(' --', end=' ')
            print()     # end of printing heading 
        
        # for every iteration of row, start with the second operator and pipe    
        print(f'{index:>3}', end='|')
        for item in row:   #then print the table values for that row
            print(f'{item:>3}', end=' ')
        print()
    
    
 #create the multiplication table   for values 1 to 10

table = [list(range(i, i*11, i)) for i in range(1,11)]

display_table(table)
