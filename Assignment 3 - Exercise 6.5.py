# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 17:31:47 2023

@author: ifg205
"""

#exercise 6.5: Counting Votes

"""Write a script that uses a dictionary to determine the number of 
votes received by canidates in an election.  The votes are 
concatenated in a string where each vote is separated from the 
next by a comma.  use the techniques you leaned in section 6.2.7"""


from collections import Counter

votes = input("To count votes, enter candidate names separated by commas: ")

#Remove space after a comma
stripped_votes = votes.replace(", ", ",")
 
counter = Counter(stripped_votes.split(','))

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')
 
