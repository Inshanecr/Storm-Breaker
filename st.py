from module import check

#check Some installation And Dependencis
check.dependency()
check.check_update()
check.check_started()
from module.colors import c
from module import handler,localhost,banner,control

while True:
    banner.banner()
    banner.show_menu() 

    try:
        User = input(c.red+" ┌─["+c.lcyan+"STORM-BREAKER"+c.re+"~"+c.lgreen+"@HOME"+c.red+"""]
 └──╼ """+c.green+"$ "+c.pink)
        if User == "1":
           banner.banner()
           handler.weather_info()
        elif User == "2":
           banner.banner()
           handler.nearyou_info()
        elif User == "3":
           banner.banner()
           handler.WebCamInfo()
        elif User == "4":
           banner.banner()          
           handler.MicrophoneInfo()
        elif User == "5":
           banner.Devloper_information()
        elif User == "6":        
            control.kill_process()
            exit(c.lred+"\n Goodbye :) ")

    except KeyboardInterrupt:
      control.kill_process()
      exit(c.cyan+"\n Goodbye :)")
