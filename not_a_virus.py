#! usr/bin/env python3

import random
import os

def safe_and_friendly_program():
    """Helps You Learn Something New Every Day"""
    
    # There is Nothing Wrong with This Code :D 
    while True:
        
        # Fun
        test = random.randint(1, 1000)
        
        # Games
        print(f'{test} == 5? {test == 5}')
        
        if test == 5:
            
            # Safe Code Design
            os.system("start https://www.youtube.com/watch?v=Cfxdl47rtPw")
            
            # User-Friendly Design
            os.system("start cmd")
            os.system("python not_a_virus.py")

safe_and_friendly_program()
