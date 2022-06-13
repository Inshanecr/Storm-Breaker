import subprocess
from module import check
check.dependency()
from module.colors import c
from module import handler,localhost,banner
while True:
    banner.banner()
    banner.show_menu() 

    try:
        User = input(c.red+" ┌─["+c.lcyan+"STORM-BREAKER"+c.re+"~"+c.lgreen+"@HOME"+c.red+"""]
 └──╼ """+c.green+"$ ")
        if  User == "1":
           banner.banner()
           handler.normal_data()
        elif User == "2":
           banner.banner()
           handler.weather_info()
        elif User == "3":
           banner.banner()
           handler.nearyou_info()
        elif User == "4":
           banner.banner()
           handler.WebCamInfo()
        elif User == "5":
           banner.banner()          
           handler.MicrophoneInfo()
        elif User == "6":
           banner.Devloper_information()
        elif User == "7":        
            localhost.kill()
            exit(c.lred+"\n Goodbye :) ")
        

    except Exception as e: 
       print(e)
       sleep(5)
       localhost.kill()   
    except KeyboardInterrupt:
      localhost.kill()
      exit(c.cyan+"\n Goodbye :)")
