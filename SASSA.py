#!/usr/bin/env python3
# -*- codeing: UFT-8 -*-

import sys, time, os, random

if sys.version_info[0] < 3:
        raise Exception("You must run SASSA as python 3!\n Try running {apt, rpm, etc} install python3 or download from python.org/getit")

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.LOGGING]
random.shuffle(color_random)

def clearScr():
    os.system('clear')

helpmenu = color.RED + '''
 __    __   _______  __      .______   
|  |  |  | |   ____||  |     |   _  \  
|  |__|  | |  |__   |  |     |  |_)  | 
|   __   | |   __|  |  |     |   ___/  
|  |  |  | |  |____ |  `----.|  |      
|__|  |__| |_______||_______|| _|      
                                       
''' + color.END + '''
        \n[!] SASSA Command Line (CLI) Help [!]

    exit    -   Exit's SASSA
    start   -   starts a proc by SASSA
        Sub commands:
          
          start-gui             -       Starts the GUI of SASSA
          start-metasploit      -       Starts the MetaSploit Framework
          start-fsociety        -       Starts Fsociety
          start-nmap            -       Starts nmap
          start-nmap_scan       -       Runs nmap on your specifyed network
          
    help                -   Shows the CLI help page
    exec-system_cmd     -   Dose a command.
''' + color.END

def sassa-gui():
    

menu = color_random[0] + '''
  ██████  ▄▄▄        ██████   ██████  ▄▄▄      
▒██    ▒ ▒████▄    ▒██    ▒ ▒██    ▒ ▒████▄    
░ ▓██▄   ▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒██  ▀█▄  
  ▒   ██▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░██▄▄▄▄██ 
▒██████▒▒ ▓█   ▓██▒▒██████▒▒▒██████▒▒ ▓█   ▓██▒
▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░
░ ░▒  ░ ░  ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒   ▒▒ ░
░  ░  ░    ░   ▒   ░  ░  ░  ░  ░  ░    ░   ▒   
      ░        ░  ░      ░        ░        ░  ░''' + color.END + color.IMPORTANT + '''


      SASSA Exploit Famework on python 3
      Made by: CRO-THEHACKER
      SASSA 1.0 - SASSAFRAMEWORK - sassaproject.tk\n\n''' + color.END

# Start Shell
clearScr()
print(menu)
while True:
    sassainput = input('SASSA$~ ')
    if sassainput.strip() == 'exit':
        clearScr()
        print("Thanks for using SASSA!")
        break
    elif sassainput == 'help':
        print(helpmenu)
    elif sassainput == 'start sassa-gui':
        sassa-gui()
    else:
        print("{}: command not found!".format(sassainput))