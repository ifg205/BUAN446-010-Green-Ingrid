# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:04:33 2023

@author: ifg205
"""

#exercise 4.12: Simulation The tortoise and the hare
import  random

def tortiose_move():
    
    prob = random.randrange(1, 11)
    if prob in [1, 2, 3, 4, 5]:
        #Fast plod
        move = 3
    elif prob in [6,7]:
        #Slip
        move = -6
    else:
        #slow plod
        move = 1
    #print('t', prob, move)    
    return(move)

def hare_move():
    prob = random.randrange(1, 11)
    if prob in [1, 2]:
        #sleep
        move = 0
    elif prob in [3, 4]:
        #big hop
        move = 9
    elif prob in [5]:
        #big slip
        move = -12
    elif prob in [6, 7, 8]:
        #small hop
        move = 1
    else:
        #small slip
        move = -2
    #print ('h',prob, move)    
    return(move)

#initialization

# import sleep to show output for some time period
from time import sleep  # will use to slow down the race and add suspense


print ('BANG!!!!!')
print ('AND THEY\'RE OFF')

tortoise_position = 1
hare_position = 1

#processesing - run the race

while tortoise_position < 70 and hare_position < 70:
    
    #tortoise moves
    tortoise_position += tortiose_move()
    if tortoise_position < 1:
       tortoise_position = 1   
       
    #hare moves   
    hare_position += hare_move()
    if hare_position < 1:
       hare_position = 1   
       
    if hare_position == tortoise_position:  #tortoise and hare in same position - tortoise bites hare  
        print("OUCH!!!")
    
    ## show position on the course
    ## create string with  H or T or space
    else :
        display_string = ''
        for count in range (1,85):
           if count == tortoise_position: 
               display_string = display_string + 'T'
           elif count == hare_position:
               display_string = display_string + 'H'
           else:
               display_string = display_string + ' '
        print(display_string)
        sleep(0.1)
    # input("Press enter for next move")        
        
#termination
if (tortoise_position < 70):
    print("Hare wins: Yuch.")
elif (hare_position < 70):
    print ("TORTOISE WINS!!! YAY!!!")
else:         
    print ("It's a tie")