# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:00:25 2023

@author: ifg205
"""

#Exercise 5.5: List Slicing
print("List Slicing")

# Create a list called numbers containing the numbers 1 to 20
numbers = [number for number in range(1,21)]

#display various elements of the list
    
print("A list called numbers:",numbers)

print("The third number:", numbers[2])    

print("The first five numbers:", numbers[0:5])

print("The first half of the list:", numbers[0:((len(numbers)//2))])

print("The last five numbers:", numbers[-6: -1])

print("Every other number:", numbers[::2])

print("The numbers in reversed order:", numbers[::-1])
    
print("and the third last number:", numbers[-3])
