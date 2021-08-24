import os, string, random, uuid, threading, time, subprocess, calendar
from os import system
clear = lambda: subprocess.call('cls||clear', shell=True)
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
try:
    import autopy
except ImportError:
    os.system("pip install autopy")
    import autopy
class Xnce():
    def __init__(self):
        try:
            self.proxies = list(open("proxies.txt", "r").read().split('\n'))
        except FileNotFoundError:
            print(f"[-] proxies.txt is missing")
            input()
            exit()
        try:
            self.webhook = open("webhook.txt","r").read()
            self.dis = True
        except:
            print("[-] Discord Webhook Not Found,'webhook.txt'")
            self.dis = False
        self.done, self.error, self.run = 0, 0, True
        self.head = {"user-agent": f"Instagram 195.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"}
        self.claimed_response = ["challenge", '"account_created":true']
        self.check_response = ["username_is_taken", "username_held_by_others"]
        self.error_response = ["signup_block", "generic_request_error"]
        self.unknown_response = ["server error", "html"]
        self.device_id = uuid.uuid4()
        self.password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=15)) + "xnce"
        self.verify_email()
        self.confirmation_code()
        print("[1] Api [2] Web")
        mode = input("[+] Mode: ")
        if mode == "1":
            func = self.api_register
        elif mode == "2":
            func = self.web_register
        else:
            exit()
        clear()
        print(f"""
                    ██╗  ██╗███╗   ██╗ ██████╗███████╗
                    ╚██╗██╔╝████╗  ██║██╔════╝██╔════╝
                     ╚███╔╝ ██╔██╗ ██║██║     █████╗  
                     ██╔██╗ ██║╚██╗██║██║     ██╔══╝  
                    ██╔╝ ██╗██║ ╚████║╚██████╗███████╗
                    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
                                  Instagram: @xnce / @ro1c
                    """)
        self.target = input("[+] Target: ")
        input("[+] Press Enter To Start.. ")
        while self.run:
            threading.Thread(target=func, daemon=True).start()
    def discord(self):
        if self.dis:
            if len(self.target) <= 4:
                timenow = requests.get("http://worldclockapi.com/api/json/est/now").text
                data = {
                    "embeds": [{
                        "description": f"username: {self.target}",
                        "color": 1600899,
                        "author": {"name": "xnce", "icon_url": "https://cdn.discordapp.com/attachments/775671093662449697/870058819902910514/image0.jpg"},
                        "timestamp": timenow[30:52]}
                    ]}
                req = requests.post(self.webhook, json=data)
                if req.status_code!=204:
                    print(f"\n[-] Discord: {req}")
    def claimed(self):
        print(f"\r[+] Claimed: {self.target}")
        open(f"{self.target}.txt", "a").write(f"username: {self.target}\nemail: {self.email}\npassword: {self.password}")
        self.discord()
        autopy.alert.alert(f"[+] Claimed: {self.target}","xnce")
    def random_proxy(self):
        proxy = random.choice(self.proxies)
        self.my_proxy = {'http': proxy, 'https': proxy}
        return self.my_proxy
    def verify_email(self):
        self.email = input("[+] Email: ")
        data = {
            "phone_id": uuid.uuid4(),
            "guid": uuid.uuid4(),
            "device_id": self.device_id,
            "email": self.email,
            "waterfall_id": uuid.uuid4(),
            "auto_confirm_only": "false"
        }
        req = requests.post("https://i.instagram.com/api/v1/accounts/send_verify_email/", headers=self.head, data=data)
        if "email_sent" in req.text:
            print(f"[+] Code Sent To: {self.email}")
            self.coo = req.cookies
        else:
            print(f"[-] {req.text}")
            input()
            exit()
    def confirmation_code(self):
        code = input("[+] Code: ")
        data = {
            "code": code,
            "device_id": self.device_id,
            "email": self.email,
            "waterfall_id": uuid.uuid4()
        }
        req = requests.post("https://i.instagram.com/api/v1/accounts/check_confirmation_code/", headers=self.head, data=data, cookies=self.coo)
        try:
            self.signup_code = req.json()["signup_code"]
            print(f"[+] {req.text}")
            self.run = True
        except:
            print(f"[-] {req.text}")
            input()
            exit()
    def api_register(self):
        urls = ["https://i.instagram.com/api/v1/accounts/create/","https://i.instagram.com/api/v1/accounts/create_business/"]
        for url in urls:
                data = {
                    "is_secondary_account_creation": "false",
                    "jazoest": "22628",
                    "tos_version": "row",
                    "do_not_auto_login_if_credentials_match": "true",
                    "phone_id": uuid.uuid4(),
                    "enc_password": f"#PWD_INSTAGRAM:0:{calendar.timegm(time.gmtime())}:{self.password}",
                    "username": self.target,
                    "first_name": "xnce",
                    "day": "21",
                    "adid": uuid.uuid4(),
                    "guid": uuid.uuid4(),
                    "year": "2000",
                    "device_id": self.device_id,
                    "_uuid": uuid.uuid4(),
                    "email": self.email,
                    "month": "2",
                    "sn_nonce": "eG5jZTAxQGdtYWlsLmNvbXwxNjI1NzkzNTczfNwTqJmxotZlHBK94dF9UxfnoZI08iVeSQ==",
                    "force_sign_up_code": self.signup_code,
                    "waterfall_id": uuid.uuid4(),
                    "qs_stamp": ""
                }
                try:
                    self.req = requests.post(url, headers=self.head, data=data, proxies=self.random_proxy())
                    #print(self.req.text,self.req.status_code)
                    if any(cl in self.req.text for cl in self.claimed_response):
                        self.claimed()
                        self.run = False
                    elif any(ch in self.req.text for ch in self.check_response):
                        self.done += 1
                        system(f"title"+f"[+] Done: {self.done} / Error: {self.error}")
                    elif any(er in self.req.text for er in self.error_response) or self.req.status_code == 429:
                        self.error += 1
                        system(f"title"+f"[+] Done: {self.done} / Error: {self.error}")
                    elif any(un in self.req.text.lower() for un in self.unknown_response) or self.req.text == "":
                        pass
                    else:
                        print(f"[-] {self.req.text} {self.req.status_code}")
                        #self.run = False
                except:
                    pass
    def web_register(self):
        head = {
            "user-agent": 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            "x-asbd-id": '437806',
            "x-csrftoken": 'N7vBsc50LAZeaRPNlbvSXIcHOYYStNPx',
            "x-ig-app-id": '1217981644879628',
            "x-ig-www-claim": '0',
            "x-instagram-ajax": '595724a46b58',
            "x-requested-with": 'XMLHttpRequest'
            }
        data = {
            "email": self.email,
            "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{calendar.timegm(time.gmtime())}:{self.password}",
            "username": self.target,
            "first_name": "xnce",
            "month": "2",
            "day": "21",
            "year": "2000",
            "client_id": self.device_id,
            "seamless_login_enabled": "1",
            "tos_version": "row",
            "force_sign_up_code": self.signup_code
            }
        try:
            self.req = requests.post("https://www.instagram.com/accounts/web_create_ajax/", headers=head, data=data, proxies=self.random_proxy())
            #print(self.req.text,self.req.status_code)
            if any(cl in self.req.text for cl in self.claimed_response):
                self.claimed()
                self.run = False
            elif any(ch in self.req.text for ch in self.check_response):
                self.done += 1
                system(f"title"+f"[+] Done: {self.done} / Error: {self.error}")
            elif any(er in self.req.text for er in self.error_response) or self.req.status_code == 429:
                self.error += 1
                system(f"title"+f"[+] Done: {self.done} / Error: {self.error}")
            elif any(un in self.req.text.lower() for un in self.unknown_response) or self.req.text == "":
                pass
            else:
                print(f"[-] {self.req.text} {self.req.status_code}")
                #self.run = False
        except:
            pass
Xnce()
