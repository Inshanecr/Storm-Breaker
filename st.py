from module import check
check.dependency()
check.check_started()
from module import banner,handler,control
from colorama import Fore
#check.check_update()

while True:
    banner.banner()
    banner.show_menu() 

    try:
        original_menu = input(Fore.RED+" ┌─["+Fore.LIGHTCYAN_EX+"STORM-BREAKER"+Fore.WHITE+"~"+Fore.LIGHTGREEN_EX+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
        
        if  original_menu == "0":
            handler.normal_data()
            
        elif original_menu == "1":
            handler.weather_start()
        
        elif original_menu == "2":
            handler.camera_temp_start()
            
        elif original_menu == "3":
            handler.microphone_temp_start()

        elif original_menu == "4":
            control.kill_php_proc()
            exit(Fore.LIGHTRED_EX+"\n Goodbye :) ")
        
            



    except KeyboardInterrupt:
        control.kill_php_proc()
        exit(Fore.CYAN+"\n Goodbye :)")
