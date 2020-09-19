#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:24:51 2020

@author: phypoh
"""

import random
import time
from utils import misc_commands

game_over = False




def Day_Phase():
    print("It is now day phase. Press \" s \" to see start searching the disaster area.")
    
    patient_num = 0
    
    while patient_num < 10:
        command = input("Please enter a command: (Type h for list of general commands) \n")
        
        if command == "s":
            print("Patient", patient_num, "seen")
            patient_num += 1
            
        else: 
            misc_commands(command)
    
    
    Night_Phase()
    
def Night_Phase():
    print("You sit by the campfire")
    is_sleep = False
    
    while not is_sleep:
        command = input("Please enter a command: (Type h for list of general commands) \n" )
        
        if command == "t":
            who = input("Who do you want to talk to? \n")
            print("You decide to talk to", who, "(enter filler text)")
            
        elif command == "s":
            print("The night grows dark and it is late.")
            is_sleep = True
            
        else:
            misc_commands(command)
            
    Day_Phase()
    
    
if __name__ == "__main__":
    print("This is a text-based version of the Disaster Relief Game.")
    Day_Phase()
    
    