from subprocess import getoutput
from module.colors import c
from module.control import kill_process
import platform,requests,os,json
from os import system
#check ALL installation 
def dependency():
    clear = os.system("clear")
    if platform.uname()[0] == "Windows" or getoutput("uname -o") == "Android":
        clear
        exit(c.red+"\n This Tool Only Works On Linux Distributions\n")
    
    if os.geteuid() != 0:
        clear
        exit(c.red+"You need to have root privileges to run this script !!!\n\n"+c.re+"Please try again, this time using"+c.yellow+" 'sudo python3 st.py' ")
    
    check_php = getoutput("php -v")
    if "not found" in check_php:
        clear
        exit(c.red+"please install php \n command > sudo apt install php")    

    check_neofetch = getoutput("neofetch")
    if "not found" in check_neofetch:
        clear
        exit(c.red+"please install neofetch \n command > sudo apt install neofetch")
        
    check_ssh= getoutput("ssh")
    if "not found" in check_ssh:
        clear
        exit(c.red+"please install openssl \n command > sudo apt install openssh")

    try:
        import requests
    except ImportError:
        exit(c.red+"please install library \n command > python3 -m pip install -r requirements.txt")

    try: 
     requests.get("https://google.com")
    except:
       clear
       exit(c.red+"\n[ - ] please Check Your internet Connection\n")
 
      
    http = requests.get("https://api.ipify.org/").text   
    location = json.loads(requests.get(f"https://geolocation-db.com/json/{http}&position=true").text)['country_code']
    if location == "IR":
      clear
      exit(c.red+"\n[-]"+c.green+" Please Enable VPN"+c.re)

#check For user start to kill php locaHost
def check_started():
    with open("Settings.json", "r") as jsonFile:
        data = json.load(jsonFile)

    if data["is_start"] == False:
        data["is_start"] = True
        with open("Settings.json", "w") as jsonFile:
            json.dump(data, jsonFile)
    if data["is_start"] == True:
       kill_process()

#Check git update  
def check_update():
    http = requests.get("https://raw.githubusercontent.com/inshanecr/Storm-Breaker/main/Settings.json").text
    
    http_json = json.loads(http)
    with open("Settings.json", "r") as version:

        data = json.load(version)
        if data['version'] < http_json['version']:
            system("rm -r *")
            exit(c.red+"["+c.re+"*"+c.red+"] Please Update Tool\n"+c.yellow+"Commands => "+c.pink+"cd ..\nrm -r Storm-Breaker\ngit clone https://github.com/inshanecr/Storm-Breaker\ncd Storm-breaker\npython st.py")
        

