import json,subprocess


#Kill php localHost
def kill_process():
    try:
     with open( 'Settings.json','r') as pidLog:
       data = json.load(pidLog)
       pid = data["pid"]
       for i in pid:
             subprocess.getoutput(f"killall -9 {i}")
          
       else:
             pid.clear()
             data["pid"] = []
             with open("Settings.json","w") as logs:
                json.dump(data,logs)
                          
    except Exception as e:
         exit(e)
