import platform,json
from subprocess import getoutput
import os,requests
from module import control
from colorama import Fore
def dependency():

    if platform.uname()[0] == "Windows":
        print("\n This Tool Only Works On Linux Distributions\n")
        
    else:
        pass
   
    red='\033[31m'
    yellow ='\033[33m'
    re ='\033[0m'
    if os.geteuid() != 0:
        exit(red+"You need to have root privileges to run this script !!!\n\n"+re+"Please try again, this time using"+yellow+" 'sudo python3 st.py' ")
    
    check_php = getoutput("php -v")
    if "not found" in check_php:
        exit("please install php \n command > sudo apt install php")
    


    result = getoutput("neofetch")
    if "not found" in result:
        exit("please install neofetch \n command > sudo apt install neofetch")


    try:
        from colorama import Fore,Style
        import requests,ipapi,psutil

    except ImportError:
        exit("please install library \n command > python3 -m pip install -r requirements.txt")

    try: #check Internet Connection 
     requests.get("https://google.com")
    except:
       os.system("clear")
       exit(Fore.RED+"\n[ - ] please Check Your internet Connection\n")
 
      
    http = requests.get("https://api.ipify.org/").text
    
    location = json.loads(requests.get(f"https://geolocation-db.com/json/{http}&position=true").text)['country_code']
    if location == "IR":
       exit(Fore.RED+"\n[-]"+Fore.WHITE+" Please Enable VPN"+Style.RESET_ALL)



def check_started():
    with open("Settings.json", "r") as jsonFile:
        data = json.load(jsonFile)

    if data["is_start"] == False:
        data["is_start"] = True
        with open("Settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)



    elif data["is_start"] == True:
        control.kill_php_proc()
        


def check_update():
    http = requests.get("https://raw.githubusercontent.com/ultrasecurity/Storm-Breaker/main/Settings.json").text
    
    http_json = json.loads(http)

    with open("Settings.json", "r") as jsonFile:

        data = json.load(jsonFile)
        if data['version'] < http_json['version']:
            exit("Please Update Tool")
        
