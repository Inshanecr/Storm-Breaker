import os
from colorama import Fore
from time import sleep
from subprocess import Popen

def banner():
    os.system("clear")
    Popen('neofetch')
    sleep(2)

def show_menu():
    blue='\033[34m'
    sleep(0.1)
    print(Fore.RED+"\n ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below \n")
    sleep(0.1)
    print(Fore.RED+" [0]"+blue+" Get Normal Data "+Fore.YELLOW+"[Without Any Permissions]\n")
    sleep(0.1)
    print(Fore.RED+" [1]"+blue+" Get Location "+Fore.GREEN+"[SMARTPHONES]\n")
    sleep(0.1)
    print(Fore.RED+" [2]"+blue+" Access Webcam\n") 
    sleep(0.1)
    print(Fore.RED+" [3]"+blue+" Access Microphone \n")
    sleep(0.1)
    print(Fore.RED+" [4]"+blue+" Exit . . .\n")
