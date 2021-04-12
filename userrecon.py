#!/usr/bin/python3

import requests
from sys import argv

class Result:
  def __init__(self, service_name: str, exists: bool, username: str, url: str) -> None:
    self.service_name = service_name
    self.exists = exists
    self.username = username
    self.url = url

class UserRecon:
  def __init__(self, username) -> None:
    self.username = username
    self.headers = {"user-agent":"userrecon/1.0"}

  def check_all(self):
    functions = list(filter(lambda item: (item.startswith("check_") and item != "check_all"), dir(self)))
    functions = [getattr(self, f) for f in functions]
    
    for f in functions:
      result: Result = f()
      
      if result.exists:
        print(f"{result.service_name}: {result.url}")
      else:
        print(f"{result.service_name}: Not found")

  def check_facebook(self) -> Result:
    response = requests.get("https://m.facebook.com/"+self.username, headers=self.headers)
    
    return Result("Facebook", True if response.status_code == 200 else False, self.username, response.url)

  def check_tiktok(self) -> Result:
    response = requests.get("https://www.tiktok.com/@"+self.username, headers=self.headers)
      
    return Result("TikTok", True if response.status_code == 200 else False,  self.username, response.url)

  def check_instagram(self) -> Result:
    response = requests.get("https://www.instagram.com/"+self.username, headers=self.headers)
    
    return Result("Instagram", True if response.status_code == 200 else False, self.username, response.url)
  
  def check_lastfm(self) -> Result:
    response = requests.get("https://www.last.fm/user/"+self.username, headers=self.headers)
    
    return Result("Last.fm", True if response.status_code == 200 else False, self.username, response.url)

banner="""
 █    ██   ██████ ▓█████  ██▀███   ██▀███  ▓█████  ▄████▄   ▒█████   ███▄    █ 
 ██  ▓██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ 
▓██  ▒██░░ ▓██▄   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒
▓▓█  ░██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒
▒▒█████▓ ▒██████▒▒░▒████▒░██▓ ▒██▒░██▓ ▒██▒░▒████▒▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░
░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░ ░ ░  ░  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░░░ ░ ░ ░  ░  ░     ░     ░░   ░   ░░   ░    ░   ░        ░ ░ ░ ▒     ░   ░ ░ 
   ░           ░     ░  ░   ░        ░        ░  ░░ ░          ░ ░           ░ 
                                                  ░                by \033[1;36m@shi0n04\033[m
"""

if len(argv) < 2 or len(argv) > 2:
    exit(f"error: invalid argvs\nusage: python3 {argv[0]} username")
    
user_recon = UserRecon(argv[1]).check_all()
