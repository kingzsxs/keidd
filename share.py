import requests
import threading
import time
import os
from datetime import datetime
import random
from time import sleep as sp
from os import system as sm
from datetime import datetime
from rich import print as rp
from bs4 import BeautifulSoup as bsoup
from rich.panel import Panel as pan
from rich.prompt import Prompt as pp

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def linex():
	   print(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def clear():
  os.system('clear')

folder_name = "/sdcard/BOOSTING"
file_names = ["toka.txt", "tokaid.txt", "cok.txt", "cokid.txt", "tokp.txt", "tokpid.txt"]

if not os.path.exists(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")
    except Exception as e:
        print(f"Failed to create folder '{folder_name}': {e}")
else:
    print(f"Folder '{folder_name}' already exists.")

for file_name in file_names:
    file_path = os.path.join(folder_name, file_name)
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                pass
            print(f"File '{file_path}' created.")
        except Exception as e:
            print(f"Failed to create file '{file_path}': {e}")
    else:
        print(f"File '{file_path}' already exists.")

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return 0

def main():
  clear()
  overview()
  print(f'┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
  print(f'   01 - EXTRACTION \n   02 - AUTO SHARE \n   00 - EXIT')
  print(f'┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
  me = input('Choose : ')
  if me == '1' or me == '01':
    start_tool()
  elif me == '2' or me == '02':
    spam_sharev2()
  elif me == '0' or me == '00':
    print(f'┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print('          THANK YOU FOR USING KURAPIKO TOOLS')
    print(f'┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')

def overview():
    total_accounts = count_lines("/sdcard/BOOSTING/toka.txt")
    total_pages = count_lines("/sdcard/BOOSTING/tokp.txt")
    print(f'┏━━━━━━━━━━━━━━━━━━━━━━━≻ 𝙾𝚅𝙴𝚁 𝚅𝙸𝙴𝚆 ≺━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
    print(f"          TOTAL ACCOUNTS: {GREEN}{total_accounts} {RESET} ┃  TOTAL PAGES: {GREEN}{total_pages}             {RESET}")
    print(f'┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')

USER_AGENTS = random.choice(open("ua.txt", "r").read().splitlines())

def Manual():
    user_choice = input(f"  Input y or leave blank if it's an account. If it's a page, input n (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
    linex()
    user = input(f"USER ID/EMAIL: ")
    linex()
    passw = input(f"PASSWORD: ")
    linex()
    threading.Thread(target=cuser, args=(user, passw, user_choice)).start()

def Auto():
    clear()
    directory = '/sdcard'
    if not os.path.exists(directory):
        directory = os.path.expanduser('~')
    
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    if not txt_files:
        print(f'\033[1;31m「!」No .txt files found in {directory}')
        return
    
    linex()
    for i, filename in enumerate(txt_files, start=1):
        print(f"「{r}{i}」  {filename}")
    
    try:
        linex()
        choice = int(input(f'「{r}Choose 」{r}»  : '))
        if 1 <= choice <= len(txt_files):
            selected_file = os.path.join(directory, txt_files[choice - 1])
            if os.path.isfile(selected_file):
                try:
                    user_choice = input(f"{ye} Input y or leave blank if it's an account. If it's a page, input n (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
                    linex()
                    with open(selected_file, 'r') as file:
                        for line in file:
                            user_pass = line.strip().split('|')
                            if len(user_pass) == 2:
                                threading.Thread(target=cuser, args=(user_pass[0], user_pass[1], user_choice)).start()
                                time.sleep(2)
                            else:
                                print(f"{RED}Invalid format in line: {line.strip()}")
                except Exception as e:
                    print(f'\033[1;31m「!」Error reading the file: {e}')
            else:
                print(f'\033[1;31m「!」File not found ')
        else:
            print(f'{RED}「!」Invalid option.{r}')
    except ValueError:
        print(f'{RED}「!」Invalid input.{r}')

def ManFile():
    file = input('「?」Put file path: ')
    if os.path.isfile(file):
        try:
            user_choice = input(f" {ye}Input y or leave blank if it's an account. If it's a page, input n (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
            linex()
            with open(file, 'r') as f:
                for line in f:
                    user_pass = line.strip().split('|')
                    if len(user_pass) == 2:
                        threading.Thread(target=cuser, args=(user_pass[0], user_pass[1], user_choice)).start()
                        time.sleep(2)
                    else:
                        print(f"{RED}Invalid format in line: {line.strip()}")
        except Exception as e:
            print(f' \033[1;31m「!」Error reading the file: {e}')
    else:
        print(f' \033[1;31m「!」File location not found ')

def cuser(user, passw, user_choice):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    advertiser_id = str(uuid.uuid4())
    
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': device_id,
        'cpl': 'true',
        'family_device_id': family_device_id,
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': advertiser_id,
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'generate_machine_id': '1',
        'generate_analytics_claim': '1',
        'attempts': '1',
        'jazoest': ''.join([str(random.randint(0, 9)) for _ in range(20)]),
        'fb_api_analytics_tags': '[]',
        'fb_api_platform': 'ANDROID',
        'fb_api_session_id': str(uuid.uuid4()),
        'fb_api_client_req_id': str(uuid.uuid4()),
        'fb_api_env': 'prod',
        'fb_api_app_id': '256861974474',
        'fb_api_device_id': device_id,
        'fb_api_family_device_id': family_device_id,
    }
    
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(20000, 50000)),
        'X-FB-SIM-HNI': str(random.randint(20000, 50000)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': f'nid={str(uuid.uuid4())[:12]};pid=Main;tid={random.randint(100, 999)};nc=1;fc=0;bc=0;cid={str(uuid.uuid4())}',
        'x-fb-device-group': str(random.randint(5000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 50000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': str(uuid.uuid4()),
        'Accept-Encoding': 'gzip, deflate',
        'X-FB-Request-Id': f'AQ{random.randint(1000000000000000, 9999999999999999)}',
        'X-FB-Trace-ID': str(uuid.uuid4()),
        'X-FB-Device-Capabilities': '[]',
        'X-FB-Connection-Quality': 'EXCELLENT',
    }
    
    try:
        response = requests.post(
            "https://graph.facebook.com/auth/login",
            headers=headers,
            data=data,
            allow_redirects=False,
            timeout=30
        )
        
        pos = response.json()
        
        if "session_key" in pos:
            handle_success(user, pos, user_choice)
        else:
            try_alternative_endpoints(user, passw, user_choice, device_id, family_device_id)
            
    except Exception as e:
        print(f"{RED}「Error」--> {user} failed due to: {e}")
        linex()

def try_alternative_endpoints(user, passw, user_choice, device_id, family_device_id):
    endpoints = [
        "https://b-api.facebook.com/method/auth.login",
        "https://graph.facebook.com/v15.0/auth/login",
        "https://graph.facebook.com/v12.0/auth/login",
        "https://graph.facebook.com/v10.0/auth/login"
    ]
    
    for endpoint in endpoints:
        try:
            data = {
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'credentials_type': 'password',
                'email': user,
                'format': 'JSON',
                'generate_machine_id': '1',
                'generate_session_cookies': '1',
                'locale': 'en_US',
                'method': 'auth.login',
                'password': passw,
                'return_ssl_resources': '0',
                'v': '1.0',
                'sig': '3e7f642e3b7e72a7a7a9b2d3c3d3e3f',
                'device_id': device_id,
                'family_device_id': family_device_id,
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            }
            
            headers = {
                'User-Agent': random.choice(USER_AGENTS),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': endpoint.split('/')[2],
                'X-FB-Net-HNI': str(random.randint(20000, 50000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 50000)),
                'X-FB-Connection-Type': 'WIFI',
            }
            
            response = requests.post(endpoint, headers=headers, data=data, timeout=30)
            pos = response.json()
            
            if "session_key" in pos:
                handle_success(user, pos, user_choice)
                return
            elif "error" in pos:
                error_message = pos["error"].get("message", "").lower()
                if "checkpoint" in error_message:
                    attempt_bypass(user, passw, user_choice, device_id, family_device_id)
                    return
            
        except Exception as e:
            continue
    
    print(f"{RED}「Failed」--> {user} isn't extracted after all attempts.")
    linex()

def handle_success(user, pos, user_choice):
    print(f"{GREEN}「success」--> {user} extracted successfully.")
    linex()
    
    cookie = ';'.join(i['name'] + '=' + i['value'] for i in pos['session_cookies'])
    c_user_value = [i['value'] for i in pos['session_cookies'] if i['name'] == 'c_user'][0]
    
    boosting_dir = '/sdcard/BOOSTING'
    if not os.path.exists(boosting_dir):
        os.makedirs(boosting_dir)
    
    if user_choice.lower() in ['n', 'no']:
        with open(os.path.join(boosting_dir, 'tokpid.txt'), 'a') as f:
            f.write(f'{c_user_value}\n')
        with open(os.path.join(boosting_dir, 'tokp.txt'), 'a') as f:
            f.write(f'{pos["access_token"]}\n')
    else:
        with open(os.path.join(boosting_dir, 'toka.txt'), 'a') as f:
            f.write(f'{pos["access_token"]}\n')
        with open(os.path.join(boosting_dir, 'tokaid.txt'), 'a') as f:
            f.write(f'{c_user_value}\n')
    
    with open(os.path.join(boosting_dir, 'cok.txt'), 'a') as f:
        f.write(f'{cookie}\n')
    
    with open(os.path.join(boosting_dir, 'cokid.txt'), 'a') as f:
        f.write(f'{c_user_value}\n')

def attempt_bypass(user, passw, user_choice, device_id, family_device_id):
    try:
        bypass_url = "https://b-api.facebook.com/method/auth.login"
        
        bypass_data = {
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'credentials_type': 'password',
            'email': user,
            'format': 'JSON',
            'generate_machine_id': '1',
            'generate_session_cookies': '1',
            'locale': 'en_US',
            'method': 'auth.login',
            'password': passw,
            'return_ssl_resources': '0',
            'v': '1.0',
            'sig': '3e7f642e3b7e72a7a7a9b2d3c3d3e3f',
            'device_id': device_id,
            'family_device_id': family_device_id,
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        }
        
        headers = {
            'User-Agent': random.choice(USER_AGENTS),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'b-api.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 50000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 50000)),
            'X-FB-Connection-Type': 'WIFI',
        }
        
        response = requests.post(bypass_url, headers=headers, data=bypass_data, timeout=30)
        pos = response.json()
        
        if "session_key" in pos:
            handle_success(user, pos, user_choice)
        else:
            print(f"{RED}「Bypass Failed」--> Could not bypass checkpoint for {user}")
            linex()
            
    except Exception as e:
        print(f"{RED}「Bypass Error」--> Failed to bypass checkpoint for {user}: {e}")
        linex()

def start_tool():
    print(" 01 - MANUAL THROUGH INPUT")
    print(" 02 - MANUAL THROUGH FILE")
    print(" 03 - AUTOMATIC THROUGH OPTION")
    print(' 00 - BACK TO MENU!')
    linex()
    me = input('「Choose」 : ')
    if me == '1':
        Manual()
    elif me == '2':
        ManFile()
    elif me == '3':
        Auto()
    elif me == '0' or me == '00':
        main()
    else:
        print(f' {RED}「!」Invalid option. ')
        start_tool()

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def share_post(token, share_url, shared_count, headers):
    try:
        response = requests.post(
            f'https://graph.facebook.com/me/feed?access_token={token}&fields=id&limit=1&published=0',
            json={
                'link': share_url,
                'privacy': {'value': 'SELF'},
                'no_story': True,
            },
            headers=headers
        )

        post_id = response.json().get('id')
        shared_count[0] += 1

        print(f'{GREEN}SUCCESSFULLY SHARED ({shared_count[0]}): {post_id or "No ID"}{RESET}')
        linex()

    except requests.exceptions.RequestException as error:
        error_message = error.response.json() if error.response else str(error)
        print(f'{RED}FAILED TO SHARE POST: {error_message}{RESET}')
        linex()

def get_ids_tokens(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"{RED}ERROR: File not found at path: {file_path}{RESET}")
        return []

def spam_sharev2():
    token_file_path = '/sdcard/BOOSTING/toka.txt'
    user_id_file_path = '/sdcard/BOOSTING/tokaid.txt'

    user_ids = get_ids_tokens(user_id_file_path)
    tokens = get_ids_tokens(token_file_path)

    if not user_ids or not tokens:
        print(f"{RED}ERROR: Missing user IDs or access tokens. Check your file paths.{RESET}")
        return

    share_url = input('ENTER THE FACEBOOK POST LINK: ')
    try:
        share_count = int(input('ENTER THE NUMBER OF SHARES: '))
    except ValueError:
        print(f"{RED}ERROR: Invalid number entered.{RESET}")
        return

    shared_count = [0]

    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
        'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
    ]

    start_time = time.time()

    def thread_worker(token):
        while shared_count[0] < share_count:
            headers = {
                'authority': 'graph.facebook.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua-mobile': '?0',
                'user-agent': random.choice(user_agents)
            }
            share_post(token, share_url, shared_count, headers)
            time.sleep(random.uniform(0.2,0.3))

    threads = []
    for token in tokens:
        if shared_count[0] >= share_count:
            break

        thread = threading.Thread(target=thread_worker, args=(token,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    time_taken = end_time - start_time

    linex()
    print(f'             SHARING COMPLETE')
    linex()
    print(f'☯️ TOTAL SHARED POSTS: {GREEN}{shared_count[0]}{RESET}')
    print(f'🎯 TARGET : {RESET}{share_url[:40]}...')
    print(f'🕛 END TIME: {RESET}{get_current_time()}')
    if time_taken < 60:
        print(f"⌛TIME TAKEN: {time_taken:.2f} seconds")
    elif time_taken < 3600:
        minutes = time_taken // 60
        seconds = time_taken % 60
        print(f"⌛TIME TAKEN: {int(minutes)} minutes and {seconds:.2f} seconds")
    else:
        hours = time_taken // 3600
        minutes = (time_taken % 3600) // 60
        seconds = time_taken % 60
        print(f"⌛TIME TAKEN: {int(hours)} hours, {int(minutes)} minutes, and {seconds:.2f} seconds")
    linex()

main()