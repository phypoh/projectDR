#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:31:08 2020

@author: phypoh
"""

# Starting Inventory
inventory = {
    "stitches": 0, 
    "bandages" : 0 , 
    "painkillers": 0
    } 


def misc_commands(command):
    if command == "h":
        help_commands()
        return True
        
    elif command == "i":
        print(inventory)
    
    else:
        unknown_command()
        return True


def help_commands():
    print("List of commands:")
    print("e - exit game without saving")
    print("h - help")
    print("i - inventory")
    print("\n")
    
    print("Day Phase Commands:")
    print("s - search the area")
    print("\n")
    
    print("Night Phase Commands:")
    print("s - sleep and progress to Day Phase")
    print("t - talk to a team member")
    
    pass
    

def unknown_command():
    print("Unknown command, please try again. For a list of general commands, please enter h.")